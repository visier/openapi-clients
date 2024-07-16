# visier.model_query_apis.DataModelApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analytic_metrics**](DataModelApi.md#analytic_metrics) | **GET** /v1/data/model/analytic-objects/{id}/metrics | Retrieve a list of metrics for an analytic object by ID
[**analytic_object**](DataModelApi.md#analytic_object) | **GET** /v1/data/model/analytic-objects/{id} | Retrieve an analytic object by ID
[**analytic_objects**](DataModelApi.md#analytic_objects) | **GET** /v1/data/model/analytic-objects | Retrieve a list of analytic objects
[**call_property**](DataModelApi.md#call_property) | **GET** /v1/data/model/analytic-objects/{objectId}/properties/{id} | Retrieve a property by ID
[**currencies**](DataModelApi.md#currencies) | **GET** /v1/data/model/currencies | Retrieve all currencies
[**currency**](DataModelApi.md#currency) | **GET** /v1/data/model/currencies/{id} | Retrieve a currency
[**currency_rates**](DataModelApi.md#currency_rates) | **GET** /v1/data/model/currencies/{id}/rates | Retrieve all exchange rates for a currency
[**currency_rates_with_to_currency**](DataModelApi.md#currency_rates_with_to_currency) | **GET** /v1/data/model/currencies/{id}/rates/{toId} | Retrieve exchange rates from one currency to another currency
[**dimension**](DataModelApi.md#dimension) | **GET** /v1/data/model/analytic-objects/{objectId}/dimensions/{id} | Retrieve a dimension by ID
[**dimension_member_map_validation**](DataModelApi.md#dimension_member_map_validation) | **POST** /v1/data/model/analytic-objects/{objectId}/dimensions/{dimensionId}/mappings/validate | Validate a member map&#39;s unmapped dimension members by ID
[**dimensions**](DataModelApi.md#dimensions) | **GET** /v1/data/model/analytic-objects/{objectId}/dimensions | Retrieve a list of dimensions
[**member**](DataModelApi.md#member) | **GET** /v1/data/model/analytic-objects/{objectId}/dimensions/{dimensionId}/members/{id} | Retrieve a dimension member
[**members**](DataModelApi.md#members) | **GET** /v1/data/model/analytic-objects/{objectId}/dimensions/{dimensionId}/members | Retrieve a list of dimension members
[**metric**](DataModelApi.md#metric) | **GET** /v1/data/model/metrics/{id} | Retrieve a metric by ID
[**metric_dimensions**](DataModelApi.md#metric_dimensions) | **GET** /v1/data/model/metrics/{metricId}/dimensions | Retrieve a metric&#39;s dimensions
[**metric_selection_concepts**](DataModelApi.md#metric_selection_concepts) | **GET** /v1/data/model/metrics/{metricId}/selection-concepts | Retrieve a metric&#39;s selection concepts
[**metrics**](DataModelApi.md#metrics) | **GET** /v1/data/model/metrics | Retrieve a list of metrics
[**planning_metrics**](DataModelApi.md#planning_metrics) | **GET** /v1/data/model/plan-models/{id}/metrics | Retrieve metrics by planning model ID
[**planning_model**](DataModelApi.md#planning_model) | **GET** /v1/data/model/plan-models/{id} | Retrieve a planning model by ID
[**planning_models**](DataModelApi.md#planning_models) | **GET** /v1/data/model/plan-models | Retrieve a list of planning models
[**planning_plan**](DataModelApi.md#planning_plan) | **GET** /v1/data/model/plan-models/{modelId}/plans/{id} | Retrieve a plan by ID
[**planning_plans**](DataModelApi.md#planning_plans) | **GET** /v1/data/model/plan-models/{modelId}/plans | Retrieve a list of plans
[**prediction**](DataModelApi.md#prediction) | **GET** /v1/data/model/predictions/{id} | Retrieve a prediction by ID
[**predictions**](DataModelApi.md#predictions) | **GET** /v1/data/model/predictions | Retrieve a list of predictions
[**properties**](DataModelApi.md#properties) | **GET** /v1/data/model/analytic-objects/{objectId}/properties | Retrieve a list of properties
[**selection_concept**](DataModelApi.md#selection_concept) | **GET** /v1/data/model/analytic-objects/{objectId}/selection-concepts/{id} | Retrieve an analytic object&#39;s selection concept by ID
[**selection_concepts**](DataModelApi.md#selection_concepts) | **GET** /v1/data/model/analytic-objects/{objectId}/selection-concepts | Retrieve an analytic object&#39;s selection concepts


# **analytic_metrics**
> MetricsDTO analytic_metrics(id)

Retrieve a list of metrics for an analytic object by ID

If you know the ID of an analytic object, use this API to retrieve metrics for that object specifically.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query_apis
from visier.model_query_apis.models.metrics_dto import MetricsDTO
from visier.model_query_apis.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query_apis.Configuration(
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
configuration = visier.model_query_apis.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query_apis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query_apis.DataModelApi(api_client)
    id = 'id_example' # str | The ID of the analytic object to retrieve metrics for.

    try:
        # Retrieve a list of metrics for an analytic object by ID
        api_response = api_instance.analytic_metrics(id)
        print("The response of DataModelApi->analytic_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->analytic_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the analytic object to retrieve metrics for. | 

### Return type

[**MetricsDTO**](MetricsDTO.md)

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

# **analytic_object**
> AnalyticObjectDTO analytic_object(id)

Retrieve an analytic object by ID

If you know the ID of an analytic object, use this API to retrieve that object specifically.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query_apis
from visier.model_query_apis.models.analytic_object_dto import AnalyticObjectDTO
from visier.model_query_apis.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query_apis.Configuration(
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
configuration = visier.model_query_apis.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query_apis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query_apis.DataModelApi(api_client)
    id = 'id_example' # str | The ID of the analytic object to retrieve.

    try:
        # Retrieve an analytic object by ID
        api_response = api_instance.analytic_object(id)
        print("The response of DataModelApi->analytic_object:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->analytic_object: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the analytic object to retrieve. | 

### Return type

[**AnalyticObjectDTO**](AnalyticObjectDTO.md)

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

# **analytic_objects**
> AnalyticObjectsDTO analytic_objects(id=id, object_type=object_type)

Retrieve a list of analytic objects

Use this API to retrieve all the analytic objects in your Visier solution.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query_apis
from visier.model_query_apis.models.analytic_objects_dto import AnalyticObjectsDTO
from visier.model_query_apis.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query_apis.Configuration(
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
configuration = visier.model_query_apis.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query_apis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query_apis.DataModelApi(api_client)
    id = ['id_example'] # List[str] | The IDs of the analytic objects to retrieve. Default is all analytic objects. (optional)
    object_type = 'object_type_example' # str | The object type to filter the returned analytic objects by. (optional)

    try:
        # Retrieve a list of analytic objects
        api_response = api_instance.analytic_objects(id=id, object_type=object_type)
        print("The response of DataModelApi->analytic_objects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->analytic_objects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**List[str]**](str.md)| The IDs of the analytic objects to retrieve. Default is all analytic objects. | [optional] 
 **object_type** | **str**| The object type to filter the returned analytic objects by. | [optional] 

### Return type

[**AnalyticObjectsDTO**](AnalyticObjectsDTO.md)

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

# **call_property**
> PropertyDTO call_property(object_id, id)

Retrieve a property by ID

If you know the ID of a property, use this API to retrieve that property specifically. You must also know the analytic object's ID..

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query_apis
from visier.model_query_apis.models.property_dto import PropertyDTO
from visier.model_query_apis.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query_apis.Configuration(
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
configuration = visier.model_query_apis.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query_apis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query_apis.DataModelApi(api_client)
    object_id = 'object_id_example' # str | The ID of the analytic object to retrieve.
    id = ['id_example'] # List[str] | The ID of the property to retrieve.

    try:
        # Retrieve a property by ID
        api_response = api_instance.call_property(object_id, id)
        print("The response of DataModelApi->call_property:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->call_property: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| The ID of the analytic object to retrieve. | 
 **id** | [**List[str]**](str.md)| The ID of the property to retrieve. | 

### Return type

[**PropertyDTO**](PropertyDTO.md)

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

# **currencies**
> CurrenciesDTO currencies()

Retrieve all currencies

Use this API to retrieve all the available currencies in your Visier solution.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query_apis
from visier.model_query_apis.models.currencies_dto import CurrenciesDTO
from visier.model_query_apis.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query_apis.Configuration(
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
configuration = visier.model_query_apis.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query_apis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query_apis.DataModelApi(api_client)

    try:
        # Retrieve all currencies
        api_response = api_instance.currencies()
        print("The response of DataModelApi->currencies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->currencies: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CurrenciesDTO**](CurrenciesDTO.md)

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

# **currency**
> CurrencyDTO currency(id)

Retrieve a currency

Use this API to retrieve a specific currency if you know the currency code.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query_apis
from visier.model_query_apis.models.currency_dto import CurrencyDTO
from visier.model_query_apis.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query_apis.Configuration(
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
configuration = visier.model_query_apis.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query_apis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query_apis.DataModelApi(api_client)
    id = 'id_example' # str | The ISO 4217 3-letter code for the currency.

    try:
        # Retrieve a currency
        api_response = api_instance.currency(id)
        print("The response of DataModelApi->currency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->currency: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ISO 4217 3-letter code for the currency. | 

### Return type

[**CurrencyDTO**](CurrencyDTO.md)

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

# **currency_rates**
> CurrencyRatesDTO currency_rates(id, start_time=start_time, end_time=end_time, decimals=decimals)

Retrieve all exchange rates for a currency

Use this API to retrieve exchange rates for a specific currency from Visier.  You can optionally specify query parameter options for the returned rates, such as the number of decimals to round the exchange rate to.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query_apis
from visier.model_query_apis.models.currency_rates_dto import CurrencyRatesDTO
from visier.model_query_apis.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query_apis.Configuration(
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
configuration = visier.model_query_apis.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query_apis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query_apis.DataModelApi(api_client)
    id = 'id_example' # str | The ISO 4217 3-letter code for the currency to get rates for.
    start_time = 'start_time_example' # str | The earliest time instant to retrieve exchange rates from. Default is to use 0 milliseconds. (optional)
    end_time = 'end_time_example' # str | The latest time instant to retrieve exchange rates from. Default is to use the time of this request in milliseconds. (optional)
    decimals = 'decimals_example' # str | The number of decimals to round exchange rates to. Default is to round to 2 decimal places. (optional)

    try:
        # Retrieve all exchange rates for a currency
        api_response = api_instance.currency_rates(id, start_time=start_time, end_time=end_time, decimals=decimals)
        print("The response of DataModelApi->currency_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->currency_rates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ISO 4217 3-letter code for the currency to get rates for. | 
 **start_time** | **str**| The earliest time instant to retrieve exchange rates from. Default is to use 0 milliseconds. | [optional] 
 **end_time** | **str**| The latest time instant to retrieve exchange rates from. Default is to use the time of this request in milliseconds. | [optional] 
 **decimals** | **str**| The number of decimals to round exchange rates to. Default is to round to 2 decimal places. | [optional] 

### Return type

[**CurrencyRatesDTO**](CurrencyRatesDTO.md)

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

# **currency_rates_with_to_currency**
> CurrencyRatesDTO currency_rates_with_to_currency(id, to_id, start_time=start_time, end_time=end_time, decimals=decimals)

Retrieve exchange rates from one currency to another currency

Use this API to retrieve exchange rates from a specific currency to another specific currency.  You can optionally specify query parameter options for the returned rates, such as the number of decimals to round the exchange rate to.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query_apis
from visier.model_query_apis.models.currency_rates_dto import CurrencyRatesDTO
from visier.model_query_apis.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query_apis.Configuration(
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
configuration = visier.model_query_apis.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query_apis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query_apis.DataModelApi(api_client)
    id = 'id_example' # str | The ISO 4217 3-letter code for the currency to convert from.
    to_id = 'to_id_example' # str | The ISO 4217 3-letter code for the currency to convert to.
    start_time = 'start_time_example' # str | The earliest time instant to retrieve exchange rates from. Default is to use 0 milliseconds. (optional)
    end_time = 'end_time_example' # str | The latest time instant to retrieve exchange rates from. Default is to use the time of this request in milliseconds. (optional)
    decimals = 'decimals_example' # str | The number of decimals to round exchange rates to. Default is to round to 2 decimal places. (optional)

    try:
        # Retrieve exchange rates from one currency to another currency
        api_response = api_instance.currency_rates_with_to_currency(id, to_id, start_time=start_time, end_time=end_time, decimals=decimals)
        print("The response of DataModelApi->currency_rates_with_to_currency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->currency_rates_with_to_currency: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ISO 4217 3-letter code for the currency to convert from. | 
 **to_id** | **str**| The ISO 4217 3-letter code for the currency to convert to. | 
 **start_time** | **str**| The earliest time instant to retrieve exchange rates from. Default is to use 0 milliseconds. | [optional] 
 **end_time** | **str**| The latest time instant to retrieve exchange rates from. Default is to use the time of this request in milliseconds. | [optional] 
 **decimals** | **str**| The number of decimals to round exchange rates to. Default is to round to 2 decimal places. | [optional] 

### Return type

[**CurrencyRatesDTO**](CurrencyRatesDTO.md)

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

# **dimension**
> DimensionDTO dimension(object_id, id)

Retrieve a dimension by ID

If you know the ID of a dimension, use this API to retrieve that dimension specifically. You must also know the analytic object's ID.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query_apis
from visier.model_query_apis.models.dimension_dto import DimensionDTO
from visier.model_query_apis.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query_apis.Configuration(
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
configuration = visier.model_query_apis.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query_apis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query_apis.DataModelApi(api_client)
    object_id = 'object_id_example' # str | The ID of the analytic object to retrieve.
    id = 'id_example' # str | The ID of the dimension to retrieve.

    try:
        # Retrieve a dimension by ID
        api_response = api_instance.dimension(object_id, id)
        print("The response of DataModelApi->dimension:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->dimension: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| The ID of the analytic object to retrieve. | 
 **id** | **str**| The ID of the dimension to retrieve. | 

### Return type

[**DimensionDTO**](DimensionDTO.md)

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

# **dimension_member_map_validation**
> DimensionMappingValidationDTO dimension_member_map_validation(object_id, dimension_id, dimension_mapping_validation_execution_dto)

Validate a member map's unmapped dimension members by ID

If you know the ID of a member map, use this API to validate one of the member map's dimensions.   You must also know the dimension's ID and the analytic object's ID.   The response returns the member map ID, the requested dimension ID, a list of the dimension's unmapped members, and a list of errors found.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query_apis
from visier.model_query_apis.models.dimension_mapping_validation_dto import DimensionMappingValidationDTO
from visier.model_query_apis.models.dimension_mapping_validation_execution_dto import DimensionMappingValidationExecutionDTO
from visier.model_query_apis.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query_apis.Configuration(
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
configuration = visier.model_query_apis.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query_apis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query_apis.DataModelApi(api_client)
    object_id = 'object_id_example' # str | The ID of the analytic object.
    dimension_id = 'dimension_id_example' # str | The ID of a dimension of the member map.
    dimension_mapping_validation_execution_dto = visier.model_query_apis.DimensionMappingValidationExecutionDTO() # DimensionMappingValidationExecutionDTO | 

    try:
        # Validate a member map's unmapped dimension members by ID
        api_response = api_instance.dimension_member_map_validation(object_id, dimension_id, dimension_mapping_validation_execution_dto)
        print("The response of DataModelApi->dimension_member_map_validation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->dimension_member_map_validation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| The ID of the analytic object. | 
 **dimension_id** | **str**| The ID of a dimension of the member map. | 
 **dimension_mapping_validation_execution_dto** | [**DimensionMappingValidationExecutionDTO**](DimensionMappingValidationExecutionDTO.md)|  | 

### Return type

[**DimensionMappingValidationDTO**](DimensionMappingValidationDTO.md)

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

# **dimensions**
> DimensionsDTO dimensions(object_id, id=id)

Retrieve a list of dimensions

Use this API to retrieve a list of dimensions for a specific analytic object.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query_apis
from visier.model_query_apis.models.dimensions_dto import DimensionsDTO
from visier.model_query_apis.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query_apis.Configuration(
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
configuration = visier.model_query_apis.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query_apis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query_apis.DataModelApi(api_client)
    object_id = 'object_id_example' # str | The ID of the analytic object to retrieve.
    id = ['id_example'] # List[str] | The IDs of the dimensions to retrieve. Default is all dimensions. (optional)

    try:
        # Retrieve a list of dimensions
        api_response = api_instance.dimensions(object_id, id=id)
        print("The response of DataModelApi->dimensions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->dimensions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| The ID of the analytic object to retrieve. | 
 **id** | [**List[str]**](str.md)| The IDs of the dimensions to retrieve. Default is all dimensions. | [optional] 

### Return type

[**DimensionsDTO**](DimensionsDTO.md)

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

# **member**
> MembersDTO member(object_id, dimension_id, id, id2=id2)

Retrieve a dimension member

If you know the ID of a dimension member, use this API to retrieve that dimension member specifically. You must also know the dimension's ID and the analytic object's ID.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query_apis
from visier.model_query_apis.models.members_dto import MembersDTO
from visier.model_query_apis.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query_apis.Configuration(
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
configuration = visier.model_query_apis.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query_apis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query_apis.DataModelApi(api_client)
    object_id = 'object_id_example' # str | The ID of the analytic object.
    dimension_id = 'dimension_id_example' # str | The ID of the dimension.
    id = 'id_example' # str | 
    id2 = 'id_example' # str | The ID of the member to retrieve. (optional)

    try:
        # Retrieve a dimension member
        api_response = api_instance.member(object_id, dimension_id, id, id2=id2)
        print("The response of DataModelApi->member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| The ID of the analytic object. | 
 **dimension_id** | **str**| The ID of the dimension. | 
 **id** | **str**|  | 
 **id2** | **str**| The ID of the member to retrieve. | [optional] 

### Return type

[**MembersDTO**](MembersDTO.md)

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

# **members**
> MembersDTO members(object_id, dimension_id, id=id, max_level=max_level, filter=filter, var_field=var_field, include_data_members=include_data_members, offset=offset, limit=limit)

Retrieve a list of dimension members

If you know the ID of a dimension, use this API to retrieve the members of that dimension specifically. You must  also know the analytic object's ID. Dimension members exist in a hierarchy. The levels in the hierarchy may be  fixed or non-uniform. Leveled dimensions have fixed hierarchies, while parent-child dimensions have non-uniform  levels. When you retrieve dimension members with this API, the response returns the level of the dimension and the  path to get to that level. For example, in a Location dimension, Vancouver is 3 levels deep:   - All > Canada > British Columbia > Vancouver   Parent-child hierarchies are non-uniform and exhibit distinct characteristics such as time dependence and data  attributes. These traits reflect the dynamic nature of hierarchies, for example, organizational hierarchies. The API  response includes elements that express the validity ranges for retrieved members.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query_apis
from visier.model_query_apis.models.members_dto import MembersDTO
from visier.model_query_apis.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query_apis.Configuration(
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
configuration = visier.model_query_apis.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query_apis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query_apis.DataModelApi(api_client)
    object_id = 'object_id_example' # str | The ID of the analytic object.
    dimension_id = 'dimension_id_example' # str | The ID of the dimension.
    id = ['id_example'] # List[str] | The IDs of the members to retrieve. Default is all members. (optional)
    max_level = 56 # int | The maximum level in the hierarchy to fetch. The top level of the hierarchy is 0. Default is all levels. (optional)
    filter = 'filter_example' # str | A regular expression that members must match to be retrieved. Default is to retrieve all members. (optional)
    var_field = 'var_field_example' # str | Indicates the aspect of the member to apply the filter to. Possible values are:  - **id**: Match the filter to the member ID.  - **display**: Match the filter to the member's display name.  - **either**: Match the filter to the member ID or display name.   Default is id. (optional)
    include_data_members = True # bool | Indicates whether data members are included in the response. Parent-child dimensions only. Default is false. (optional)
    offset = 56 # int | For paginated member requests against high-cardinality dimensions, the offset of the first member to retrieve. Default is 0. If the `offset` value is specified to a non-default value, all other non-pagination parameters are ignored. (optional)
    limit = 56 # int | For paginated member requests against high-cardinality dimensions, the maximum number of members to retrieve. Default is -1, meaning no limit. If the `limit` value is specified to a non-default value, all other non-pagination parameters are ignored. (optional)

    try:
        # Retrieve a list of dimension members
        api_response = api_instance.members(object_id, dimension_id, id=id, max_level=max_level, filter=filter, var_field=var_field, include_data_members=include_data_members, offset=offset, limit=limit)
        print("The response of DataModelApi->members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| The ID of the analytic object. | 
 **dimension_id** | **str**| The ID of the dimension. | 
 **id** | [**List[str]**](str.md)| The IDs of the members to retrieve. Default is all members. | [optional] 
 **max_level** | **int**| The maximum level in the hierarchy to fetch. The top level of the hierarchy is 0. Default is all levels. | [optional] 
 **filter** | **str**| A regular expression that members must match to be retrieved. Default is to retrieve all members. | [optional] 
 **var_field** | **str**| Indicates the aspect of the member to apply the filter to. Possible values are:  - **id**: Match the filter to the member ID.  - **display**: Match the filter to the member&#39;s display name.  - **either**: Match the filter to the member ID or display name.   Default is id. | [optional] 
 **include_data_members** | **bool**| Indicates whether data members are included in the response. Parent-child dimensions only. Default is false. | [optional] 
 **offset** | **int**| For paginated member requests against high-cardinality dimensions, the offset of the first member to retrieve. Default is 0. If the &#x60;offset&#x60; value is specified to a non-default value, all other non-pagination parameters are ignored. | [optional] 
 **limit** | **int**| For paginated member requests against high-cardinality dimensions, the maximum number of members to retrieve. Default is -1, meaning no limit. If the &#x60;limit&#x60; value is specified to a non-default value, all other non-pagination parameters are ignored. | [optional] 

### Return type

[**MembersDTO**](MembersDTO.md)

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

# **metric**
> MetricDTO metric(id)

Retrieve a metric by ID

If you know the ID of a metric, use this API to retrieve that metric specifically.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query_apis
from visier.model_query_apis.models.metric_dto import MetricDTO
from visier.model_query_apis.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query_apis.Configuration(
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
configuration = visier.model_query_apis.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query_apis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query_apis.DataModelApi(api_client)
    id = 'id_example' # str | The ID of the metric to retrieve.

    try:
        # Retrieve a metric by ID
        api_response = api_instance.metric(id)
        print("The response of DataModelApi->metric:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->metric: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the metric to retrieve. | 

### Return type

[**MetricDTO**](MetricDTO.md)

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

# **metric_dimensions**
> DimensionsDTO metric_dimensions(metric_id, id=id)

Retrieve a metric's dimensions

Use this API to retrieve a list of dimensions for a specific metric.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query_apis
from visier.model_query_apis.models.dimensions_dto import DimensionsDTO
from visier.model_query_apis.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query_apis.Configuration(
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
configuration = visier.model_query_apis.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query_apis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query_apis.DataModelApi(api_client)
    metric_id = 'metric_id_example' # str | The ID of the metric to retrieve.
    id = ['id_example'] # List[str] | The IDs of the dimensions to retrieve. Default is all dimensions. (optional)

    try:
        # Retrieve a metric's dimensions
        api_response = api_instance.metric_dimensions(metric_id, id=id)
        print("The response of DataModelApi->metric_dimensions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->metric_dimensions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric_id** | **str**| The ID of the metric to retrieve. | 
 **id** | [**List[str]**](str.md)| The IDs of the dimensions to retrieve. Default is all dimensions. | [optional] 

### Return type

[**DimensionsDTO**](DimensionsDTO.md)

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

# **metric_selection_concepts**
> SelectionConceptsDTO metric_selection_concepts(metric_id, id=id)

Retrieve a metric's selection concepts

Use this API to retrieve a list of selection concepts for a specific metric

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query_apis
from visier.model_query_apis.models.selection_concepts_dto import SelectionConceptsDTO
from visier.model_query_apis.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query_apis.Configuration(
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
configuration = visier.model_query_apis.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query_apis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query_apis.DataModelApi(api_client)
    metric_id = 'metric_id_example' # str | The ID of the metric to retrieve.
    id = ['id_example'] # List[str] | The IDs of the selection concepts to retrieve. Default is all selection concepts. (optional)

    try:
        # Retrieve a metric's selection concepts
        api_response = api_instance.metric_selection_concepts(metric_id, id=id)
        print("The response of DataModelApi->metric_selection_concepts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->metric_selection_concepts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric_id** | **str**| The ID of the metric to retrieve. | 
 **id** | [**List[str]**](str.md)| The IDs of the selection concepts to retrieve. Default is all selection concepts. | [optional] 

### Return type

[**SelectionConceptsDTO**](SelectionConceptsDTO.md)

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

# **metrics**
> MetricsDTO metrics(id=id, category=category)

Retrieve a list of metrics

Use this API to retrieve all the metrics in your Visier solution.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query_apis
from visier.model_query_apis.models.metrics_dto import MetricsDTO
from visier.model_query_apis.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query_apis.Configuration(
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
configuration = visier.model_query_apis.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query_apis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query_apis.DataModelApi(api_client)
    id = ['id_example'] # List[str] | The IDs of the metrics to retrieve. Default is all metrics. (optional)
    category = 'category_example' # str | The category to filter the returned metrics by. (optional)

    try:
        # Retrieve a list of metrics
        api_response = api_instance.metrics(id=id, category=category)
        print("The response of DataModelApi->metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**List[str]**](str.md)| The IDs of the metrics to retrieve. Default is all metrics. | [optional] 
 **category** | **str**| The category to filter the returned metrics by. | [optional] 

### Return type

[**MetricsDTO**](MetricsDTO.md)

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

# **planning_metrics**
> MetricsDTO planning_metrics(id)

Retrieve metrics by planning model ID

Use this API to retrieve all the metrics you have access to for a planning model.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query_apis
from visier.model_query_apis.models.metrics_dto import MetricsDTO
from visier.model_query_apis.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query_apis.Configuration(
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
configuration = visier.model_query_apis.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query_apis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query_apis.DataModelApi(api_client)
    id = 'id_example' # str | The ID of the planning model to retrieve.

    try:
        # Retrieve metrics by planning model ID
        api_response = api_instance.planning_metrics(id)
        print("The response of DataModelApi->planning_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->planning_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the planning model to retrieve. | 

### Return type

[**MetricsDTO**](MetricsDTO.md)

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

# **planning_model**
> PlanningModelDTO planning_model(id)

Retrieve a planning model by ID

Use this API to retrieve a specific planning model you have access to.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query_apis
from visier.model_query_apis.models.planning_model_dto import PlanningModelDTO
from visier.model_query_apis.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query_apis.Configuration(
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
configuration = visier.model_query_apis.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query_apis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query_apis.DataModelApi(api_client)
    id = 'id_example' # str | The ID of the planning model to retrieve.

    try:
        # Retrieve a planning model by ID
        api_response = api_instance.planning_model(id)
        print("The response of DataModelApi->planning_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->planning_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the planning model to retrieve. | 

### Return type

[**PlanningModelDTO**](PlanningModelDTO.md)

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

# **planning_models**
> PlanningModelsDTO planning_models(id=id)

Retrieve a list of planning models

Use this API to retrieve all the planning models you have access to.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query_apis
from visier.model_query_apis.models.planning_models_dto import PlanningModelsDTO
from visier.model_query_apis.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query_apis.Configuration(
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
configuration = visier.model_query_apis.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query_apis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query_apis.DataModelApi(api_client)
    id = ['id_example'] # List[str] | The IDs of the planning models to retrieve. Default is all models. (optional)

    try:
        # Retrieve a list of planning models
        api_response = api_instance.planning_models(id=id)
        print("The response of DataModelApi->planning_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->planning_models: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**List[str]**](str.md)| The IDs of the planning models to retrieve. Default is all models. | [optional] 

### Return type

[**PlanningModelsDTO**](PlanningModelsDTO.md)

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

# **planning_plan**
> PlanningPlanDTO planning_plan(model_id, id)

Retrieve a plan by ID

Use this API to retrieve a specific plan that you have access to in a planning model.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query_apis
from visier.model_query_apis.models.planning_plan_dto import PlanningPlanDTO
from visier.model_query_apis.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query_apis.Configuration(
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
configuration = visier.model_query_apis.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query_apis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query_apis.DataModelApi(api_client)
    model_id = 'model_id_example' # str | The ID of the planning model to retrieve.
    id = 'id_example' # str | The ID of the plan to retrieve.

    try:
        # Retrieve a plan by ID
        api_response = api_instance.planning_plan(model_id, id)
        print("The response of DataModelApi->planning_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->planning_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **str**| The ID of the planning model to retrieve. | 
 **id** | **str**| The ID of the plan to retrieve. | 

### Return type

[**PlanningPlanDTO**](PlanningPlanDTO.md)

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

# **planning_plans**
> PlanningPlansDTO planning_plans(model_id, id=id)

Retrieve a list of plans

Use this API to retrieve all the plans you have access to for a planning model.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query_apis
from visier.model_query_apis.models.planning_plans_dto import PlanningPlansDTO
from visier.model_query_apis.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query_apis.Configuration(
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
configuration = visier.model_query_apis.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query_apis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query_apis.DataModelApi(api_client)
    model_id = 'model_id_example' # str | The ID of the planning model to retrieve.
    id = ['id_example'] # List[str] | The IDs of the plans to retrieve. Default is all plans. (optional)

    try:
        # Retrieve a list of plans
        api_response = api_instance.planning_plans(model_id, id=id)
        print("The response of DataModelApi->planning_plans:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->planning_plans: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **str**| The ID of the planning model to retrieve. | 
 **id** | [**List[str]**](str.md)| The IDs of the plans to retrieve. Default is all plans. | [optional] 

### Return type

[**PlanningPlansDTO**](PlanningPlansDTO.md)

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

# **prediction**
> PredictionDTO prediction(id)

Retrieve a prediction by ID

If you know the ID of a prediction, use this API to retrieve that prediction specifically.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query_apis
from visier.model_query_apis.models.prediction_dto import PredictionDTO
from visier.model_query_apis.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query_apis.Configuration(
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
configuration = visier.model_query_apis.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query_apis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query_apis.DataModelApi(api_client)
    id = 'id_example' # str | The ID of the prediction to retrieve.

    try:
        # Retrieve a prediction by ID
        api_response = api_instance.prediction(id)
        print("The response of DataModelApi->prediction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->prediction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the prediction to retrieve. | 

### Return type

[**PredictionDTO**](PredictionDTO.md)

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

# **predictions**
> PredictionsDTO predictions(id=id)

Retrieve a list of predictions

Use this API to retrieve all the predictions in your Visier solution.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query_apis
from visier.model_query_apis.models.predictions_dto import PredictionsDTO
from visier.model_query_apis.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query_apis.Configuration(
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
configuration = visier.model_query_apis.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query_apis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query_apis.DataModelApi(api_client)
    id = ['id_example'] # List[str] | The IDs of the predictions to retrieve. Default is all predictions. (optional)

    try:
        # Retrieve a list of predictions
        api_response = api_instance.predictions(id=id)
        print("The response of DataModelApi->predictions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->predictions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**List[str]**](str.md)| The IDs of the predictions to retrieve. Default is all predictions. | [optional] 

### Return type

[**PredictionsDTO**](PredictionsDTO.md)

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

# **properties**
> PropertiesDTO properties(object_id, id=id)

Retrieve a list of properties

Use this API to retrieve a list of properties for a specific analytic object.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query_apis
from visier.model_query_apis.models.properties_dto import PropertiesDTO
from visier.model_query_apis.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query_apis.Configuration(
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
configuration = visier.model_query_apis.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query_apis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query_apis.DataModelApi(api_client)
    object_id = 'object_id_example' # str | The ID of the analytic object to retrieve.
    id = ['id_example'] # List[str] | The IDs of the properties to retrieve. Default is all properties. (optional)

    try:
        # Retrieve a list of properties
        api_response = api_instance.properties(object_id, id=id)
        print("The response of DataModelApi->properties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->properties: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| The ID of the analytic object to retrieve. | 
 **id** | [**List[str]**](str.md)| The IDs of the properties to retrieve. Default is all properties. | [optional] 

### Return type

[**PropertiesDTO**](PropertiesDTO.md)

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

# **selection_concept**
> SelectionConceptDTO selection_concept(object_id, id)

Retrieve an analytic object's selection concept by ID

If you know the ID of a selection concept, use this API to retrieve that selection concept specifically. You must also know the analytic object's ID.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query_apis
from visier.model_query_apis.models.selection_concept_dto import SelectionConceptDTO
from visier.model_query_apis.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query_apis.Configuration(
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
configuration = visier.model_query_apis.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query_apis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query_apis.DataModelApi(api_client)
    object_id = 'object_id_example' # str | The ID of the analytic object to retrieve.
    id = 'id_example' # str | The ID of the selection concept to retrieve.

    try:
        # Retrieve an analytic object's selection concept by ID
        api_response = api_instance.selection_concept(object_id, id)
        print("The response of DataModelApi->selection_concept:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->selection_concept: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| The ID of the analytic object to retrieve. | 
 **id** | **str**| The ID of the selection concept to retrieve. | 

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

# **selection_concepts**
> SelectionConceptsDTO selection_concepts(object_id, id=id)

Retrieve an analytic object's selection concepts

Use this API to retrieve a list of selection concepts for a specific analytic object.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query_apis
from visier.model_query_apis.models.selection_concepts_dto import SelectionConceptsDTO
from visier.model_query_apis.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query_apis.Configuration(
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
configuration = visier.model_query_apis.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query_apis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query_apis.DataModelApi(api_client)
    object_id = 'object_id_example' # str | The ID of the analytic object to retrieve.
    id = ['id_example'] # List[str] | The IDs of the selection concepts to retrieve. Default is all selection concepts. (optional)

    try:
        # Retrieve an analytic object's selection concepts
        api_response = api_instance.selection_concepts(object_id, id=id)
        print("The response of DataModelApi->selection_concepts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->selection_concepts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| The ID of the analytic object to retrieve. | 
 **id** | [**List[str]**](str.md)| The IDs of the selection concepts to retrieve. Default is all selection concepts. | [optional] 

### Return type

[**SelectionConceptsDTO**](SelectionConceptsDTO.md)

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

