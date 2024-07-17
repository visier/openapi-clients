# visier.api.project_management.ProductionVersionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_production_versions**](ProductionVersionsApi.md#get_production_versions) | **GET** /v1alpha/admin/production-versions | Retrieve a list of all production versions
[**post_production_versions**](ProductionVersionsApi.md#post_production_versions) | **POST** /v1alpha/admin/production-versions | Perform an operation on production versions


# **get_production_versions**
> GetProductionVersionsAPIResponseDTO get_production_versions(limit=limit, start=start)

Retrieve a list of all production versions

*  This API allows you to retrieve a list of all projects that were published to production, ordered from latest published to earliest published.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example


```python
import visier.api.project_management
from visier.api.project_management.models.get_production_versions_api_response_dto import GetProductionVersionsAPIResponseDTO
from visier.api.project_management.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.project_management.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with visier.api.project_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.project_management.ProductionVersionsApi(api_client)
    limit = 56 # int | The maximum number of production versions to return. Default is 400. (optional)
    start = 56 # int | The starting index of the first production version to return. Default is 0. (optional)

    try:
        # Retrieve a list of all production versions
        api_response = api_instance.get_production_versions(limit=limit, start=start)
        print("The response of ProductionVersionsApi->get_production_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductionVersionsApi->get_production_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of production versions to return. Default is 400. | [optional] 
 **start** | **int**| The starting index of the first production version to return. Default is 0. | [optional] 

### Return type

[**GetProductionVersionsAPIResponseDTO**](GetProductionVersionsAPIResponseDTO.md)

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

# **post_production_versions**
> ProductionVersionsAPIOperationResponseDTO post_production_versions(production_versions_api_operation_request_dto)

Perform an operation on production versions

*  This API allows you to perform operations on production versions, such as exporting a production project's committed changes. If exporting, please specify `Accept: application/zip, application/json` in the header.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example


```python
import visier.api.project_management
from visier.api.project_management.models.production_versions_api_operation_request_dto import ProductionVersionsAPIOperationRequestDTO
from visier.api.project_management.models.production_versions_api_operation_response_dto import ProductionVersionsAPIOperationResponseDTO
from visier.api.project_management.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.project_management.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with visier.api.project_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.project_management.ProductionVersionsApi(api_client)
    production_versions_api_operation_request_dto = visier.api.project_management.ProductionVersionsAPIOperationRequestDTO() # ProductionVersionsAPIOperationRequestDTO | 

    try:
        # Perform an operation on production versions
        api_response = api_instance.post_production_versions(production_versions_api_operation_request_dto)
        print("The response of ProductionVersionsApi->post_production_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductionVersionsApi->post_production_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **production_versions_api_operation_request_dto** | [**ProductionVersionsAPIOperationRequestDTO**](ProductionVersionsAPIOperationRequestDTO.md)|  | 

### Return type

[**ProductionVersionsAPIOperationResponseDTO**](ProductionVersionsAPIOperationResponseDTO.md)

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

