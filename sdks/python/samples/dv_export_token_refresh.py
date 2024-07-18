import os

from dotenv import load_dotenv
from visier.api.data_version_export import ApiClient, Configuration, DataVersionExportV1AlphaApi
from visier.api.model_query import Configuration, ApiClient, DataModelApi

def main():
    load_dotenv(override=True)
    config = Configuration(
        host=os.getenv('VISIER_HOST'),
        api_key=os.getenv('VISIER_APIKEY'),
        username=os.getenv('VISIER_USERNAME'),
        password=os.getenv('VISIER_PASSWORD'),
        client_id=os.getenv('VISIER_CLIENT_ID'),
        client_secret=os.getenv('VISIER_CLIENT_SECRET'),
        redirect_uri=os.getenv('VISIER_REDIRECT_URI'))

    api_client = ApiClient(config)
    dv_api = DataVersionExportV1AlphaApi(api_client)

    available = dv_api.get_available_data_versions()
    config.asid_token = 'dummy_token'

    available = dv_api.get_available_data_versions()

    print(available)


if __name__ == '__main__':
    main()
