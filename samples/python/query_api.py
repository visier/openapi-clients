import visier
from visier.authentication import AuthenticationApi
from visier.model_query import DataModelApi

visier_host = 'http://d3m.localdev.local:8000'


def createAuthApi() -> AuthenticationApi:
    auth_config = visier.authentication.Configuration(visier_host)

    auth_client = visier.authentication.api_client.ApiClient(auth_config)
    return AuthenticationApi(auth_client)


def createModelApi(token: str) -> DataModelApi:
    model_config = visier.model_query.Configuration(host=visier_host)
    model_config.api_key = {'Authorization': f'Bearer {token}'}
    model_client = visier.model_query.api_client.ApiClient(model_config)
    return DataModelApi(model_client)


authApi = createAuthApi()
token = authApi.authentication_asid_token_authentication('ceo@d3m.com', 'Visier1234')
print(token)

modelApi = createModelApi(token)
objects = modelApi.data_model_analytic_objects()
