import os

from dotenv import load_dotenv
from visier.api.model_query import Configuration, ApiClient, DataModelApi


def main():
    load_dotenv(override=True)
    configuration = Configuration(
        host=os.getenv('VISIER_HOST'),
        api_key=os.getenv('VISIER_APIKEY'),
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
