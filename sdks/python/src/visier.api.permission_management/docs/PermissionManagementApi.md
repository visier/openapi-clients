# visier.api.permission_management.PermissionManagementApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_data_access_sets**](PermissionManagementApi.md#create_data_access_sets) | **POST** /v1/admin/data-access-sets | Create shareable data access sets
[**create_permissions**](PermissionManagementApi.md#create_permissions) | **POST** /v1/admin/permissions | Create permissions
[**delete_permissions**](PermissionManagementApi.md#delete_permissions) | **DELETE** /v1/admin/permissions | Delete permissions
[**get_capabilities**](PermissionManagementApi.md#get_capabilities) | **GET** /v1/admin/capabilities | Retrieve a list of all permission capabilities
[**get_capability**](PermissionManagementApi.md#get_capability) | **GET** /v1/admin/capabilities/{capabilityId} | Retrieve a permission capability&#39;s details
[**get_content_package**](PermissionManagementApi.md#get_content_package) | **GET** /v1/admin/content-packages/{contentPackageId} | Retrieve a content package&#39;s details
[**get_content_packages**](PermissionManagementApi.md#get_content_packages) | **GET** /v1/admin/content-packages | Retrieve a list of all content packages
[**get_data_access_set**](PermissionManagementApi.md#get_data_access_set) | **GET** /v1/admin/data-access-sets/{dataAccessSetId} | Retrieve a data access set&#39;s details
[**get_data_access_sets**](PermissionManagementApi.md#get_data_access_sets) | **GET** /v1/admin/data-access-sets | Retrieve a list of all data access sets
[**get_data_security_objects**](PermissionManagementApi.md#get_data_security_objects) | **GET** /v1/admin/data-security-objects | Retrieve a list of data security objects
[**get_permission**](PermissionManagementApi.md#get_permission) | **GET** /v1/admin/permissions/{permissionId} | Retrieve a permission&#39;s details
[**get_permissions**](PermissionManagementApi.md#get_permissions) | **GET** /v1/admin/permissions | Retrieve a list of all permissions
[**update_permissions**](PermissionManagementApi.md#update_permissions) | **PUT** /v1/admin/permissions | Update permissions


# **create_data_access_sets**
> BulkDataAccessSetResponseDTO create_data_access_sets(create_data_access_set_request_dto)

Create shareable data access sets

This API allows you to create shareable data access sets. Shareable data access sets let you reuse common data access configurations in multiple permissions.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.permission_management
from visier.api.permission_management.models.bulk_data_access_set_response_dto import BulkDataAccessSetResponseDTO
from visier.api.permission_management.models.create_data_access_set_request_dto import CreateDataAccessSetRequestDTO
from visier.api.permission_management.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.permission_management.Configuration(
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
configuration = visier.api.permission_management.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.permission_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.permission_management.PermissionManagementApi(api_client)
    create_data_access_set_request_dto = visier.api.permission_management.CreateDataAccessSetRequestDTO() # CreateDataAccessSetRequestDTO | 

    try:
        # Create shareable data access sets
        api_response = api_instance.create_data_access_sets(create_data_access_set_request_dto)
        print("The response of PermissionManagementApi->create_data_access_sets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionManagementApi->create_data_access_sets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_data_access_set_request_dto** | [**CreateDataAccessSetRequestDTO**](CreateDataAccessSetRequestDTO.md)|  | 

### Return type

[**BulkDataAccessSetResponseDTO**](BulkDataAccessSetResponseDTO.md)

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

# **create_permissions**
> PermissionBulkOperationResponseDTO create_permissions(permissions_list_dto, tenant_code=tenant_code)

Create permissions

This API allows you to create new permissions. Administrating tenant users can specify the tenant in which to add these permissions.   To specify the project in which to create permissions, provide a project UUID in the `ProjectID` request header.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.permission_management
from visier.api.permission_management.models.permission_bulk_operation_response_dto import PermissionBulkOperationResponseDTO
from visier.api.permission_management.models.permissions_list_dto import PermissionsListDTO
from visier.api.permission_management.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.permission_management.Configuration(
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
configuration = visier.api.permission_management.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.permission_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.permission_management.PermissionManagementApi(api_client)
    permissions_list_dto = visier.api.permission_management.PermissionsListDTO() # PermissionsListDTO | 
    tenant_code = 'tenant_code_example' # str | Specify the tenant to create permissions in. (optional)

    try:
        # Create permissions
        api_response = api_instance.create_permissions(permissions_list_dto, tenant_code=tenant_code)
        print("The response of PermissionManagementApi->create_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionManagementApi->create_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permissions_list_dto** | [**PermissionsListDTO**](PermissionsListDTO.md)|  | 
 **tenant_code** | **str**| Specify the tenant to create permissions in. | [optional] 

### Return type

[**PermissionBulkOperationResponseDTO**](PermissionBulkOperationResponseDTO.md)

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

# **delete_permissions**
> PermissionBulkOperationResponseDTO delete_permissions(delete_permissions_request_dto, tenant_code=tenant_code)

Delete permissions

This API allows you to delete existing permissions.   To specify the project in which to delete permissions, provide a project UUID in the `ProjectID` request header.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.permission_management
from visier.api.permission_management.models.delete_permissions_request_dto import DeletePermissionsRequestDTO
from visier.api.permission_management.models.permission_bulk_operation_response_dto import PermissionBulkOperationResponseDTO
from visier.api.permission_management.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.permission_management.Configuration(
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
configuration = visier.api.permission_management.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.permission_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.permission_management.PermissionManagementApi(api_client)
    delete_permissions_request_dto = visier.api.permission_management.DeletePermissionsRequestDTO() # DeletePermissionsRequestDTO | 
    tenant_code = 'tenant_code_example' # str | Specify the tenant to delete permissions from. (optional)

    try:
        # Delete permissions
        api_response = api_instance.delete_permissions(delete_permissions_request_dto, tenant_code=tenant_code)
        print("The response of PermissionManagementApi->delete_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionManagementApi->delete_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_permissions_request_dto** | [**DeletePermissionsRequestDTO**](DeletePermissionsRequestDTO.md)|  | 
 **tenant_code** | **str**| Specify the tenant to delete permissions from. | [optional] 

### Return type

[**PermissionBulkOperationResponseDTO**](PermissionBulkOperationResponseDTO.md)

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

# **get_capabilities**
> GetCapabilitiesAPIResponseDTO get_capabilities(tenant_code=tenant_code)

Retrieve a list of all permission capabilities

This API allows you to retrieve all the permission capabilities in your tenant.  You can use the returned capabilities in other API calls when creating or updating permissions to assign the capability to the permission.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.permission_management
from visier.api.permission_management.models.get_capabilities_api_response_dto import GetCapabilitiesAPIResponseDTO
from visier.api.permission_management.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.permission_management.Configuration(
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
configuration = visier.api.permission_management.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.permission_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.permission_management.PermissionManagementApi(api_client)
    tenant_code = 'tenant_code_example' # str | Specify the tenant to retrieve the capabilities from. (optional)

    try:
        # Retrieve a list of all permission capabilities
        api_response = api_instance.get_capabilities(tenant_code=tenant_code)
        print("The response of PermissionManagementApi->get_capabilities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionManagementApi->get_capabilities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_code** | **str**| Specify the tenant to retrieve the capabilities from. | [optional] 

### Return type

[**GetCapabilitiesAPIResponseDTO**](GetCapabilitiesAPIResponseDTO.md)

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

# **get_capability**
> CapabilityDTO get_capability(capability_id, tenant_code=tenant_code)

Retrieve a permission capability's details

This API allows you to retrieve the details of a specific capability.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.permission_management
from visier.api.permission_management.models.capability_dto import CapabilityDTO
from visier.api.permission_management.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.permission_management.Configuration(
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
configuration = visier.api.permission_management.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.permission_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.permission_management.PermissionManagementApi(api_client)
    capability_id = 'capability_id_example' # str | The unique identifier of the capability you want to retrieve.
    tenant_code = 'tenant_code_example' # str | Specify the tenant to retrieve a capability from. (optional)

    try:
        # Retrieve a permission capability's details
        api_response = api_instance.get_capability(capability_id, tenant_code=tenant_code)
        print("The response of PermissionManagementApi->get_capability:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionManagementApi->get_capability: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **capability_id** | **str**| The unique identifier of the capability you want to retrieve. | 
 **tenant_code** | **str**| Specify the tenant to retrieve a capability from. | [optional] 

### Return type

[**CapabilityDTO**](CapabilityDTO.md)

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

# **get_content_package**
> ContentPackageDTO get_content_package(content_package_id, tenant_code=tenant_code)

Retrieve a content package's details

This API allows you to retrieve the details of a specific content package.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.permission_management
from visier.api.permission_management.models.content_package_dto import ContentPackageDTO
from visier.api.permission_management.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.permission_management.Configuration(
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
configuration = visier.api.permission_management.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.permission_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.permission_management.PermissionManagementApi(api_client)
    content_package_id = 'content_package_id_example' # str | The unique identifier of the content package you want to retrieve.
    tenant_code = 'tenant_code_example' # str | Specify the tenant to retrieve a content package from. (optional)

    try:
        # Retrieve a content package's details
        api_response = api_instance.get_content_package(content_package_id, tenant_code=tenant_code)
        print("The response of PermissionManagementApi->get_content_package:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionManagementApi->get_content_package: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_package_id** | **str**| The unique identifier of the content package you want to retrieve. | 
 **tenant_code** | **str**| Specify the tenant to retrieve a content package from. | [optional] 

### Return type

[**ContentPackageDTO**](ContentPackageDTO.md)

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

# **get_content_packages**
> GetContentPackagesAPIResponseDTO get_content_packages(tenant_code=tenant_code, search_string=search_string)

Retrieve a list of all content packages

This API allows you to retrieve the list of available content packages.  You can use the returned content packages in other API calls when creating or updating permissions to add the content package to the permission.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.permission_management
from visier.api.permission_management.models.get_content_packages_api_response_dto import GetContentPackagesAPIResponseDTO
from visier.api.permission_management.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.permission_management.Configuration(
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
configuration = visier.api.permission_management.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.permission_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.permission_management.PermissionManagementApi(api_client)
    tenant_code = 'tenant_code_example' # str | Specify the tenant to retrieve the content packages from. (optional)
    search_string = 'search_string_example' # str | Optional search string to return only content packages whose display name or description contains that search string.  If searchString is empty or not provided, the response returns a list of all content packages. (optional)

    try:
        # Retrieve a list of all content packages
        api_response = api_instance.get_content_packages(tenant_code=tenant_code, search_string=search_string)
        print("The response of PermissionManagementApi->get_content_packages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionManagementApi->get_content_packages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_code** | **str**| Specify the tenant to retrieve the content packages from. | [optional] 
 **search_string** | **str**| Optional search string to return only content packages whose display name or description contains that search string.  If searchString is empty or not provided, the response returns a list of all content packages. | [optional] 

### Return type

[**GetContentPackagesAPIResponseDTO**](GetContentPackagesAPIResponseDTO.md)

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

# **get_data_access_set**
> DataAccessSetDTO get_data_access_set(data_access_set_id)

Retrieve a data access set's details

This API allows you to retrieve the details of a specific shareable data access set. You must know the ID of the data access set to retrieve its details. To retrieve data access set IDs, see `GET v1/admin/data-access-sets`.   **Note:** This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.permission_management
from visier.api.permission_management.models.data_access_set_dto import DataAccessSetDTO
from visier.api.permission_management.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.permission_management.Configuration(
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
configuration = visier.api.permission_management.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.permission_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.permission_management.PermissionManagementApi(api_client)
    data_access_set_id = 'data_access_set_id_example' # str | The unique identifier of the data access set you want to retrieve.

    try:
        # Retrieve a data access set's details
        api_response = api_instance.get_data_access_set(data_access_set_id)
        print("The response of PermissionManagementApi->get_data_access_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionManagementApi->get_data_access_set: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_access_set_id** | **str**| The unique identifier of the data access set you want to retrieve. | 

### Return type

[**DataAccessSetDTO**](DataAccessSetDTO.md)

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

# **get_data_access_sets**
> GetDataAccessSetsAPIResponseDTO get_data_access_sets(analytic_object_id=analytic_object_id, var_with=var_with, limit=limit)

Retrieve a list of all data access sets

This API allows you to retrieve a list of all shareable data access sets. Data access sets define the level of access that users have to properties and property values for the analytic object in a permission. Data access sets also grant access to properties of subjects that are referenced by the analytic object in the permission.  You can assign data access sets to a permission when creating or updating permissions.   **Note:**   * If the number of valid data access sets exceeds the default limit of 100, the response status code is 206. To retrieve more than 100 data access sets, set `limit` to a higher number.  * This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.permission_management
from visier.api.permission_management.models.get_data_access_sets_api_response_dto import GetDataAccessSetsAPIResponseDTO
from visier.api.permission_management.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.permission_management.Configuration(
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
configuration = visier.api.permission_management.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.permission_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.permission_management.PermissionManagementApi(api_client)
    analytic_object_id = 'analytic_object_id_example' # str | Specify the analytic object ID to retrieve the shareable data access sets for. Default is all analytic objects. (optional)
    var_with = ['var_with_example'] # List[str] | The information about the data access set to include in the request response.  * If empty, returns basic information for the data access set, including its unique ID, display name, description, and analytic object ID.  * If `details`, returns basic information and property data access information (`propertyAccessConfigs`). (optional)
    limit = 56 # int | The maximum number of data access sets to return. Default is 100. Maximum is 1000. (optional)

    try:
        # Retrieve a list of all data access sets
        api_response = api_instance.get_data_access_sets(analytic_object_id=analytic_object_id, var_with=var_with, limit=limit)
        print("The response of PermissionManagementApi->get_data_access_sets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionManagementApi->get_data_access_sets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analytic_object_id** | **str**| Specify the analytic object ID to retrieve the shareable data access sets for. Default is all analytic objects. | [optional] 
 **var_with** | [**List[str]**](str.md)| The information about the data access set to include in the request response.  * If empty, returns basic information for the data access set, including its unique ID, display name, description, and analytic object ID.  * If &#x60;details&#x60;, returns basic information and property data access information (&#x60;propertyAccessConfigs&#x60;). | [optional] 
 **limit** | **int**| The maximum number of data access sets to return. Default is 100. Maximum is 1000. | [optional] 

### Return type

[**GetDataAccessSetsAPIResponseDTO**](GetDataAccessSetsAPIResponseDTO.md)

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

# **get_data_security_objects**
> GetDataSecurityObjectsAPIResponseDTO get_data_security_objects(id=id, include_details=include_details, tenant_code=tenant_code)

Retrieve a list of data security objects

This API allows you to retrieve the list of available data security objects.  Data security objects are analytic objects and their related objects that are available to define  permissions’ data security profiles.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.permission_management
from visier.api.permission_management.models.get_data_security_objects_api_response_dto import GetDataSecurityObjectsAPIResponseDTO
from visier.api.permission_management.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.permission_management.Configuration(
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
configuration = visier.api.permission_management.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.permission_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.permission_management.PermissionManagementApi(api_client)
    id = ['id_example'] # List[str] | The unique identifiers of the data security objects (analytic objects) to retrieve.  Default is all data security objects. (optional)
    include_details = True # bool | If `true`, the response includes the analytic objects (display name, ID, and object type), related objects,  securable properties, and securable dimensions. If `false`, the response only includes analytic objects  (display name, ID, and object type). Default is `false`. (optional)
    tenant_code = 'tenant_code_example' # str | Specify the tenant to retrieve data security objects from. (optional)

    try:
        # Retrieve a list of data security objects
        api_response = api_instance.get_data_security_objects(id=id, include_details=include_details, tenant_code=tenant_code)
        print("The response of PermissionManagementApi->get_data_security_objects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionManagementApi->get_data_security_objects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**List[str]**](str.md)| The unique identifiers of the data security objects (analytic objects) to retrieve.  Default is all data security objects. | [optional] 
 **include_details** | **bool**| If &#x60;true&#x60;, the response includes the analytic objects (display name, ID, and object type), related objects,  securable properties, and securable dimensions. If &#x60;false&#x60;, the response only includes analytic objects  (display name, ID, and object type). Default is &#x60;false&#x60;. | [optional] 
 **tenant_code** | **str**| Specify the tenant to retrieve data security objects from. | [optional] 

### Return type

[**GetDataSecurityObjectsAPIResponseDTO**](GetDataSecurityObjectsAPIResponseDTO.md)

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

# **get_permission**
> PermissionDTO get_permission(permission_id, tenant_code=tenant_code, include_details_with_status=include_details_with_status)

Retrieve a permission's details

This API allows you to retrieve the details for a specified permission.   To specify the project in which to retrieve the permission, provide a project UUID in the `ProjectID` request header.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.permission_management
from visier.api.permission_management.models.permission_dto import PermissionDTO
from visier.api.permission_management.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.permission_management.Configuration(
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
configuration = visier.api.permission_management.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.permission_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.permission_management.PermissionManagementApi(api_client)
    permission_id = 'permission_id_example' # str | The unique identifier of the permission you want to retrieve.
    tenant_code = 'tenant_code_example' # str | Specify the tenant to retrieve a permission from. (optional)
    include_details_with_status = 'include_details_with_status_example' # str | If `true`, returns the validity statuses for the permission's properties in data access sets and the  permission's dimensions, dimension members, and hierarchy properties in member filters. If `false`,  doesn't return validity status information. Default is `false`. (optional)

    try:
        # Retrieve a permission's details
        api_response = api_instance.get_permission(permission_id, tenant_code=tenant_code, include_details_with_status=include_details_with_status)
        print("The response of PermissionManagementApi->get_permission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionManagementApi->get_permission: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission_id** | **str**| The unique identifier of the permission you want to retrieve. | 
 **tenant_code** | **str**| Specify the tenant to retrieve a permission from. | [optional] 
 **include_details_with_status** | **str**| If &#x60;true&#x60;, returns the validity statuses for the permission&#39;s properties in data access sets and the  permission&#39;s dimensions, dimension members, and hierarchy properties in member filters. If &#x60;false&#x60;,  doesn&#39;t return validity status information. Default is &#x60;false&#x60;. | [optional] 

### Return type

[**PermissionDTO**](PermissionDTO.md)

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

# **get_permissions**
> GetPermissionsAPIResponseDTO get_permissions(tenant_code=tenant_code, include_details=include_details, include_details_with_status=include_details_with_status)

Retrieve a list of all permissions

This API allows you to retrieve the full list of user permissions in your tenant.   To specify the project in which to retrieve permissions, provide a project UUID in the `ProjectID` request header.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.permission_management
from visier.api.permission_management.models.get_permissions_api_response_dto import GetPermissionsAPIResponseDTO
from visier.api.permission_management.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.permission_management.Configuration(
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
configuration = visier.api.permission_management.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.permission_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.permission_management.PermissionManagementApi(api_client)
    tenant_code = 'tenant_code_example' # str | Specify the tenant to retrieve the permissions from. (optional)
    include_details = True # bool | If `true`, returns the permission's details. If `false`, only returns the permissions' ID, display name,  and description. Default is `false`. (optional)
    include_details_with_status = True # bool | If `true`, returns the validity statuses for the permission's properties in data access sets and the  permission's dimensions, dimension members, and hierarchy properties in member filters. If `false`,  doesn't return validity status information. Default is `false`. (optional)

    try:
        # Retrieve a list of all permissions
        api_response = api_instance.get_permissions(tenant_code=tenant_code, include_details=include_details, include_details_with_status=include_details_with_status)
        print("The response of PermissionManagementApi->get_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionManagementApi->get_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_code** | **str**| Specify the tenant to retrieve the permissions from. | [optional] 
 **include_details** | **bool**| If &#x60;true&#x60;, returns the permission&#39;s details. If &#x60;false&#x60;, only returns the permissions&#39; ID, display name,  and description. Default is &#x60;false&#x60;. | [optional] 
 **include_details_with_status** | **bool**| If &#x60;true&#x60;, returns the validity statuses for the permission&#39;s properties in data access sets and the  permission&#39;s dimensions, dimension members, and hierarchy properties in member filters. If &#x60;false&#x60;,  doesn&#39;t return validity status information. Default is &#x60;false&#x60;. | [optional] 

### Return type

[**GetPermissionsAPIResponseDTO**](GetPermissionsAPIResponseDTO.md)

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

# **update_permissions**
> PermissionBulkOperationResponseDTO update_permissions(permissions_list_dto, tenant_code=tenant_code)

Update permissions

This API allows you to update existing permissions.   To specify the project in which to update permissions, provide a project UUID in the `ProjectID` request header.   <br>**Note:** <em>This API is in **limited availability**. If you are interested in using it, please contact your Customer Success Manager (CSM).</em>

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.permission_management
from visier.api.permission_management.models.permission_bulk_operation_response_dto import PermissionBulkOperationResponseDTO
from visier.api.permission_management.models.permissions_list_dto import PermissionsListDTO
from visier.api.permission_management.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.permission_management.Configuration(
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
configuration = visier.api.permission_management.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.permission_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.permission_management.PermissionManagementApi(api_client)
    permissions_list_dto = visier.api.permission_management.PermissionsListDTO() # PermissionsListDTO | 
    tenant_code = 'tenant_code_example' # str | Specify the tenant to update permissions in. (optional)

    try:
        # Update permissions
        api_response = api_instance.update_permissions(permissions_list_dto, tenant_code=tenant_code)
        print("The response of PermissionManagementApi->update_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionManagementApi->update_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permissions_list_dto** | [**PermissionsListDTO**](PermissionsListDTO.md)|  | 
 **tenant_code** | **str**| Specify the tenant to update permissions in. | [optional] 

### Return type

[**PermissionBulkOperationResponseDTO**](PermissionBulkOperationResponseDTO.md)

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

