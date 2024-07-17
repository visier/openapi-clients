# visier.api.tenant_management.TenantManagementApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tenant**](TenantManagementApi.md#create_tenant) | **POST** /v2/admin/tenants | Add an analytic tenant
[**list_tenants**](TenantManagementApi.md#list_tenants) | **GET** /v2/admin/tenants | Retrieve a list of all analytic tenants
[**tenant_info**](TenantManagementApi.md#tenant_info) | **GET** /v2/admin/tenants/{tenantId} | Retrieve an analytic tenant&#39;s details
[**update_tenant**](TenantManagementApi.md#update_tenant) | **PUT** /v2/admin/tenants/{tenantId} | Update an analytic tenant


# **create_tenant**
> TenantManagementAPIUpdateResponseDTO create_tenant(tenant_management_api_update_request_dto)

Add an analytic tenant

Prior to processing and loading an analytic tenant's data files, you must provision, or create, that tenant. A  provisioned analytic tenant is automatically enabled. If the tenant's data is loaded after provisioning, that data  is immediately accessible by their users.   This API allows you to create an analytic tenant and identify the  applications assigned to the tenant. Visier organizes content under a set of modules.   Contact Visier Support to determine the list of modules allocated to you.   **Note:** API requests that contain **homeAnalysisId**, **homeAnalysisByUserGroup**, **clickThroughLink**, or  **defaultCurrency** take longer to run because they require publishing a project to production.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.tenant_management
from visier.api.tenant_management.models.tenant_management_api_update_request_dto import TenantManagementAPIUpdateRequestDTO
from visier.api.tenant_management.models.tenant_management_api_update_response_dto import TenantManagementAPIUpdateResponseDTO
from visier.api.tenant_management.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.tenant_management.Configuration(
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
configuration = visier.api.tenant_management.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.tenant_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.tenant_management.TenantManagementApi(api_client)
    tenant_management_api_update_request_dto = visier.api.tenant_management.TenantManagementAPIUpdateRequestDTO() # TenantManagementAPIUpdateRequestDTO | 

    try:
        # Add an analytic tenant
        api_response = api_instance.create_tenant(tenant_management_api_update_request_dto)
        print("The response of TenantManagementApi->create_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantManagementApi->create_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_management_api_update_request_dto** | [**TenantManagementAPIUpdateRequestDTO**](TenantManagementAPIUpdateRequestDTO.md)|  | 

### Return type

[**TenantManagementAPIUpdateResponseDTO**](TenantManagementAPIUpdateResponseDTO.md)

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

# **list_tenants**
> TenantManagementAPIListResponseDTO list_tenants(mask_message, limit=limit, start=start)

Retrieve a list of all analytic tenants

Use this API to retrieve the full list of analytic tenants managed by you with their current states and the content  modules assigned to them, and all other relevant details for the tenants if requested.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.tenant_management
from visier.api.tenant_management.models.mask_message import MaskMessage
from visier.api.tenant_management.models.tenant_management_api_list_response_dto import TenantManagementAPIListResponseDTO
from visier.api.tenant_management.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.tenant_management.Configuration(
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
configuration = visier.api.tenant_management.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.tenant_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.tenant_management.TenantManagementApi(api_client)
    mask_message = visier.api.tenant_management.MaskMessage() # MaskMessage | 
    limit = 56 # int | The maximum number of tenants to return. Default is 400. (optional)
    start = 56 # int | The starting index of the first tenant to return. Default is 0. (optional)

    try:
        # Retrieve a list of all analytic tenants
        api_response = api_instance.list_tenants(mask_message, limit=limit, start=start)
        print("The response of TenantManagementApi->list_tenants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantManagementApi->list_tenants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mask_message** | [**MaskMessage**](MaskMessage.md)|  | 
 **limit** | **int**| The maximum number of tenants to return. Default is 400. | [optional] 
 **start** | **int**| The starting index of the first tenant to return. Default is 0. | [optional] 

### Return type

[**TenantManagementAPIListResponseDTO**](TenantManagementAPIListResponseDTO.md)

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

# **tenant_info**
> TenantManagementAPIGetResponseDTO tenant_info(tenant_id, mask_message)

Retrieve an analytic tenant's details

Use this API to retrieve the details for a specified analytic tenant. Doing so allows you to see the current state  of the tenant, the content modules assigned to it, and all other relevant details for the tenant.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.tenant_management
from visier.api.tenant_management.models.mask_message import MaskMessage
from visier.api.tenant_management.models.tenant_management_api_get_response_dto import TenantManagementAPIGetResponseDTO
from visier.api.tenant_management.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.tenant_management.Configuration(
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
configuration = visier.api.tenant_management.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.tenant_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.tenant_management.TenantManagementApi(api_client)
    tenant_id = 'tenant_id_example' # str | The ID of the tenant to retrieve.
    mask_message = visier.api.tenant_management.MaskMessage() # MaskMessage | 

    try:
        # Retrieve an analytic tenant's details
        api_response = api_instance.tenant_info(tenant_id, mask_message)
        print("The response of TenantManagementApi->tenant_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantManagementApi->tenant_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The ID of the tenant to retrieve. | 
 **mask_message** | [**MaskMessage**](MaskMessage.md)|  | 

### Return type

[**TenantManagementAPIGetResponseDTO**](TenantManagementAPIGetResponseDTO.md)

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

# **update_tenant**
> TenantManagementAPIUpdateResponseDTO update_tenant(tenant_id, tenant_management_api_update_request_dto)

Update an analytic tenant

You may need to update analytic tenants as they grow and as your organization upgrades the content available to them.  You may also encounter a scenario where an analytic tenant transitions across different industries. To make updates  to your tenants, use this API.   * To ensure that the analytic tenant receives accurate benchmarks and predictive functionality, update their industry code in the Visier system.  * To programmatically assign the Home analysis that analytic tenants see at login, use this API to set the default Home analysis for a tenant and specific user groups of that tenant.   You can use this API to update any field on an analytic tenant, except tenantCode.   **Note:** API requests that contain **homeAnalysisId**, **homeAnalysisByUserGroup**, **clickThroughLink**, or  **defaultCurrency** take longer to run because they require publishing a project to production.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.tenant_management
from visier.api.tenant_management.models.tenant_management_api_update_request_dto import TenantManagementAPIUpdateRequestDTO
from visier.api.tenant_management.models.tenant_management_api_update_response_dto import TenantManagementAPIUpdateResponseDTO
from visier.api.tenant_management.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.tenant_management.Configuration(
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
configuration = visier.api.tenant_management.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.tenant_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.tenant_management.TenantManagementApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    tenant_management_api_update_request_dto = visier.api.tenant_management.TenantManagementAPIUpdateRequestDTO() # TenantManagementAPIUpdateRequestDTO | 

    try:
        # Update an analytic tenant
        api_response = api_instance.update_tenant(tenant_id, tenant_management_api_update_request_dto)
        print("The response of TenantManagementApi->update_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantManagementApi->update_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_management_api_update_request_dto** | [**TenantManagementAPIUpdateRequestDTO**](TenantManagementAPIUpdateRequestDTO.md)|  | 

### Return type

[**TenantManagementAPIUpdateResponseDTO**](TenantManagementAPIUpdateResponseDTO.md)

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

