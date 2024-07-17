# visier.api.object_configuration.ObjectConfigurationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_calculation_concept**](ObjectConfigurationApi.md#get_calculation_concept) | **GET** /v1/admin/calculation-concepts/{conceptId} | Retrieve the configuration of a calculation concept
[**get_calculation_concepts**](ObjectConfigurationApi.md#get_calculation_concepts) | **GET** /v1/admin/calculation-concepts | Retrieve all calculation concepts
[**get_selection_concept**](ObjectConfigurationApi.md#get_selection_concept) | **GET** /v1/admin/selection-concepts/{conceptId} | Retrieve the configuration of a selection concept
[**get_selection_concepts**](ObjectConfigurationApi.md#get_selection_concepts) | **GET** /v1/admin/selection-concepts | Retrieve all selection concepts
[**map_calculation_concept**](ObjectConfigurationApi.md#map_calculation_concept) | **PUT** /v1/admin/calculation-concepts/{conceptId}/configure | Map dimension members to nodes in a calculation concept
[**map_selection_concept**](ObjectConfigurationApi.md#map_selection_concept) | **PUT** /v1/admin/selection-concepts/{conceptId}/configure | Map dimension members to a selection concept


# **get_calculation_concept**
> CalculationConceptDTO get_calculation_concept(concept_id)

Retrieve the configuration of a calculation concept

This API allows you to retrieve the configuration details of a calculation concept in production.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.object_configuration
from visier.api.object_configuration.models.calculation_concept_dto import CalculationConceptDTO
from visier.api.object_configuration.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.object_configuration.Configuration(
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
configuration = visier.api.object_configuration.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.object_configuration.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.object_configuration.ObjectConfigurationApi(api_client)
    concept_id = 'concept_id_example' # str | The ID of the concept to retrieve the configuration for.

    try:
        # Retrieve the configuration of a calculation concept
        api_response = api_instance.get_calculation_concept(concept_id)
        print("The response of ObjectConfigurationApi->get_calculation_concept:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectConfigurationApi->get_calculation_concept: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **concept_id** | **str**| The ID of the concept to retrieve the configuration for. | 

### Return type

[**CalculationConceptDTO**](CalculationConceptDTO.md)

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

# **get_calculation_concepts**
> CalculationConceptListDTO get_calculation_concepts()

Retrieve all calculation concepts

This API allows you to retrieve the calculation concepts available in production.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.object_configuration
from visier.api.object_configuration.models.calculation_concept_list_dto import CalculationConceptListDTO
from visier.api.object_configuration.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.object_configuration.Configuration(
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
configuration = visier.api.object_configuration.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.object_configuration.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.object_configuration.ObjectConfigurationApi(api_client)

    try:
        # Retrieve all calculation concepts
        api_response = api_instance.get_calculation_concepts()
        print("The response of ObjectConfigurationApi->get_calculation_concepts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectConfigurationApi->get_calculation_concepts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CalculationConceptListDTO**](CalculationConceptListDTO.md)

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

# **get_selection_concept**
> SelectionConceptDTO get_selection_concept(concept_id)

Retrieve the configuration of a selection concept

This API allows you to retrieve the configuration details of a selection concept in production.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.object_configuration
from visier.api.object_configuration.models.selection_concept_dto import SelectionConceptDTO
from visier.api.object_configuration.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.object_configuration.Configuration(
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
configuration = visier.api.object_configuration.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.object_configuration.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.object_configuration.ObjectConfigurationApi(api_client)
    concept_id = 'concept_id_example' # str | The ID of the concept to retrieve the configuration for.

    try:
        # Retrieve the configuration of a selection concept
        api_response = api_instance.get_selection_concept(concept_id)
        print("The response of ObjectConfigurationApi->get_selection_concept:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectConfigurationApi->get_selection_concept: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **concept_id** | **str**| The ID of the concept to retrieve the configuration for. | 

### Return type

[**SelectionConceptDTO**](SelectionConceptDTO.md)

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

# **get_selection_concepts**
> SelectionConceptListDTO get_selection_concepts()

Retrieve all selection concepts

This API allows you to retrieve the selection concepts available in production.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.object_configuration
from visier.api.object_configuration.models.selection_concept_list_dto import SelectionConceptListDTO
from visier.api.object_configuration.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.object_configuration.Configuration(
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
configuration = visier.api.object_configuration.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.object_configuration.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.object_configuration.ObjectConfigurationApi(api_client)

    try:
        # Retrieve all selection concepts
        api_response = api_instance.get_selection_concepts()
        print("The response of ObjectConfigurationApi->get_selection_concepts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectConfigurationApi->get_selection_concepts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SelectionConceptListDTO**](SelectionConceptListDTO.md)

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

# **map_calculation_concept**
> ConceptConfigurationResultDTO map_calculation_concept(concept_id, calculation_concept_configuration_map_dto)

Map dimension members to nodes in a calculation concept

This API allows you to map dimension members to nodes in a calculation concept.  The changes are applied in a new project and published to production.   The body of this API is the source of truth for dimension members mapped to the concept. For example, if a node in  the body does not have any dimension members, all existing dimension members mapped to that node will be removed.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.object_configuration
from visier.api.object_configuration.models.calculation_concept_configuration_map_dto import CalculationConceptConfigurationMapDTO
from visier.api.object_configuration.models.concept_configuration_result_dto import ConceptConfigurationResultDTO
from visier.api.object_configuration.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.object_configuration.Configuration(
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
configuration = visier.api.object_configuration.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.object_configuration.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.object_configuration.ObjectConfigurationApi(api_client)
    concept_id = 'concept_id_example' # str | The UUID of the concept to configure.
    calculation_concept_configuration_map_dto = visier.api.object_configuration.CalculationConceptConfigurationMapDTO() # CalculationConceptConfigurationMapDTO | 

    try:
        # Map dimension members to nodes in a calculation concept
        api_response = api_instance.map_calculation_concept(concept_id, calculation_concept_configuration_map_dto)
        print("The response of ObjectConfigurationApi->map_calculation_concept:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectConfigurationApi->map_calculation_concept: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **concept_id** | **str**| The UUID of the concept to configure. | 
 **calculation_concept_configuration_map_dto** | [**CalculationConceptConfigurationMapDTO**](CalculationConceptConfigurationMapDTO.md)|  | 

### Return type

[**ConceptConfigurationResultDTO**](ConceptConfigurationResultDTO.md)

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

# **map_selection_concept**
> ConceptConfigurationResultDTO map_selection_concept(concept_id, selection_concept_configuration_map_dto)

Map dimension members to a selection concept

This API allows you to map dimension members to a selection concept.  The changes are applied to a new project and published to production.   The body of this API is the source of truth for dimension members mapped to the concept. For example, if a node in  the body does not have any dimension members, all existing dimension members mapped to that node will be removed.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.object_configuration
from visier.api.object_configuration.models.concept_configuration_result_dto import ConceptConfigurationResultDTO
from visier.api.object_configuration.models.selection_concept_configuration_map_dto import SelectionConceptConfigurationMapDTO
from visier.api.object_configuration.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.object_configuration.Configuration(
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
configuration = visier.api.object_configuration.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.object_configuration.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.object_configuration.ObjectConfigurationApi(api_client)
    concept_id = 'concept_id_example' # str | The UUID of the concept to configure.
    selection_concept_configuration_map_dto = visier.api.object_configuration.SelectionConceptConfigurationMapDTO() # SelectionConceptConfigurationMapDTO | 

    try:
        # Map dimension members to a selection concept
        api_response = api_instance.map_selection_concept(concept_id, selection_concept_configuration_map_dto)
        print("The response of ObjectConfigurationApi->map_selection_concept:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectConfigurationApi->map_selection_concept: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **concept_id** | **str**| The UUID of the concept to configure. | 
 **selection_concept_configuration_map_dto** | [**SelectionConceptConfigurationMapDTO**](SelectionConceptConfigurationMapDTO.md)|  | 

### Return type

[**ConceptConfigurationResultDTO**](ConceptConfigurationResultDTO.md)

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

