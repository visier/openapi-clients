# visier.authentication.AuthenticationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authentication_asid_token_authentication**](AuthenticationApi.md#authentication_asid_token_authentication) | **POST** /v1/admin/visierSecureToken | 
[**authentication_o_auth2_authorize**](AuthenticationApi.md#authentication_o_auth2_authorize) | **GET** /v1/auth/oauth2/authorize | 
[**authentication_o_auth2_token**](AuthenticationApi.md#authentication_o_auth2_token) | **POST** /v1/auth/oauth2/token | 
[**authentication_ticket_authentication**](AuthenticationApi.md#authentication_ticket_authentication) | **POST** /v1/admin/visierSecureTicket | 


# **authentication_asid_token_authentication**
> str authentication_asid_token_authentication(username=username, password=password)



Generate a Visier authentication token

### Example


```python
import visier.authentication
from visier.authentication.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.authentication.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with visier.authentication.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.authentication.AuthenticationApi(api_client)
    username = 'username_example' # str |  (optional)
    password = 'password_example' # str |  (optional)

    try:
        api_response = api_instance.authentication_asid_token_authentication(username=username, password=password)
        print("The response of AuthenticationApi->authentication_asid_token_authentication:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->authentication_asid_token_authentication: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] 
 **password** | **str**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Authentication token response |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authentication_o_auth2_authorize**
> Status authentication_o_auth2_authorize(response_type, client_id, redirect_uri=redirect_uri, scope=scope)



Initiate an OAuth2 authorization code flow.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import visier.authentication
from visier.authentication.models.status import Status
from visier.authentication.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.authentication.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with visier.authentication.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.authentication.AuthenticationApi(api_client)
    response_type = 'response_type_example' # str | The response type. Must be `code`.
    client_id = 'client_id_example' # str | The ID of the pre-registered client application.
    redirect_uri = 'redirect_uri_example' # str | The optional URI to redirect to after authorization. (optional)
    scope = 'scope_example' # str | The OAuth 2.0 scope of the authorization request. Defaults to `read`. (optional)

    try:
        api_response = api_instance.authentication_o_auth2_authorize(response_type, client_id, redirect_uri=redirect_uri, scope=scope)
        print("The response of AuthenticationApi->authentication_o_auth2_authorize:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->authentication_o_auth2_authorize: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **response_type** | **str**| The response type. Must be &#x60;code&#x60;. | 
 **client_id** | **str**| The ID of the pre-registered client application. | 
 **redirect_uri** | **str**| The optional URI to redirect to after authorization. | [optional] 
 **scope** | **str**| The OAuth 2.0 scope of the authorization request. Defaults to &#x60;read&#x60;. | [optional] 

### Return type

[**Status**](Status.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**3XX** | Redirect to authorization page. |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authentication_o_auth2_token**
> str authentication_o_auth2_token(grant_type=grant_type, client_id=client_id, redirect_uri=redirect_uri, code=code, username=username, password=password, asid_token=asid_token)



Generate a JSON Web Token (JWT) for the specified user.

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import visier.authentication
from visier.authentication.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.authentication.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = visier.authentication.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with visier.authentication.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.authentication.AuthenticationApi(api_client)
    grant_type = 'grant_type_example' # str | The grant type. Supported values: - `authorization_code`: The authorization code grant type. - `password`: The password grant type. - `urn:visier:params:oauth:grant-type:asid-token`: The ASID token grant type. (optional)
    client_id = 'client_id_example' # str | The ID of the pre-registered client application. (optional)
    redirect_uri = 'redirect_uri_example' # str | The optional URI to redirect to after authorization. (optional)
    code = 'code_example' # str | The authorization code. Applicable only for authorization code grant type. (optional)
    username = 'username_example' # str | The username of the user to authenticate. Applicable only for password grant type. (optional)
    password = 'password_example' # str | The password of the user to authenticate. Applicable only for password grant type. (optional)
    asid_token = 'asid_token_example' # str | The ASID token. Applicable only for ASID token grant type. (optional)

    try:
        api_response = api_instance.authentication_o_auth2_token(grant_type=grant_type, client_id=client_id, redirect_uri=redirect_uri, code=code, username=username, password=password, asid_token=asid_token)
        print("The response of AuthenticationApi->authentication_o_auth2_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->authentication_o_auth2_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**| The grant type. Supported values: - &#x60;authorization_code&#x60;: The authorization code grant type. - &#x60;password&#x60;: The password grant type. - &#x60;urn:visier:params:oauth:grant-type:asid-token&#x60;: The ASID token grant type. | [optional] 
 **client_id** | **str**| The ID of the pre-registered client application. | [optional] 
 **redirect_uri** | **str**| The optional URI to redirect to after authorization. | [optional] 
 **code** | **str**| The authorization code. Applicable only for authorization code grant type. | [optional] 
 **username** | **str**| The username of the user to authenticate. Applicable only for password grant type. | [optional] 
 **password** | **str**| The password of the user to authenticate. Applicable only for password grant type. | [optional] 
 **asid_token** | **str**| The ASID token. Applicable only for ASID token grant type. | [optional] 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/jwt

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JWT response |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authentication_ticket_authentication**
> str authentication_ticket_authentication(username=username, password=password)



Generate a legacy Visier secure ticket

### Example


```python
import visier.authentication
from visier.authentication.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.authentication.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with visier.authentication.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.authentication.AuthenticationApi(api_client)
    username = 'username_example' # str |  (optional)
    password = 'password_example' # str |  (optional)

    try:
        api_response = api_instance.authentication_ticket_authentication(username=username, password=password)
        print("The response of AuthenticationApi->authentication_ticket_authentication:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->authentication_ticket_authentication: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] 
 **password** | **str**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secure ticket response |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

