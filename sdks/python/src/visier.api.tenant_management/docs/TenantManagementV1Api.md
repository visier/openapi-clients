# visier.api.tenant_management.TenantManagementV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_tenant**](TenantManagementV1Api.md#add_tenant) | **POST** /v1/admin/tenants | Add an analytic tenant
[**delete_tenant**](TenantManagementV1Api.md#delete_tenant) | **DELETE** /v1/admin/tenants/{tenantId} | Deprovision an analytic tenant
[**disable_tenant**](TenantManagementV1Api.md#disable_tenant) | **PUT** /v1/admin/tenants/{tenantId}/disable | Disable an analytic tenant
[**enable_tenant**](TenantManagementV1Api.md#enable_tenant) | **PUT** /v1/admin/tenants/{tenantId}/enable | Enable an analytic tenant
[**get_tenant**](TenantManagementV1Api.md#get_tenant) | **GET** /v1/admin/tenants/{tenantId} | Retrieve an analytic tenant&#39;s details
[**get_tenants**](TenantManagementV1Api.md#get_tenants) | **GET** /v1/admin/tenants | Retrieve a list of all analytic tenants
[**update_tenant**](TenantManagementV1Api.md#update_tenant) | **PUT** /v1/admin/tenants/{tenantId} | Update an analytic tenant
[**validate_tenant**](TenantManagementV1Api.md#validate_tenant) | **GET** /v1/op/validation/tenants/{tenantId} | Validate an analytic tenant&#39;s metric values
[**validate_tenants**](TenantManagementV1Api.md#validate_tenants) | **GET** /v1/op/validation/tenants | Validate metric values for all analytic tenants


# **add_tenant**
> TenantProvisionAPIDTO add_tenant(tenant_provision_apidto)

Add an analytic tenant

Prior to processing and loading an analytic tenant's data files, you must provision, or create, that tenant.  A provisioned analytic tenant is automatically enabled. If the tenant's data is loaded after provisioning, that  data is immediately accessible by their users.   This API allows you to create an analytic tenant and identify the applications assigned to the tenant. Visier  organizes content under a set of modules.   Contact Visier Support to determine the list of modules allocated to you.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.tenant_management
from visier.api.tenant_management.models.tenant_provision_apidto import TenantProvisionAPIDTO
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
    api_instance = visier.api.tenant_management.TenantManagementV1Api(api_client)
    tenant_provision_apidto = visier.api.tenant_management.TenantProvisionAPIDTO() # TenantProvisionAPIDTO | 

    try:
        # Add an analytic tenant
        api_response = api_instance.add_tenant(tenant_provision_apidto)
        print("The response of TenantManagementV1Api->add_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantManagementV1Api->add_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_provision_apidto** | [**TenantProvisionAPIDTO**](TenantProvisionAPIDTO.md)|  | 

### Return type

[**TenantProvisionAPIDTO**](TenantProvisionAPIDTO.md)

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

# **delete_tenant**
> TenantStatusAPIDTO delete_tenant(tenant_id)

Deprovision an analytic tenant

Warning! Deprovisioning an analytic tenant is not reversible.  Before deprovisioning, you must disable an analytic tenant. For more information, see **`/v1/admin/tenants/{tenantId}/disable`**.   This API removes an analytic tenant permanently from the Visier system. If you are unsure whether an analytic tenant  may be re-enabled on any of the Visier modules at any time, you may instead want to disable the analytic tenant.   If successful, the response returns the status \"Deprovisioned\". This indicates that the tenant is scheduled for  deprovisioning, which may take several days to complete.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.tenant_management
from visier.api.tenant_management.models.tenant_status_apidto import TenantStatusAPIDTO
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
    api_instance = visier.api.tenant_management.TenantManagementV1Api(api_client)
    tenant_id = 'tenant_id_example' # str | The ID of the tenant. For example, WFF_{XXX}~{YYY} where {XXX} is the administrating tenant code and {YYY}  is the analytic tenant code.

    try:
        # Deprovision an analytic tenant
        api_response = api_instance.delete_tenant(tenant_id)
        print("The response of TenantManagementV1Api->delete_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantManagementV1Api->delete_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The ID of the tenant. For example, WFF_{XXX}~{YYY} where {XXX} is the administrating tenant code and {YYY}  is the analytic tenant code. | 

### Return type

[**TenantStatusAPIDTO**](TenantStatusAPIDTO.md)

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

# **disable_tenant**
> TenantStatusAPIDTO disable_tenant(tenant_id)

Disable an analytic tenant

Use this API to disable an analytic tenant and remove access to Visier visualizations for the tenant's users.   You must disable an analytic tenant before deprovisioning, or removing, it from the system.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.tenant_management
from visier.api.tenant_management.models.tenant_status_apidto import TenantStatusAPIDTO
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
    api_instance = visier.api.tenant_management.TenantManagementV1Api(api_client)
    tenant_id = 'tenant_id_example' # str | The ID of the tenant. For example, WFF_{XXX}~{YYY} where {XXX} is the administrating tenant code and {YYY}  is the analytic tenant code.

    try:
        # Disable an analytic tenant
        api_response = api_instance.disable_tenant(tenant_id)
        print("The response of TenantManagementV1Api->disable_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantManagementV1Api->disable_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The ID of the tenant. For example, WFF_{XXX}~{YYY} where {XXX} is the administrating tenant code and {YYY}  is the analytic tenant code. | 

### Return type

[**TenantStatusAPIDTO**](TenantStatusAPIDTO.md)

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

# **enable_tenant**
> TenantStatusAPIDTO enable_tenant(tenant_id)

Enable an analytic tenant

An analytic tenant is enabled when you provision or create the tenant.   Use this API to enable a tenant that you have specifically disabled; for example, if you previously did not  want that tenant to have access to Visier visualizations, but now do.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.tenant_management
from visier.api.tenant_management.models.tenant_status_apidto import TenantStatusAPIDTO
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
    api_instance = visier.api.tenant_management.TenantManagementV1Api(api_client)
    tenant_id = 'tenant_id_example' # str | The ID of the tenant. For example, WFF_{XXX}~{YYY} where {XXX} is the administrating tenant code and {YYY}  is the analytic tenant code.

    try:
        # Enable an analytic tenant
        api_response = api_instance.enable_tenant(tenant_id)
        print("The response of TenantManagementV1Api->enable_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantManagementV1Api->enable_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The ID of the tenant. For example, WFF_{XXX}~{YYY} where {XXX} is the administrating tenant code and {YYY}  is the analytic tenant code. | 

### Return type

[**TenantStatusAPIDTO**](TenantStatusAPIDTO.md)

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

# **get_tenant**
> TenantDetailAPIDTO get_tenant(tenant_id)

Retrieve an analytic tenant's details

Use this API to retrieve all details for a specified analytic tenant. Doing so allows you to see the current state  of the tenant, the content modules assigned to it, and all other relevant details for the tenant.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.tenant_management
from visier.api.tenant_management.models.tenant_detail_apidto import TenantDetailAPIDTO
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
    api_instance = visier.api.tenant_management.TenantManagementV1Api(api_client)
    tenant_id = 'tenant_id_example' # str | The ID of the tenant. For example, WFF_{XXX}~{YYY} where {XXX} is the administrating tenant code and {YYY}  is the analytic tenant code.

    try:
        # Retrieve an analytic tenant's details
        api_response = api_instance.get_tenant(tenant_id)
        print("The response of TenantManagementV1Api->get_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantManagementV1Api->get_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The ID of the tenant. For example, WFF_{XXX}~{YYY} where {XXX} is the administrating tenant code and {YYY}  is the analytic tenant code. | 

### Return type

[**TenantDetailAPIDTO**](TenantDetailAPIDTO.md)

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

# **get_tenants**
> AllTenantsStatusAPIDTO get_tenants(limit=limit, start=start, details=details)

Retrieve a list of all analytic tenants

Use this API to retrieve the full list of analytic tenants managed by you with their current states and the  content modules assigned to them, and all other relevant details for the tenants if requested.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.tenant_management
from visier.api.tenant_management.models.all_tenants_status_apidto import AllTenantsStatusAPIDTO
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
    api_instance = visier.api.tenant_management.TenantManagementV1Api(api_client)
    limit = 56 # int | The limit of analytic tenant details to retrieve. (optional)
    start = 56 # int | The index to start retrieving results from, also known as offset. The index begins at 0. (optional)
    details = True # bool | If true, the response returns information about the data version and modules. (optional)

    try:
        # Retrieve a list of all analytic tenants
        api_response = api_instance.get_tenants(limit=limit, start=start, details=details)
        print("The response of TenantManagementV1Api->get_tenants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantManagementV1Api->get_tenants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The limit of analytic tenant details to retrieve. | [optional] 
 **start** | **int**| The index to start retrieving results from, also known as offset. The index begins at 0. | [optional] 
 **details** | **bool**| If true, the response returns information about the data version and modules. | [optional] 

### Return type

[**AllTenantsStatusAPIDTO**](AllTenantsStatusAPIDTO.md)

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

# **update_tenant**
> TenantProvisionAPIDTO update_tenant(tenant_id, update_tenant_model)

Update an analytic tenant

You may need to update analytic tenants as they grow and as your organization upgrades the content available to  them. You may also encounter a scenario where an analytic tenant transitions across different industries.   To ensure that the analytic tenant receives accurate benchmarks and predictive functionality, update their  industry code in the Visier system.   You can use this API to update any field on an analytic tenant, except tenantCode.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.tenant_management
from visier.api.tenant_management.models.tenant_provision_apidto import TenantProvisionAPIDTO
from visier.api.tenant_management.models.update_tenant_model import UpdateTenantModel
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
    api_instance = visier.api.tenant_management.TenantManagementV1Api(api_client)
    tenant_id = 'tenant_id_example' # str | The ID of the tenant to update.
    update_tenant_model = visier.api.tenant_management.UpdateTenantModel() # UpdateTenantModel | 

    try:
        # Update an analytic tenant
        api_response = api_instance.update_tenant(tenant_id, update_tenant_model)
        print("The response of TenantManagementV1Api->update_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantManagementV1Api->update_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The ID of the tenant to update. | 
 **update_tenant_model** | [**UpdateTenantModel**](UpdateTenantModel.md)|  | 

### Return type

[**TenantProvisionAPIDTO**](TenantProvisionAPIDTO.md)

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

# **validate_tenant**
> TenantPreviewEntriesSummaryDTO validate_tenant(tenant_id)

Validate an analytic tenant's metric values

Use this API to retrieve the metric values for an individual analytic tenant. The metric values included in the  response are the tenant's configured summary metrics. Administrators can configure summary metrics in a project:  - Sign in to Visier as an administrator.  - In a project, on the navigation bar, click the Home button.  - Click Dashboard, and then click Edit Summary Metrics.  - Select the metrics that you want to validate, and then close the Summary Metrics dialog.  - Publish the project to production.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.tenant_management
from visier.api.tenant_management.models.tenant_preview_entries_summary_dto import TenantPreviewEntriesSummaryDTO
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
    api_instance = visier.api.tenant_management.TenantManagementV1Api(api_client)
    tenant_id = 'tenant_id_example' # str | The ID of the tenant. For example, WFF_{XXX}~{YYY} where {XXX} is the administrating tenant code and {YYY}  is the analytic tenant code.

    try:
        # Validate an analytic tenant's metric values
        api_response = api_instance.validate_tenant(tenant_id)
        print("The response of TenantManagementV1Api->validate_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantManagementV1Api->validate_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The ID of the tenant. For example, WFF_{XXX}~{YYY} where {XXX} is the administrating tenant code and {YYY}  is the analytic tenant code. | 

### Return type

[**TenantPreviewEntriesSummaryDTO**](TenantPreviewEntriesSummaryDTO.md)

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

# **validate_tenants**
> TenantPreviewEntriesSummaryListDTO validate_tenants(limit=limit, start=start)

Validate metric values for all analytic tenants

As you onboard more analytic tenants, you can validate the data visible to your users to ensure it matches the  source systems from which it was exported and that it matches what your expectations are for this data.   The metric values included in the response are the tenant's configured summary metrics. Administrators can  configure summary metrics in a project:  - Sign in to Visier as an administrator.  - In a project, on the navigation bar, click the Home button.  - Click Dashboard, and then click Edit Summary Metrics.  - Select the metrics that you want to validate, and then close the Summary Metrics dialog.  - Publish the project to production.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.tenant_management
from visier.api.tenant_management.models.tenant_preview_entries_summary_list_dto import TenantPreviewEntriesSummaryListDTO
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
    api_instance = visier.api.tenant_management.TenantManagementV1Api(api_client)
    limit = 56 # int | The limit of analytic tenant details to retrieve. (optional)
    start = 56 # int | The index to start retrieving results from, also known as offset. The index begins at 0. (optional)

    try:
        # Validate metric values for all analytic tenants
        api_response = api_instance.validate_tenants(limit=limit, start=start)
        print("The response of TenantManagementV1Api->validate_tenants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantManagementV1Api->validate_tenants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The limit of analytic tenant details to retrieve. | [optional] 
 **start** | **int**| The index to start retrieving results from, also known as offset. The index begins at 0. | [optional] 

### Return type

[**TenantPreviewEntriesSummaryListDTO**](TenantPreviewEntriesSummaryListDTO.md)

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

