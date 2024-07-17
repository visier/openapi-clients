# visier.api.user_management.UserManagementV2Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_users**](UserManagementV2Api.md#add_users) | **POST** /v2/admin/users | Add users
[**delete_users**](UserManagementV2Api.md#delete_users) | **DELETE** /v2/admin/users | Delete users
[**update_users**](UserManagementV2Api.md#update_users) | **PUT** /v2/admin/users | Update users


# **add_users**
> UsersAPIResponseDTO add_users(users_creation_api_request_dto, tenant_code=tenant_code)

Add users

This API allows you to create new users. Administrating tenant users can specify the tenant in which to add these users.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.user_management
from visier.api.user_management.models.users_api_response_dto import UsersAPIResponseDTO
from visier.api.user_management.models.users_creation_api_request_dto import UsersCreationAPIRequestDTO
from visier.api.user_management.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.user_management.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: CookieAuth
configuration.api_key['CookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['CookieAuth'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization: BearerAuth
configuration = visier.api.user_management.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.user_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.user_management.UserManagementV2Api(api_client)
    users_creation_api_request_dto = visier.api.user_management.UsersCreationAPIRequestDTO() # UsersCreationAPIRequestDTO | 
    tenant_code = 'tenant_code_example' # str | Specify the tenant to create a user in. (optional)

    try:
        # Add users
        api_response = api_instance.add_users(users_creation_api_request_dto, tenant_code=tenant_code)
        print("The response of UserManagementV2Api->add_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementV2Api->add_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **users_creation_api_request_dto** | [**UsersCreationAPIRequestDTO**](UsersCreationAPIRequestDTO.md)|  | 
 **tenant_code** | **str**| Specify the tenant to create a user in. | [optional] 

### Return type

[**UsersAPIResponseDTO**](UsersAPIResponseDTO.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [OAuth2Auth](../README.md#OAuth2Auth), [OAuth2Auth](../README.md#OAuth2Auth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_users**
> UsersAPIResponseDTO delete_users(users_delete_api_request_dto, tenant_code=tenant_code)

Delete users

This API allows you to delete an existing user. Administrating tenant users can specify the tenant from which to delete a user.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.user_management
from visier.api.user_management.models.users_api_response_dto import UsersAPIResponseDTO
from visier.api.user_management.models.users_delete_api_request_dto import UsersDeleteAPIRequestDTO
from visier.api.user_management.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.user_management.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: CookieAuth
configuration.api_key['CookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['CookieAuth'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization: BearerAuth
configuration = visier.api.user_management.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.user_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.user_management.UserManagementV2Api(api_client)
    users_delete_api_request_dto = visier.api.user_management.UsersDeleteAPIRequestDTO() # UsersDeleteAPIRequestDTO | 
    tenant_code = 'tenant_code_example' # str | Specify the tenant to delete a user in. (optional)

    try:
        # Delete users
        api_response = api_instance.delete_users(users_delete_api_request_dto, tenant_code=tenant_code)
        print("The response of UserManagementV2Api->delete_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementV2Api->delete_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **users_delete_api_request_dto** | [**UsersDeleteAPIRequestDTO**](UsersDeleteAPIRequestDTO.md)|  | 
 **tenant_code** | **str**| Specify the tenant to delete a user in. | [optional] 

### Return type

[**UsersAPIResponseDTO**](UsersAPIResponseDTO.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [OAuth2Auth](../README.md#OAuth2Auth), [OAuth2Auth](../README.md#OAuth2Auth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_users**
> UsersAPIResponseDTO update_users(users_update_api_request_dto, tenant_code=tenant_code)

Update users

This API allows you to update an existing user's information, such as their display name or if the user is enabled in Visier.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.user_management
from visier.api.user_management.models.users_api_response_dto import UsersAPIResponseDTO
from visier.api.user_management.models.users_update_api_request_dto import UsersUpdateAPIRequestDTO
from visier.api.user_management.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.user_management.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: CookieAuth
configuration.api_key['CookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['CookieAuth'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization: BearerAuth
configuration = visier.api.user_management.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.user_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.user_management.UserManagementV2Api(api_client)
    users_update_api_request_dto = visier.api.user_management.UsersUpdateAPIRequestDTO() # UsersUpdateAPIRequestDTO | 
    tenant_code = 'tenant_code_example' # str | Specify the tenant to update a user in. (optional)

    try:
        # Update users
        api_response = api_instance.update_users(users_update_api_request_dto, tenant_code=tenant_code)
        print("The response of UserManagementV2Api->update_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementV2Api->update_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **users_update_api_request_dto** | [**UsersUpdateAPIRequestDTO**](UsersUpdateAPIRequestDTO.md)|  | 
 **tenant_code** | **str**| Specify the tenant to update a user in. | [optional] 

### Return type

[**UsersAPIResponseDTO**](UsersAPIResponseDTO.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [OAuth2Auth](../README.md#OAuth2Auth), [OAuth2Auth](../README.md#OAuth2Auth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

