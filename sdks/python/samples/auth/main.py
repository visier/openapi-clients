import os

from dotenv import load_dotenv

from visier.model_query_apis import ApiClient, DataModelApi
from visier.model_query_apis import Configuration


def main():
    load_dotenv(override=True)
    api_key = {'ApiKeyAuth': os.getenv('VISIER_APIKEY')}
    configuration = Configuration(
        host=os.getenv('VISIER_HOST'),
        api_key=api_key,
        api_key_auth=os.getenv('VISIER_APIKEY'),
        username=os.getenv('VISIER_USERNAME'),
        password=os.getenv('VISIER_PASSWORD'),
        client_id=os.getenv('VISIER_CLIENT_ID'),
        client_secret=os.getenv('VISIER_CLIENT_SECRET'),
        redirect_uri=os.getenv('VISIER_REDIRECT_URI'))

    api_client = ApiClient(configuration)
    model_client = DataModelApi(api_client)

    properties = model_client.properties('Applicant')
    print(properties)
    productivity_properties = model_client.properties('Productivity')
    print(productivity_properties)



if __name__ == '__main__':
    main()
