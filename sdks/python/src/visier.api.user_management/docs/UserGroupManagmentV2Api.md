# visier.api.user_management.UserGroupManagmentV2Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_groups**](UserGroupManagmentV2Api.md#create_user_groups) | **POST** /v2alpha/admin/user-groups | Create multiple user groups
[**delete_user_group**](UserGroupManagmentV2Api.md#delete_user_group) | **DELETE** /v2alpha/admin/user-groups/{userGroupId} | Delete a user group
[**delete_user_groups**](UserGroupManagmentV2Api.md#delete_user_groups) | **DELETE** /v2alpha/admin/user-groups | Delete multiple user groups
[**get_user_group**](UserGroupManagmentV2Api.md#get_user_group) | **GET** /v2alpha/admin/user-groups/{userGroupId} | Retrieve the details of a user group
[**get_user_groups**](UserGroupManagmentV2Api.md#get_user_groups) | **GET** /v2alpha/admin/user-groups | Retrieve a list of user groups
[**patch_user_groups**](UserGroupManagmentV2Api.md#patch_user_groups) | **PATCH** /v2alpha/admin/user-groups | Patch multiple user groups
[**put_user_groups**](UserGroupManagmentV2Api.md#put_user_groups) | **PUT** /v2alpha/admin/user-groups | Update multiple user groups


# **create_user_groups**
> UserGroupChangeResponseDTO create_user_groups(user_groups_change_dto)

Create multiple user groups

This API allows you to create new user groups. To specify the tenant in which to add new user groups, administrating tenants can provide an analytic tenant code in the `TargetTenantID` request header.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.user_management
from visier.api.user_management.models.user_group_change_response_dto import UserGroupChangeResponseDTO
from visier.api.user_management.models.user_groups_change_dto import UserGroupsChangeDTO
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
    api_instance = visier.api.user_management.UserGroupManagmentV2Api(api_client)
    user_groups_change_dto = visier.api.user_management.UserGroupsChangeDTO() # UserGroupsChangeDTO | 

    try:
        # Create multiple user groups
        api_response = api_instance.create_user_groups(user_groups_change_dto)
        print("The response of UserGroupManagmentV2Api->create_user_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserGroupManagmentV2Api->create_user_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_groups_change_dto** | [**UserGroupsChangeDTO**](UserGroupsChangeDTO.md)|  | 

### Return type

[**UserGroupChangeResponseDTO**](UserGroupChangeResponseDTO.md)

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

# **delete_user_group**
> UserGroupSingleDeleteResponseDTO delete_user_group(user_group_id, delete_user_group_v2_request)

Delete a user group

This API allows you to delete a specific user group. To specify the tenant in which to delete a user group, administrating tenants can provide an analytic tenant code in the `TargetTenantID` request header or `tenantCode` for each user group in the request body.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.user_management
from visier.api.user_management.models.delete_user_group_v2_request import DeleteUserGroupV2Request
from visier.api.user_management.models.user_group_single_delete_response_dto import UserGroupSingleDeleteResponseDTO
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
    api_instance = visier.api.user_management.UserGroupManagmentV2Api(api_client)
    user_group_id = 'user_group_id_example' # str | The ID of user group to delete.
    delete_user_group_v2_request = visier.api.user_management.DeleteUserGroupV2Request() # DeleteUserGroupV2Request | 

    try:
        # Delete a user group
        api_response = api_instance.delete_user_group(user_group_id, delete_user_group_v2_request)
        print("The response of UserGroupManagmentV2Api->delete_user_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserGroupManagmentV2Api->delete_user_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_id** | **str**| The ID of user group to delete. | 
 **delete_user_group_v2_request** | [**DeleteUserGroupV2Request**](DeleteUserGroupV2Request.md)|  | 

### Return type

[**UserGroupSingleDeleteResponseDTO**](UserGroupSingleDeleteResponseDTO.md)

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

# **delete_user_groups**
> UserGroupDeleteResponseDTO delete_user_groups(user_groups_delete_request_dto)

Delete multiple user groups

This API allows you to delete user groups in bulk. To specify the tenant in which to delete user groups, administrating tenants can provide an analytic tenant code in the `TargetTenantID` request header.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.user_management
from visier.api.user_management.models.user_group_delete_response_dto import UserGroupDeleteResponseDTO
from visier.api.user_management.models.user_groups_delete_request_dto import UserGroupsDeleteRequestDTO
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
    api_instance = visier.api.user_management.UserGroupManagmentV2Api(api_client)
    user_groups_delete_request_dto = visier.api.user_management.UserGroupsDeleteRequestDTO() # UserGroupsDeleteRequestDTO | 

    try:
        # Delete multiple user groups
        api_response = api_instance.delete_user_groups(user_groups_delete_request_dto)
        print("The response of UserGroupManagmentV2Api->delete_user_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserGroupManagmentV2Api->delete_user_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_groups_delete_request_dto** | [**UserGroupsDeleteRequestDTO**](UserGroupsDeleteRequestDTO.md)|  | 

### Return type

[**UserGroupDeleteResponseDTO**](UserGroupDeleteResponseDTO.md)

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

# **get_user_group**
> UserGroupChangeDefinitionDTO get_user_group(user_group_id, var_with=var_with)

Retrieve the details of a user group

This API allows you to retrieve all available information about a specific user group.    <br>To specify the tenant in which to retrieve a user group, administrating tenants can provide an analytic tenant code in the `TargetTenantID` request header.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.user_management
from visier.api.user_management.models.user_group_change_definition_dto import UserGroupChangeDefinitionDTO
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
    api_instance = visier.api.user_management.UserGroupManagmentV2Api(api_client)
    user_group_id = 'user_group_id_example' # str | The ID of user group.
    var_with = 'var_with_example' # str | Controls the amount of detail to return in the response. Omit to return detailed information.  * **permissions**: Include the user group's permissions.  * **users**: Include the users in the user group.  * **details**: Include all available information. (optional)

    try:
        # Retrieve the details of a user group
        api_response = api_instance.get_user_group(user_group_id, var_with=var_with)
        print("The response of UserGroupManagmentV2Api->get_user_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserGroupManagmentV2Api->get_user_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_id** | **str**| The ID of user group. | 
 **var_with** | **str**| Controls the amount of detail to return in the response. Omit to return detailed information.  * **permissions**: Include the user group&#39;s permissions.  * **users**: Include the users in the user group.  * **details**: Include all available information. | [optional] 

### Return type

[**UserGroupChangeDefinitionDTO**](UserGroupChangeDefinitionDTO.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [OAuth2Auth](../README.md#OAuth2Auth), [OAuth2Auth](../README.md#OAuth2Auth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_groups**
> UserGroupsChangeDTO get_user_groups(var_with=var_with, limit=limit)

Retrieve a list of user groups

This API allows you to retrieve a collection of user groups. Use `with` to control the amount of detail returned in the response.  `with` supports these values:  * **permissions**: Include the user group's permissions.  * **users**: Include the users in the user group.  * **details**: Include all available information.   This API can return a maximum of 1000 user groups. The default number of user groups to return is 100.   <br>To specify the tenant in which to retrieve user groups, administrating tenants can provide an analytic tenant code in the `TargetTenantID` request header.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.user_management
from visier.api.user_management.models.user_groups_change_dto import UserGroupsChangeDTO
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
    api_instance = visier.api.user_management.UserGroupManagmentV2Api(api_client)
    var_with = 'var_with_example' # str | Controls the amount of detail to return in the response. Omit to return basic information.  * **permissions**: Include the user group's permissions.  * **users**: Include the users in the user group.  * **details**: Include all available information. (optional)
    limit = 56 # int | The number of results to return. The maximum number of user groups to retrieve is 1000. The default is 100. (optional)

    try:
        # Retrieve a list of user groups
        api_response = api_instance.get_user_groups(var_with=var_with, limit=limit)
        print("The response of UserGroupManagmentV2Api->get_user_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserGroupManagmentV2Api->get_user_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_with** | **str**| Controls the amount of detail to return in the response. Omit to return basic information.  * **permissions**: Include the user group&#39;s permissions.  * **users**: Include the users in the user group.  * **details**: Include all available information. | [optional] 
 **limit** | **int**| The number of results to return. The maximum number of user groups to retrieve is 1000. The default is 100. | [optional] 

### Return type

[**UserGroupsChangeDTO**](UserGroupsChangeDTO.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [OAuth2Auth](../README.md#OAuth2Auth), [OAuth2Auth](../README.md#OAuth2Auth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_user_groups**
> UserGroupChangeResponseDTO patch_user_groups(user_groups_change_dto)

Patch multiple user groups

This API allows you to make partial changes to user groups. To specify the tenant in which to patch a user group, administrating tenants can provide an analytic tenant code in the `TargetTenantID` request header or `tenantCode` for each user group in the request body.   Unlike `PUT`, which completely replaces the user group definition, use `PATCH` to change specific fields in the user group without affecting omitted fields.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.user_management
from visier.api.user_management.models.user_group_change_response_dto import UserGroupChangeResponseDTO
from visier.api.user_management.models.user_groups_change_dto import UserGroupsChangeDTO
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
    api_instance = visier.api.user_management.UserGroupManagmentV2Api(api_client)
    user_groups_change_dto = visier.api.user_management.UserGroupsChangeDTO() # UserGroupsChangeDTO | 

    try:
        # Patch multiple user groups
        api_response = api_instance.patch_user_groups(user_groups_change_dto)
        print("The response of UserGroupManagmentV2Api->patch_user_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserGroupManagmentV2Api->patch_user_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_groups_change_dto** | [**UserGroupsChangeDTO**](UserGroupsChangeDTO.md)|  | 

### Return type

[**UserGroupChangeResponseDTO**](UserGroupChangeResponseDTO.md)

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

# **put_user_groups**
> UserGroupChangeResponseDTO put_user_groups(user_groups_change_dto)

Update multiple user groups

This API allows you to update existing user groups. To specify the tenant in which to update a user group, administrating tenants can provide an analytic tenant code in the `TargetTenantID` request header or `tenantCode` for each user group in the request body.   When updating user groups, the user group definition in your API call replaces the prior definition. You must provide the entire definition in the `PUT` call. If you omit values from the update request, those values are removed from the user group. We recommend that you retrieve a user group's details before you update the user group with new values.    <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.user_management
from visier.api.user_management.models.user_group_change_response_dto import UserGroupChangeResponseDTO
from visier.api.user_management.models.user_groups_change_dto import UserGroupsChangeDTO
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
    api_instance = visier.api.user_management.UserGroupManagmentV2Api(api_client)
    user_groups_change_dto = visier.api.user_management.UserGroupsChangeDTO() # UserGroupsChangeDTO | 

    try:
        # Update multiple user groups
        api_response = api_instance.put_user_groups(user_groups_change_dto)
        print("The response of UserGroupManagmentV2Api->put_user_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserGroupManagmentV2Api->put_user_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_groups_change_dto** | [**UserGroupsChangeDTO**](UserGroupsChangeDTO.md)|  | 

### Return type

[**UserGroupChangeResponseDTO**](UserGroupChangeResponseDTO.md)

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

