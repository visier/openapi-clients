import os

import visier
from urllib3.util.retry import Retry
from visier.authentication import AuthenticationApi
from visier.model_query import DataModelApi

visier_host = 'http://d3m.localdev.local:8000'


class CustomRetry(Retry):
    def __init__(self, read=3, connect=3, total=6, status_forcelist=[401], raise_on_status=True, **kwargs):
        super().__init__(read=read, connect=connect,
                         total=total,
                         status_forcelist=status_forcelist,
                         raise_on_status=raise_on_status,
                         **kwargs)

    def increment(self, *args, **kwargs):
        response = kwargs.get('response')
        if response and response.status == 401:
            self.refresh_token()
        return super().increment(*args, **kwargs)

    def refresh_token(self):
        auth_api = createAuthApi()
        token = auth_api.authentication_asid_token_authentication('ceo@d3m.com', os.getenv('VISIER_PASSWORD'))


def createAuthApi() -> AuthenticationApi:
    auth_config = visier.authentication.Configuration(host=visier_host,
                                                      api_key={'ApiKeyAuth': os.getenv('VISIER_APIKEY')})
    auth_client = visier.authentication.api_client.ApiClient(auth_config)
    return AuthenticationApi(auth_client)


first = True


def refresh_token(model_config: visier.model_query.Configuration):
    return
    global first
    if not first:
        return

    print("Getting auth token")
    auth_api = createAuthApi()
    token = auth_api.authentication_asid_token_authentication('ceo@d3m.com', os.getenv('VISIER_PASSWORD'))
    model_config.api_key['CookieAuth'] = f'VisierASIDToken={token}'
    first = False


def createModelApi() -> DataModelApi:
    model_config = visier.model_query.Configuration(host=visier_host)

    model_config.refresh_api_key_hook = refresh_token
    model_config.retries = CustomRetry()
    model_config.api_key['ApiKeyAuth'] = os.getenv('VISIER_APIKEY')
    model_config.api_key['CookieAuth'] = f'VisierASIDToken='
    # model_config.api_key = {
    #     'ApiKeyAuth': os.getenv('VISIER_APIKEY'),
    #     'CookieAuth': token
    # }
    model_client = visier.model_query.api_client.ApiClient(model_config)

    # model_client.default_headers['Cookie'] = f'VisierASIDToken={token}'
    # model_client.default_headers['apikey'] = os.getenv('VISIER_APIKEY')
    data_model_api = DataModelApi(model_client)

    return data_model_api


modelApi = createModelApi()
applicant = modelApi.data_model_analytic_object('Applicant')
# employee = modelApi.data_model_analytic_object('Employee')


print(object)
