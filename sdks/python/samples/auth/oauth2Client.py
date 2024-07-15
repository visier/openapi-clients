from visier.oauth2_apis.configuration import Configuration

from visier.oauth2_apis.api_client import ApiClient

from visier.oauth2_apis.api.o_auth2_api import OAuth2Api


def main():
    config = Configuration()
    api_client = ApiClient(config)
    oauth_client = OAuth2Api(api_client)
    print(oauth_client)



if __name__ == '__main__':
    main()
