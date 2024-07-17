# visier.api.consolidated_analytics.ConsolidatedAnalyticsV1AlphaApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_excluded_sources**](ConsolidatedAnalyticsV1AlphaApi.md#add_excluded_sources) | **PATCH** /v1alpha/admin/consolidated-analytics/tenants/{tenantId}/excluded-sources | Add excluded sources to a consolidated analytics tenant
[**add_source_tenants**](ConsolidatedAnalyticsV1AlphaApi.md#add_source_tenants) | **PATCH** /v1alpha/admin/consolidated-analytics/tenants/{tenantId}/source-tenants | Add source tenants to a consolidated analytics tenant
[**create_tenant**](ConsolidatedAnalyticsV1AlphaApi.md#create_tenant) | **POST** /v1alpha/admin/consolidated-analytics/tenants | Create a consolidated analytics tenant
[**list_excluded_sources**](ConsolidatedAnalyticsV1AlphaApi.md#list_excluded_sources) | **GET** /v1alpha/admin/consolidated-analytics/tenants/{tenantId}/excluded-sources | Retrieve a consolidated analytics tenant&#39;s excluded sources
[**list_source_tenants**](ConsolidatedAnalyticsV1AlphaApi.md#list_source_tenants) | **GET** /v1alpha/admin/consolidated-analytics/tenants/{tenantId}/source-tenants | Retrieve a consolidated analytics tenant&#39;s source tenants
[**list_tenants**](ConsolidatedAnalyticsV1AlphaApi.md#list_tenants) | **GET** /v1alpha/admin/consolidated-analytics/tenants | Retrieve a list of all consolidated analytics tenants
[**list_tenants_with_details**](ConsolidatedAnalyticsV1AlphaApi.md#list_tenants_with_details) | **GET** /v1alpha/admin/consolidated-analytics/tenants-with-details | Retrieve the details of all consolidated analytics tenants
[**remove_excluded_sources**](ConsolidatedAnalyticsV1AlphaApi.md#remove_excluded_sources) | **DELETE** /v1alpha/admin/consolidated-analytics/tenants/{tenantId}/excluded-sources | Remove excluded sources from a consolidated analytics tenants
[**remove_source_tenants**](ConsolidatedAnalyticsV1AlphaApi.md#remove_source_tenants) | **DELETE** /v1alpha/admin/consolidated-analytics/tenants/{tenantId}/source-tenants | Remove source tenants from a consolidated analytics tenants
[**set_excluded_sources**](ConsolidatedAnalyticsV1AlphaApi.md#set_excluded_sources) | **PUT** /v1alpha/admin/consolidated-analytics/tenants/{tenantId}/excluded-sources | Set a consolidated analytics tenant&#39;s excluded sources
[**set_source_tenants**](ConsolidatedAnalyticsV1AlphaApi.md#set_source_tenants) | **PUT** /v1alpha/admin/consolidated-analytics/tenants/{tenantId}/source-tenants | Set a consolidated analytics tenant&#39;s source tenants


# **add_excluded_sources**
> ConsolidatedAnalyticsAPIExcludedSourceListDTO add_excluded_sources(tenant_id, excluded_sources_body)

Add excluded sources to a consolidated analytics tenant

This API adds excluded sources to the list of excluded sources for a consolidated analytics tenant.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example


```python
import visier.api.consolidated_analytics
from visier.api.consolidated_analytics.models.consolidated_analytics_api_excluded_source_list_dto import ConsolidatedAnalyticsAPIExcludedSourceListDTO
from visier.api.consolidated_analytics.models.excluded_sources_body import ExcludedSourcesBody
from visier.api.consolidated_analytics.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.consolidated_analytics.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with visier.api.consolidated_analytics.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.consolidated_analytics.ConsolidatedAnalyticsV1AlphaApi(api_client)
    tenant_id = 'tenant_id_example' # str | The ID of the tenant. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}  is the consolidated analytic tenant code.
    excluded_sources_body = visier.api.consolidated_analytics.ExcludedSourcesBody() # ExcludedSourcesBody | 

    try:
        # Add excluded sources to a consolidated analytics tenant
        api_response = api_instance.add_excluded_sources(tenant_id, excluded_sources_body)
        print("The response of ConsolidatedAnalyticsV1AlphaApi->add_excluded_sources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsolidatedAnalyticsV1AlphaApi->add_excluded_sources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The ID of the tenant. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}  is the consolidated analytic tenant code. | 
 **excluded_sources_body** | [**ExcludedSourcesBody**](ExcludedSourcesBody.md)|  | 

### Return type

[**ConsolidatedAnalyticsAPIExcludedSourceListDTO**](ConsolidatedAnalyticsAPIExcludedSourceListDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_source_tenants**
> ConsolidatedAnalyticsAPISourceTenantListDTO add_source_tenants(tenant_id, tenant_code_body, limit=limit)

Add source tenants to a consolidated analytics tenant

This API adds source tenants to the list of source tenants for a consolidated analytics tenant.   If successful, the response returns an updated list of source tenants.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example


```python
import visier.api.consolidated_analytics
from visier.api.consolidated_analytics.models.consolidated_analytics_api_source_tenant_list_dto import ConsolidatedAnalyticsAPISourceTenantListDTO
from visier.api.consolidated_analytics.models.tenant_code_body import TenantCodeBody
from visier.api.consolidated_analytics.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.consolidated_analytics.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with visier.api.consolidated_analytics.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.consolidated_analytics.ConsolidatedAnalyticsV1AlphaApi(api_client)
    tenant_id = 'tenant_id_example' # str | The ID of the tenant. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}  is the consolidated analytic tenant code.
    tenant_code_body = visier.api.consolidated_analytics.TenantCodeBody() # TenantCodeBody | 
    limit = 56 # int | The maximum number of source tenants to return. The maximum value is 1000. Default is 400. (optional)

    try:
        # Add source tenants to a consolidated analytics tenant
        api_response = api_instance.add_source_tenants(tenant_id, tenant_code_body, limit=limit)
        print("The response of ConsolidatedAnalyticsV1AlphaApi->add_source_tenants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsolidatedAnalyticsV1AlphaApi->add_source_tenants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The ID of the tenant. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}  is the consolidated analytic tenant code. | 
 **tenant_code_body** | [**TenantCodeBody**](TenantCodeBody.md)|  | 
 **limit** | **int**| The maximum number of source tenants to return. The maximum value is 1000. Default is 400. | [optional] 

### Return type

[**ConsolidatedAnalyticsAPISourceTenantListDTO**](ConsolidatedAnalyticsAPISourceTenantListDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tenant**
> ConsolidatedAnalyticsAPITenantCreateRequestDTO create_tenant(consolidated_analytics_api_tenant_create_request_dto)

Create a consolidated analytics tenant

This API allows you to create a consolidated analytics tenant.   A new CA tenant has no source tenants and no excluded sources.   **Note:** CA tenant codes must have a prefix of CA. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}  is the consolidated analytic tenant code.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example


```python
import visier.api.consolidated_analytics
from visier.api.consolidated_analytics.models.consolidated_analytics_api_tenant_create_request_dto import ConsolidatedAnalyticsAPITenantCreateRequestDTO
from visier.api.consolidated_analytics.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.consolidated_analytics.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with visier.api.consolidated_analytics.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.consolidated_analytics.ConsolidatedAnalyticsV1AlphaApi(api_client)
    consolidated_analytics_api_tenant_create_request_dto = visier.api.consolidated_analytics.ConsolidatedAnalyticsAPITenantCreateRequestDTO() # ConsolidatedAnalyticsAPITenantCreateRequestDTO | 

    try:
        # Create a consolidated analytics tenant
        api_response = api_instance.create_tenant(consolidated_analytics_api_tenant_create_request_dto)
        print("The response of ConsolidatedAnalyticsV1AlphaApi->create_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsolidatedAnalyticsV1AlphaApi->create_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consolidated_analytics_api_tenant_create_request_dto** | [**ConsolidatedAnalyticsAPITenantCreateRequestDTO**](ConsolidatedAnalyticsAPITenantCreateRequestDTO.md)|  | 

### Return type

[**ConsolidatedAnalyticsAPITenantCreateRequestDTO**](ConsolidatedAnalyticsAPITenantCreateRequestDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_excluded_sources**
> ConsolidatedAnalyticsAPIExcludedSourceListDTO list_excluded_sources(tenant_id)

Retrieve a consolidated analytics tenant's excluded sources

This API allows you to retrieve a CA tenant's excluded sources.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example


```python
import visier.api.consolidated_analytics
from visier.api.consolidated_analytics.models.consolidated_analytics_api_excluded_source_list_dto import ConsolidatedAnalyticsAPIExcludedSourceListDTO
from visier.api.consolidated_analytics.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.consolidated_analytics.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with visier.api.consolidated_analytics.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.consolidated_analytics.ConsolidatedAnalyticsV1AlphaApi(api_client)
    tenant_id = 'tenant_id_example' # str | The ID of the tenant. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}  is the consolidated analytic tenant code.

    try:
        # Retrieve a consolidated analytics tenant's excluded sources
        api_response = api_instance.list_excluded_sources(tenant_id)
        print("The response of ConsolidatedAnalyticsV1AlphaApi->list_excluded_sources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsolidatedAnalyticsV1AlphaApi->list_excluded_sources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The ID of the tenant. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}  is the consolidated analytic tenant code. | 

### Return type

[**ConsolidatedAnalyticsAPIExcludedSourceListDTO**](ConsolidatedAnalyticsAPIExcludedSourceListDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_source_tenants**
> ConsolidatedAnalyticsAPISourceTenantListDTO list_source_tenants(tenant_id, limit=limit, start=start)

Retrieve a consolidated analytics tenant's source tenants

This API allows you to retrieve a CA tenant's source tenants.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example


```python
import visier.api.consolidated_analytics
from visier.api.consolidated_analytics.models.consolidated_analytics_api_source_tenant_list_dto import ConsolidatedAnalyticsAPISourceTenantListDTO
from visier.api.consolidated_analytics.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.consolidated_analytics.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with visier.api.consolidated_analytics.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.consolidated_analytics.ConsolidatedAnalyticsV1AlphaApi(api_client)
    tenant_id = 'tenant_id_example' # str | The ID of the tenant. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}  is the consolidated analytic tenant code.
    limit = 56 # int | The maximum number of source tenants to return. The maximum value is 1000. Default is 400. (optional)
    start = 56 # int | The starting index of the first source tenant to return. Default is 0. (optional)

    try:
        # Retrieve a consolidated analytics tenant's source tenants
        api_response = api_instance.list_source_tenants(tenant_id, limit=limit, start=start)
        print("The response of ConsolidatedAnalyticsV1AlphaApi->list_source_tenants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsolidatedAnalyticsV1AlphaApi->list_source_tenants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The ID of the tenant. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}  is the consolidated analytic tenant code. | 
 **limit** | **int**| The maximum number of source tenants to return. The maximum value is 1000. Default is 400. | [optional] 
 **start** | **int**| The starting index of the first source tenant to return. Default is 0. | [optional] 

### Return type

[**ConsolidatedAnalyticsAPISourceTenantListDTO**](ConsolidatedAnalyticsAPISourceTenantListDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tenants**
> ConsolidatedAnalyticsAPITenantListResponseDTO list_tenants(limit=limit, start=start)

Retrieve a list of all consolidated analytics tenants

This API allows you to retrieve the full list of consolidated analytics tenants in your administrating tenant.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example


```python
import visier.api.consolidated_analytics
from visier.api.consolidated_analytics.models.consolidated_analytics_api_tenant_list_response_dto import ConsolidatedAnalyticsAPITenantListResponseDTO
from visier.api.consolidated_analytics.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.consolidated_analytics.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with visier.api.consolidated_analytics.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.consolidated_analytics.ConsolidatedAnalyticsV1AlphaApi(api_client)
    limit = 56 # int | The maximum number of tenants to return. The maximum value is 1000. Default is 400. (optional)
    start = 56 # int | The starting index of the first tenant to return. Default is 0. (optional)

    try:
        # Retrieve a list of all consolidated analytics tenants
        api_response = api_instance.list_tenants(limit=limit, start=start)
        print("The response of ConsolidatedAnalyticsV1AlphaApi->list_tenants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsolidatedAnalyticsV1AlphaApi->list_tenants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of tenants to return. The maximum value is 1000. Default is 400. | [optional] 
 **start** | **int**| The starting index of the first tenant to return. Default is 0. | [optional] 

### Return type

[**ConsolidatedAnalyticsAPITenantListResponseDTO**](ConsolidatedAnalyticsAPITenantListResponseDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tenants_with_details**
> ConsolidatedAnalyticsAPITenantWithDetailsListResponseDTO list_tenants_with_details(limit=limit, start=start)

Retrieve the details of all consolidated analytics tenants

This API allows you to retrieve the full list of consolidated analytics tenants and their details in your administrating tenant.   **Note:** If your consolidated analytics tenants have thousands of source tenants, we recommend that you use the `GET /admin/consolidated-analytics/tenants` endpoint to get all CA tenants and then use the `GET /admin/consolidated-analytics/tenants/{tenantId}/source-tenants` and `GET /admin/consolidated-analytics/tenants/{tenantId}/excluded-sources` endpoints to retrieve information about specific CA tenants.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example


```python
import visier.api.consolidated_analytics
from visier.api.consolidated_analytics.models.consolidated_analytics_api_tenant_with_details_list_response_dto import ConsolidatedAnalyticsAPITenantWithDetailsListResponseDTO
from visier.api.consolidated_analytics.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.consolidated_analytics.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with visier.api.consolidated_analytics.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.consolidated_analytics.ConsolidatedAnalyticsV1AlphaApi(api_client)
    limit = 56 # int | The maximum number of tenants to return. The maximum value is 1000. Default is 400. (optional)
    start = 56 # int | The starting index of the first tenant to return. Default is 0. (optional)

    try:
        # Retrieve the details of all consolidated analytics tenants
        api_response = api_instance.list_tenants_with_details(limit=limit, start=start)
        print("The response of ConsolidatedAnalyticsV1AlphaApi->list_tenants_with_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsolidatedAnalyticsV1AlphaApi->list_tenants_with_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of tenants to return. The maximum value is 1000. Default is 400. | [optional] 
 **start** | **int**| The starting index of the first tenant to return. Default is 0. | [optional] 

### Return type

[**ConsolidatedAnalyticsAPITenantWithDetailsListResponseDTO**](ConsolidatedAnalyticsAPITenantWithDetailsListResponseDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_excluded_sources**
> ConsolidatedAnalyticsAPIExcludedSourceListDTO remove_excluded_sources(tenant_id, excluded_sources_body)

Remove excluded sources from a consolidated analytics tenants

This API removes excluded sources from the list of excluded sources for a consolidated analytics tenant.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example


```python
import visier.api.consolidated_analytics
from visier.api.consolidated_analytics.models.consolidated_analytics_api_excluded_source_list_dto import ConsolidatedAnalyticsAPIExcludedSourceListDTO
from visier.api.consolidated_analytics.models.excluded_sources_body import ExcludedSourcesBody
from visier.api.consolidated_analytics.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.consolidated_analytics.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with visier.api.consolidated_analytics.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.consolidated_analytics.ConsolidatedAnalyticsV1AlphaApi(api_client)
    tenant_id = 'tenant_id_example' # str | The ID of the tenant. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}  is the consolidated analytic tenant code.
    excluded_sources_body = visier.api.consolidated_analytics.ExcludedSourcesBody() # ExcludedSourcesBody | 

    try:
        # Remove excluded sources from a consolidated analytics tenants
        api_response = api_instance.remove_excluded_sources(tenant_id, excluded_sources_body)
        print("The response of ConsolidatedAnalyticsV1AlphaApi->remove_excluded_sources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsolidatedAnalyticsV1AlphaApi->remove_excluded_sources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The ID of the tenant. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}  is the consolidated analytic tenant code. | 
 **excluded_sources_body** | [**ExcludedSourcesBody**](ExcludedSourcesBody.md)|  | 

### Return type

[**ConsolidatedAnalyticsAPIExcludedSourceListDTO**](ConsolidatedAnalyticsAPIExcludedSourceListDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_source_tenants**
> ConsolidatedAnalyticsAPISourceTenantListDTO remove_source_tenants(tenant_id, tenant_code_body, limit=limit)

Remove source tenants from a consolidated analytics tenants

This API removes source tenants from the list of source tenants for a consolidated analytics tenant.   If successful, the response returns an updated list of source tenants.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example


```python
import visier.api.consolidated_analytics
from visier.api.consolidated_analytics.models.consolidated_analytics_api_source_tenant_list_dto import ConsolidatedAnalyticsAPISourceTenantListDTO
from visier.api.consolidated_analytics.models.tenant_code_body import TenantCodeBody
from visier.api.consolidated_analytics.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.consolidated_analytics.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with visier.api.consolidated_analytics.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.consolidated_analytics.ConsolidatedAnalyticsV1AlphaApi(api_client)
    tenant_id = 'tenant_id_example' # str | The ID of the tenant. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}  is the consolidated analytic tenant code.
    tenant_code_body = visier.api.consolidated_analytics.TenantCodeBody() # TenantCodeBody | 
    limit = 56 # int | The maximum number of source tenants to return. The maximum value is 1000. Default is 400. (optional)

    try:
        # Remove source tenants from a consolidated analytics tenants
        api_response = api_instance.remove_source_tenants(tenant_id, tenant_code_body, limit=limit)
        print("The response of ConsolidatedAnalyticsV1AlphaApi->remove_source_tenants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsolidatedAnalyticsV1AlphaApi->remove_source_tenants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The ID of the tenant. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}  is the consolidated analytic tenant code. | 
 **tenant_code_body** | [**TenantCodeBody**](TenantCodeBody.md)|  | 
 **limit** | **int**| The maximum number of source tenants to return. The maximum value is 1000. Default is 400. | [optional] 

### Return type

[**ConsolidatedAnalyticsAPISourceTenantListDTO**](ConsolidatedAnalyticsAPISourceTenantListDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_excluded_sources**
> ConsolidatedAnalyticsAPIExcludedSourceListDTO set_excluded_sources(tenant_id, excluded_sources_body)

Set a consolidated analytics tenant's excluded sources

This API defines the excluded sources for a consolidated analytics tenant.   After you create a CA tenant, you may optionally define a list of excluded sources. The excluded sources are the sources whose data is excluded from the CA tenant.  You can also use this API to replace the list of excluded sources for an existing CA tenant.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example


```python
import visier.api.consolidated_analytics
from visier.api.consolidated_analytics.models.consolidated_analytics_api_excluded_source_list_dto import ConsolidatedAnalyticsAPIExcludedSourceListDTO
from visier.api.consolidated_analytics.models.excluded_sources_body import ExcludedSourcesBody
from visier.api.consolidated_analytics.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.consolidated_analytics.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with visier.api.consolidated_analytics.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.consolidated_analytics.ConsolidatedAnalyticsV1AlphaApi(api_client)
    tenant_id = 'tenant_id_example' # str | The ID of the tenant. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}  is the consolidated analytic tenant code.
    excluded_sources_body = visier.api.consolidated_analytics.ExcludedSourcesBody() # ExcludedSourcesBody | 

    try:
        # Set a consolidated analytics tenant's excluded sources
        api_response = api_instance.set_excluded_sources(tenant_id, excluded_sources_body)
        print("The response of ConsolidatedAnalyticsV1AlphaApi->set_excluded_sources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsolidatedAnalyticsV1AlphaApi->set_excluded_sources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The ID of the tenant. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}  is the consolidated analytic tenant code. | 
 **excluded_sources_body** | [**ExcludedSourcesBody**](ExcludedSourcesBody.md)|  | 

### Return type

[**ConsolidatedAnalyticsAPIExcludedSourceListDTO**](ConsolidatedAnalyticsAPIExcludedSourceListDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_source_tenants**
> ConsolidatedAnalyticsAPISourceTenantListDTO set_source_tenants(tenant_id, tenant_code_body, limit=limit)

Set a consolidated analytics tenant's source tenants

This API defines the source tenants for a consolidated analytics tenant.   After you create a CA tenant, you must define a list of its source tenants. The source tenants are the tenants whose data is aggregated in the CA tenant.  You can also use this API to replace the list of source tenants for an existing CA tenant.   If successful, the response returns an updated list of source tenants.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example


```python
import visier.api.consolidated_analytics
from visier.api.consolidated_analytics.models.consolidated_analytics_api_source_tenant_list_dto import ConsolidatedAnalyticsAPISourceTenantListDTO
from visier.api.consolidated_analytics.models.tenant_code_body import TenantCodeBody
from visier.api.consolidated_analytics.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.consolidated_analytics.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with visier.api.consolidated_analytics.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.consolidated_analytics.ConsolidatedAnalyticsV1AlphaApi(api_client)
    tenant_id = 'tenant_id_example' # str | The ID of the tenant. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}  is the consolidated analytic tenant code.
    tenant_code_body = visier.api.consolidated_analytics.TenantCodeBody() # TenantCodeBody | 
    limit = 56 # int | The maximum number of source tenants to return. The maximum value is 1000. Default is 400. (optional)

    try:
        # Set a consolidated analytics tenant's source tenants
        api_response = api_instance.set_source_tenants(tenant_id, tenant_code_body, limit=limit)
        print("The response of ConsolidatedAnalyticsV1AlphaApi->set_source_tenants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsolidatedAnalyticsV1AlphaApi->set_source_tenants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The ID of the tenant. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}  is the consolidated analytic tenant code. | 
 **tenant_code_body** | [**TenantCodeBody**](TenantCodeBody.md)|  | 
 **limit** | **int**| The maximum number of source tenants to return. The maximum value is 1000. Default is 400. | [optional] 

### Return type

[**ConsolidatedAnalyticsAPISourceTenantListDTO**](ConsolidatedAnalyticsAPISourceTenantListDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

