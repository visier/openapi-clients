import datetime
import logging
import os

import visier.model_query_apis
from dotenv import load_dotenv
from visier.authentication_apis import AuthenticationApi
from visier.model_query_apis import Configuration
from visier.model_query_apis.api import DataModelApi, QueryApi
from visier.model_query_apis.api_client import ApiClient
from visier.model_query_apis.models import ListQueryExecutionDTO, ListQuerySourceDTO, QueryTimeIntervalDTO, \
    ListQueryExecutionOptionsDTO, PropertyColumnDTO, QueryPropertyDTO, PropertyReferenceDTO


def setup_logger() -> logging.Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s')

    file_handler = logging.FileHandler('model_query/app.log', mode='a')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger


logger = setup_logger()


def create_auth_api(host: str) -> AuthenticationApi:
    config = visier.authentication_apis.Configuration(host=host)
    api_client = visier.authentication_apis.api_client.ApiClient(config)
    return AuthenticationApi(api_client)


def create_model_query_configuration(host: str, user_name: str, password: str) -> Configuration:
    auth_api = create_auth_api(host)
    token = auth_api.asid_token_authentication(username=user_name, password=password)
    api_key = {
        'ApiKeyAuth': os.getenv('VISIER_APIKEY'),
        'CookieAuth': f'VisierASIDToken={token}',
        'Accept': 'application/json'
    }
    return Configuration(api_key=api_key, host=host)


def refresh_api_key(config: Configuration):
    # Should be implemented logic for refreshing token if necessary
    logger.info("Refreshing token")
    auth_api = create_auth_api(config.host)
    token = auth_api.asid_token_authentication(username=os.getenv('VISIER_USERNAME'),
                                               password=os.getenv('VISIER_PASSWORD'))
    config.api_key['CookieAuth'] = f'VisierASIDToken={token}'


def run_without_token_updating():
    load_dotenv()
    config = create_model_query_configuration(
        os.getenv('VISIER_HOST'),
        os.getenv('VISIER_USERNAME'),
        os.getenv('VISIER_PASSWORD')
    )

    # One of the way to refresh token, still necessary to make some changes in template
    # because currently
    config.refresh_config = refresh_api_key
    # Could be changed retry count or implemented custom retry logic
    # config.retries = CustomRetry() OR config.retries = 5
    # problem is that retry logic is used inside urlib3

    object_id = 'Productivity'

    # Inner api client. Every generated specification will have separated ApiClient
    # Another opportunity is to update ApiClient template or create CustomApiClient with refresh token logic
    api_client = ApiClient(config)

    # Creating custom API client
    data_model_api = DataModelApi(api_client)

    # All method names have prefix like 'data_model_' or 'query_'
    # could be changed in specification operationId
    properties = data_model_api.properties(object_id)
    logger.info(f"Received properties for object {object_id}. Properties: {properties.to_str()}")

    # Creating custom API client
    query_api = QueryApi(api_client)

    list_query_dto = ListQueryExecutionDTO(
        source=ListQuerySourceDTO(analytic_object=object_id),
        time_interval=QueryTimeIntervalDTO(
            from_date_time=datetime.date.today().strftime('%Y-%m-%d'),
            interval_period_type='YEAR',
            interval_period_count=4
        ),
        options=ListQueryExecutionOptionsDTO(limit=10),
        columns=[
            PropertyColumnDTO(
                column_name=prop.display_name,
                column_definition=QueryPropertyDTO(
                    var_property=PropertyReferenceDTO(
                        name=prop.id,
                        qualifying_path=object_id
                    )
                )
            )
            for prop in properties.properties  # Creating query properties from received
        ]
    )
    list_response = query_api.list(list_query_dto)
    logger.info(f"Received query result: {list_response}")


if __name__ == "__main__":
    run_without_token_updating()
