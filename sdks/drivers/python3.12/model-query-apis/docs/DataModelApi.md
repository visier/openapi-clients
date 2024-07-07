# visier.model_query.DataModelApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_model_analytic_object**](DataModelApi.md#data_model_analytic_object) | **GET** /v1/data/model/analytic-objects/{id} | Retrieve an analytic object by ID
[**data_model_analytic_objects**](DataModelApi.md#data_model_analytic_objects) | **GET** /v1/data/model/analytic-objects | Retrieve a list of analytic objects
[**data_model_currencies**](DataModelApi.md#data_model_currencies) | **GET** /v1/data/model/currencies | Retrieve all currencies
[**data_model_currency**](DataModelApi.md#data_model_currency) | **GET** /v1/data/model/currencies/{id} | Retrieve a currency
[**data_model_currency_rates**](DataModelApi.md#data_model_currency_rates) | **GET** /v1/data/model/currencies/{id}/rates | Retrieve all exchange rates for a currency
[**data_model_currency_rates_with_to_currency**](DataModelApi.md#data_model_currency_rates_with_to_currency) | **GET** /v1/data/model/currencies/{id}/rates/{toId} | Retrieve exchange rates from one currency to another currency
[**data_model_dimension**](DataModelApi.md#data_model_dimension) | **GET** /v1/data/model/analytic-objects/{objectId}/dimensions/{id} | Retrieve a dimension by ID
[**data_model_dimensions**](DataModelApi.md#data_model_dimensions) | **GET** /v1/data/model/analytic-objects/{objectId}/dimensions | Retrieve a list of dimensions
[**data_model_member**](DataModelApi.md#data_model_member) | **GET** /v1/data/model/analytic-objects/{objectId}/dimensions/{dimensionId}/members/{id} | Retrieve a dimension member
[**data_model_members**](DataModelApi.md#data_model_members) | **GET** /v1/data/model/analytic-objects/{objectId}/dimensions/{dimensionId}/members | Retrieve a list of dimension members
[**data_model_metric**](DataModelApi.md#data_model_metric) | **GET** /v1/data/model/metrics/{id} | Retrieve a metric by ID
[**data_model_metric_dimensions**](DataModelApi.md#data_model_metric_dimensions) | **GET** /v1/data/model/metrics/{metricId}/dimensions | Retrieve a metric&#39;s dimensions
[**data_model_metric_selection_concepts**](DataModelApi.md#data_model_metric_selection_concepts) | **GET** /v1/data/model/metrics/{metricId}/selection-concepts | Retrieve a metric&#39;s selection concepts
[**data_model_metrics**](DataModelApi.md#data_model_metrics) | **GET** /v1/data/model/metrics | Retrieve a list of metrics
[**data_model_planning_metrics**](DataModelApi.md#data_model_planning_metrics) | **GET** /v1/data/model/plan-models/{id}/metrics | Retrieve metrics by planning model ID
[**data_model_planning_model**](DataModelApi.md#data_model_planning_model) | **GET** /v1/data/model/plan-models/{id} | Retrieve a planning model by ID
[**data_model_planning_models**](DataModelApi.md#data_model_planning_models) | **GET** /v1/data/model/plan-models | Retrieve a list of planning models
[**data_model_planning_plan**](DataModelApi.md#data_model_planning_plan) | **GET** /v1/data/model/plan-models/{modelId}/plans/{id} | Retrieve a plan by ID
[**data_model_planning_plans**](DataModelApi.md#data_model_planning_plans) | **GET** /v1/data/model/plan-models/{modelId}/plans | Retrieve a list of plans
[**data_model_prediction**](DataModelApi.md#data_model_prediction) | **GET** /v1/data/model/predictions/{id} | Retrieve a prediction by ID
[**data_model_predictions**](DataModelApi.md#data_model_predictions) | **GET** /v1/data/model/predictions | Retrieve a list of predictions
[**data_model_properties**](DataModelApi.md#data_model_properties) | **GET** /v1/data/model/analytic-objects/{objectId}/properties | Retrieve a list of properties
[**data_model_property**](DataModelApi.md#data_model_property) | **GET** /v1/data/model/analytic-objects/{objectId}/properties/{id} | Retrieve a property by ID
[**data_model_selection_concept**](DataModelApi.md#data_model_selection_concept) | **GET** /v1/data/model/analytic-objects/{objectId}/selection-concepts/{id} | Retrieve an analytic object&#39;s selection concept by ID
[**data_model_selection_concepts**](DataModelApi.md#data_model_selection_concepts) | **GET** /v1/data/model/analytic-objects/{objectId}/selection-concepts | Retrieve an analytic object&#39;s selection concepts


# **data_model_analytic_object**
> AnalyticObjectDTO data_model_analytic_object(id)

Retrieve an analytic object by ID

If you know the ID of an analytic object, use this API to retrieve that object specifically.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query
from visier.model_query.models.analytic_object_dto import AnalyticObjectDTO
from visier.model_query.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query.Configuration(
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
configuration = visier.model_query.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query.DataModelApi(api_client)
    id = 'id_example' # str | The ID of the analytic object to retrieve.

    try:
        # Retrieve an analytic object by ID
        api_response = api_instance.data_model_analytic_object(id)
        print("The response of DataModelApi->data_model_analytic_object:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->data_model_analytic_object: %s\n" % e)
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

# **data_model_analytic_objects**
> AnalyticObjectsDTO data_model_analytic_objects(id=id, object_type=object_type)

Retrieve a list of analytic objects

Use this API to retrieve all the analytic objects in your Visier solution.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query
from visier.model_query.models.analytic_objects_dto import AnalyticObjectsDTO
from visier.model_query.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query.Configuration(
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
configuration = visier.model_query.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query.DataModelApi(api_client)
    id = ['id_example'] # List[str] | The IDs of the analytic objects to retrieve. Default is all analytic objects. (optional)
    object_type = 'object_type_example' # str | The object type to filter the returned analytic objects by. (optional)

    try:
        # Retrieve a list of analytic objects
        api_response = api_instance.data_model_analytic_objects(id=id, object_type=object_type)
        print("The response of DataModelApi->data_model_analytic_objects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->data_model_analytic_objects: %s\n" % e)
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

# **data_model_currencies**
> CurrenciesDTO data_model_currencies()

Retrieve all currencies

Use this API to retrieve all the available currencies in your Visier solution.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query
from visier.model_query.models.currencies_dto import CurrenciesDTO
from visier.model_query.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query.Configuration(
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
configuration = visier.model_query.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query.DataModelApi(api_client)

    try:
        # Retrieve all currencies
        api_response = api_instance.data_model_currencies()
        print("The response of DataModelApi->data_model_currencies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->data_model_currencies: %s\n" % e)
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

# **data_model_currency**
> CurrencyDTO data_model_currency(id)

Retrieve a currency

Use this API to retrieve a specific currency if you know the currency code.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query
from visier.model_query.models.currency_dto import CurrencyDTO
from visier.model_query.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query.Configuration(
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
configuration = visier.model_query.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query.DataModelApi(api_client)
    id = 'id_example' # str | The ISO 4217 3-letter code for the currency.

    try:
        # Retrieve a currency
        api_response = api_instance.data_model_currency(id)
        print("The response of DataModelApi->data_model_currency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->data_model_currency: %s\n" % e)
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

# **data_model_currency_rates**
> CurrencyRatesDTO data_model_currency_rates(id, start_time=start_time, end_time=end_time, decimals=decimals)

Retrieve all exchange rates for a currency

Use this API to retrieve exchange rates for a specific currency from Visier.  You can optionally specify query parameter options for the returned rates, such as the number of decimals to round the exchange rate to.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query
from visier.model_query.models.currency_rates_dto import CurrencyRatesDTO
from visier.model_query.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query.Configuration(
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
configuration = visier.model_query.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query.DataModelApi(api_client)
    id = 'id_example' # str | The ISO 4217 3-letter code for the currency to get rates for.
    start_time = 'start_time_example' # str | The earliest time instant to retrieve exchange rates from. Default is to use 0 milliseconds. (optional)
    end_time = 'end_time_example' # str | The latest time instant to retrieve exchange rates from. Default is to use the time of this request in milliseconds. (optional)
    decimals = 'decimals_example' # str | The number of decimals to round exchange rates to. Default is to round to 2 decimal places. (optional)

    try:
        # Retrieve all exchange rates for a currency
        api_response = api_instance.data_model_currency_rates(id, start_time=start_time, end_time=end_time, decimals=decimals)
        print("The response of DataModelApi->data_model_currency_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->data_model_currency_rates: %s\n" % e)
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

# **data_model_currency_rates_with_to_currency**
> CurrencyRatesDTO data_model_currency_rates_with_to_currency(id, to_id, start_time=start_time, end_time=end_time, decimals=decimals)

Retrieve exchange rates from one currency to another currency

Use this API to retrieve exchange rates from a specific currency to another specific currency.  You can optionally specify query parameter options for the returned rates, such as the number of decimals to round the exchange rate to.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query
from visier.model_query.models.currency_rates_dto import CurrencyRatesDTO
from visier.model_query.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query.Configuration(
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
configuration = visier.model_query.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query.DataModelApi(api_client)
    id = 'id_example' # str | The ISO 4217 3-letter code for the currency to convert from.
    to_id = 'to_id_example' # str | The ISO 4217 3-letter code for the currency to convert to.
    start_time = 'start_time_example' # str | The earliest time instant to retrieve exchange rates from. Default is to use 0 milliseconds. (optional)
    end_time = 'end_time_example' # str | The latest time instant to retrieve exchange rates from. Default is to use the time of this request in milliseconds. (optional)
    decimals = 'decimals_example' # str | The number of decimals to round exchange rates to. Default is to round to 2 decimal places. (optional)

    try:
        # Retrieve exchange rates from one currency to another currency
        api_response = api_instance.data_model_currency_rates_with_to_currency(id, to_id, start_time=start_time, end_time=end_time, decimals=decimals)
        print("The response of DataModelApi->data_model_currency_rates_with_to_currency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->data_model_currency_rates_with_to_currency: %s\n" % e)
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

# **data_model_dimension**
> DimensionDTO data_model_dimension(object_id, id)

Retrieve a dimension by ID

If you know the ID of a dimension, use this API to retrieve that dimension specifically. You must also know the analytic object's ID.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query
from visier.model_query.models.dimension_dto import DimensionDTO
from visier.model_query.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query.Configuration(
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
configuration = visier.model_query.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query.DataModelApi(api_client)
    object_id = 'object_id_example' # str | The ID of the analytic object to retrieve.
    id = 'id_example' # str | The ID of the dimension to retrieve.

    try:
        # Retrieve a dimension by ID
        api_response = api_instance.data_model_dimension(object_id, id)
        print("The response of DataModelApi->data_model_dimension:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->data_model_dimension: %s\n" % e)
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

# **data_model_dimensions**
> DimensionsDTO data_model_dimensions(object_id, id=id)

Retrieve a list of dimensions

Use this API to retrieve a list of dimensions for a specific analytic object.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query
from visier.model_query.models.dimensions_dto import DimensionsDTO
from visier.model_query.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query.Configuration(
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
configuration = visier.model_query.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query.DataModelApi(api_client)
    object_id = 'object_id_example' # str | The ID of the analytic object to retrieve.
    id = ['id_example'] # List[str] | The IDs of the dimensions to retrieve. Default is all dimensions. (optional)

    try:
        # Retrieve a list of dimensions
        api_response = api_instance.data_model_dimensions(object_id, id=id)
        print("The response of DataModelApi->data_model_dimensions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->data_model_dimensions: %s\n" % e)
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

# **data_model_member**
> MembersDTO data_model_member(object_id, dimension_id, id, id2=id2)

Retrieve a dimension member

If you know the ID of a dimension member, use this API to retrieve that dimension member specifically. You must also know the dimension's ID and the analytic object's ID.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query
from visier.model_query.models.members_dto import MembersDTO
from visier.model_query.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query.Configuration(
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
configuration = visier.model_query.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query.DataModelApi(api_client)
    object_id = 'object_id_example' # str | The ID of the analytic object
    dimension_id = 'dimension_id_example' # str | The ID of the dimension
    id = 'id_example' # str | 
    id2 = 'id_example' # str | The ID of the member to retrieve (optional)

    try:
        # Retrieve a dimension member
        api_response = api_instance.data_model_member(object_id, dimension_id, id, id2=id2)
        print("The response of DataModelApi->data_model_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->data_model_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| The ID of the analytic object | 
 **dimension_id** | **str**| The ID of the dimension | 
 **id** | **str**|  | 
 **id2** | **str**| The ID of the member to retrieve | [optional] 

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

# **data_model_members**
> MembersDTO data_model_members(object_id, dimension_id, id=id, max_level=max_level, filter=filter, var_field=var_field, include_data_members=include_data_members, offset=offset, limit=limit)

Retrieve a list of dimension members

If you know the ID of a dimension, use this API to retrieve the members of that dimension specifically. You must  also know the analytic object's ID. Dimension members exist in a hierarchy. The levels in the hierarchy may be  fixed or non-uniform. Leveled dimensions have fixed hierarchies, while parent-child dimensions have non-uniform  levels. When you retrieve dimension members with this API, the response returns the level of the dimension and the  path to get to that level. For example, in a Location dimension, Vancouver is 3 levels deep:   - All > Canada > British Columbia > Vancouver   Parent-child hierarchies are non-uniform and exhibit distinct characteristics such as time dependence and data  attributes. These traits reflect the dynamic nature of hierarchies, for example, organizational hierarchies. The API  response includes elements that express the validity ranges for retrieved members.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query
from visier.model_query.models.members_dto import MembersDTO
from visier.model_query.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query.Configuration(
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
configuration = visier.model_query.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query.DataModelApi(api_client)
    object_id = 'object_id_example' # str | The ID of the analytic object
    dimension_id = 'dimension_id_example' # str | The ID of the dimension
    id = ['id_example'] # List[str] | The IDs of the members to retrieve. Default is all members. (optional)
    max_level = 56 # int | The maximum level in the hierarchy to fetch. The top level of the hierarchy is 0. Default is all levels. (optional)
    filter = 'filter_example' # str | A regular expression that members must match to be retrieved. Default is to retrieve all members. (optional)
    var_field = 'var_field_example' # str | Indicates the aspect of the member to apply the filter to. Possible values are:  - **id**: Match the filter to the member ID.  - **display**: Match the filter to the member's display name.  - **either**: Match the filter to the member ID or display name.   Default is id. (optional)
    include_data_members = True # bool | Indicates whether data members are included in the response. Parent-child dimensions only. Default is false. (optional)
    offset = 56 # int | For paginated member requests against high-cardinality dimensions, the offset of the first member to retrieve. Default is 0. If the `offset` value is specified to a non-default value, all other non-pagination parameters are ignored. (optional)
    limit = 56 # int | For paginated member requests against high-cardinality dimensions, the maximum number of members to retrieve. Default is -1, meaning no limit. If the `limit` value is specified to a non-default value, all other non-pagination parameters are ignored. (optional)

    try:
        # Retrieve a list of dimension members
        api_response = api_instance.data_model_members(object_id, dimension_id, id=id, max_level=max_level, filter=filter, var_field=var_field, include_data_members=include_data_members, offset=offset, limit=limit)
        print("The response of DataModelApi->data_model_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->data_model_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| The ID of the analytic object | 
 **dimension_id** | **str**| The ID of the dimension | 
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

# **data_model_metric**
> MetricDTO data_model_metric(id)

Retrieve a metric by ID

If you know the ID of a metric, use this API to retrieve that metric specifically.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query
from visier.model_query.models.metric_dto import MetricDTO
from visier.model_query.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query.Configuration(
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
configuration = visier.model_query.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query.DataModelApi(api_client)
    id = 'id_example' # str | The ID of the metric to retrieve.

    try:
        # Retrieve a metric by ID
        api_response = api_instance.data_model_metric(id)
        print("The response of DataModelApi->data_model_metric:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->data_model_metric: %s\n" % e)
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

# **data_model_metric_dimensions**
> DimensionsDTO data_model_metric_dimensions(metric_id, id=id)

Retrieve a metric's dimensions

Use this API to retrieve a list of dimensions for a specific metric.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query
from visier.model_query.models.dimensions_dto import DimensionsDTO
from visier.model_query.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query.Configuration(
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
configuration = visier.model_query.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query.DataModelApi(api_client)
    metric_id = 'metric_id_example' # str | The ID of the metric to retrieve.
    id = ['id_example'] # List[str] | The IDs of the dimensions to retrieve. Default is all dimensions. (optional)

    try:
        # Retrieve a metric's dimensions
        api_response = api_instance.data_model_metric_dimensions(metric_id, id=id)
        print("The response of DataModelApi->data_model_metric_dimensions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->data_model_metric_dimensions: %s\n" % e)
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

# **data_model_metric_selection_concepts**
> SelectionConceptsDTO data_model_metric_selection_concepts(metric_id, id=id)

Retrieve a metric's selection concepts

Use this API to retrieve a list of selection concepts for a specific metric

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query
from visier.model_query.models.selection_concepts_dto import SelectionConceptsDTO
from visier.model_query.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query.Configuration(
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
configuration = visier.model_query.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query.DataModelApi(api_client)
    metric_id = 'metric_id_example' # str | The ID of the metric to retrieve.
    id = ['id_example'] # List[str] | The IDs of the selection concepts to retrieve. Default is all selection concepts. (optional)

    try:
        # Retrieve a metric's selection concepts
        api_response = api_instance.data_model_metric_selection_concepts(metric_id, id=id)
        print("The response of DataModelApi->data_model_metric_selection_concepts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->data_model_metric_selection_concepts: %s\n" % e)
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

# **data_model_metrics**
> MetricsDTO data_model_metrics(id=id, category=category)

Retrieve a list of metrics

Use this API to retrieve all the metrics in your Visier solution.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query
from visier.model_query.models.metrics_dto import MetricsDTO
from visier.model_query.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query.Configuration(
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
configuration = visier.model_query.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query.DataModelApi(api_client)
    id = ['id_example'] # List[str] | The IDs of the metrics to retrieve. Default is all metrics. (optional)
    category = 'category_example' # str | The category to filter the returned metrics by. (optional)

    try:
        # Retrieve a list of metrics
        api_response = api_instance.data_model_metrics(id=id, category=category)
        print("The response of DataModelApi->data_model_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->data_model_metrics: %s\n" % e)
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

# **data_model_planning_metrics**
> MetricsDTO data_model_planning_metrics(id)

Retrieve metrics by planning model ID

Use this API to retrieve all the metrics you have access to for a planning model.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query
from visier.model_query.models.metrics_dto import MetricsDTO
from visier.model_query.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query.Configuration(
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
configuration = visier.model_query.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query.DataModelApi(api_client)
    id = 'id_example' # str | The ID of the planning model to retrieve.

    try:
        # Retrieve metrics by planning model ID
        api_response = api_instance.data_model_planning_metrics(id)
        print("The response of DataModelApi->data_model_planning_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->data_model_planning_metrics: %s\n" % e)
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

# **data_model_planning_model**
> PlanningModelDTO data_model_planning_model(id)

Retrieve a planning model by ID

Use this API to retrieve a specific planning model you have access to.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query
from visier.model_query.models.planning_model_dto import PlanningModelDTO
from visier.model_query.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query.Configuration(
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
configuration = visier.model_query.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query.DataModelApi(api_client)
    id = 'id_example' # str | The ID of the planning model to retrieve.

    try:
        # Retrieve a planning model by ID
        api_response = api_instance.data_model_planning_model(id)
        print("The response of DataModelApi->data_model_planning_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->data_model_planning_model: %s\n" % e)
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

# **data_model_planning_models**
> PlanningModelsDTO data_model_planning_models(id=id)

Retrieve a list of planning models

Use this API to retrieve all the planning models you have access to.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query
from visier.model_query.models.planning_models_dto import PlanningModelsDTO
from visier.model_query.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query.Configuration(
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
configuration = visier.model_query.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query.DataModelApi(api_client)
    id = ['id_example'] # List[str] | The IDs of the planning models to retrieve. Default is all models. (optional)

    try:
        # Retrieve a list of planning models
        api_response = api_instance.data_model_planning_models(id=id)
        print("The response of DataModelApi->data_model_planning_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->data_model_planning_models: %s\n" % e)
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

# **data_model_planning_plan**
> PlanningPlanDTO data_model_planning_plan(model_id, id)

Retrieve a plan by ID

Use this API to retrieve a specific plan that you have access to in a planning model.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query
from visier.model_query.models.planning_plan_dto import PlanningPlanDTO
from visier.model_query.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query.Configuration(
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
configuration = visier.model_query.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query.DataModelApi(api_client)
    model_id = 'model_id_example' # str | The ID of the planning model to retrieve.
    id = 'id_example' # str | The ID of the plan to retrieve.

    try:
        # Retrieve a plan by ID
        api_response = api_instance.data_model_planning_plan(model_id, id)
        print("The response of DataModelApi->data_model_planning_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->data_model_planning_plan: %s\n" % e)
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

# **data_model_planning_plans**
> PlanningPlansDTO data_model_planning_plans(model_id, id=id)

Retrieve a list of plans

Use this API to retrieve all the plans you have access to for a planning model.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query
from visier.model_query.models.planning_plans_dto import PlanningPlansDTO
from visier.model_query.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query.Configuration(
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
configuration = visier.model_query.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query.DataModelApi(api_client)
    model_id = 'model_id_example' # str | The ID of the planning model to retrieve.
    id = ['id_example'] # List[str] | The IDs of the plans to retrieve. Default is all plans. (optional)

    try:
        # Retrieve a list of plans
        api_response = api_instance.data_model_planning_plans(model_id, id=id)
        print("The response of DataModelApi->data_model_planning_plans:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->data_model_planning_plans: %s\n" % e)
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

# **data_model_prediction**
> PredictionDTO data_model_prediction(id)

Retrieve a prediction by ID

If you know the ID of a prediction, use this API to retrieve that prediction specifically.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query
from visier.model_query.models.prediction_dto import PredictionDTO
from visier.model_query.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query.Configuration(
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
configuration = visier.model_query.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query.DataModelApi(api_client)
    id = 'id_example' # str | The ID of the prediction to retrieve.

    try:
        # Retrieve a prediction by ID
        api_response = api_instance.data_model_prediction(id)
        print("The response of DataModelApi->data_model_prediction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->data_model_prediction: %s\n" % e)
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

# **data_model_predictions**
> PredictionsDTO data_model_predictions(id=id)

Retrieve a list of predictions

Use this API to retrieve all the predictions in your Visier solution.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query
from visier.model_query.models.predictions_dto import PredictionsDTO
from visier.model_query.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query.Configuration(
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
configuration = visier.model_query.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query.DataModelApi(api_client)
    id = ['id_example'] # List[str] | The IDs of the predictions to retrieve. Default is all predictions. (optional)

    try:
        # Retrieve a list of predictions
        api_response = api_instance.data_model_predictions(id=id)
        print("The response of DataModelApi->data_model_predictions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->data_model_predictions: %s\n" % e)
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

# **data_model_properties**
> PropertiesDTO data_model_properties(object_id, id=id)

Retrieve a list of properties

Use this API to retrieve a list of properties for a specific analytic object.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query
from visier.model_query.models.properties_dto import PropertiesDTO
from visier.model_query.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query.Configuration(
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
configuration = visier.model_query.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query.DataModelApi(api_client)
    object_id = 'object_id_example' # str | The ID of the analytic object to retrieve.
    id = ['id_example'] # List[str] | The IDs of the properties to retrieve. Default is all properties. (optional)

    try:
        # Retrieve a list of properties
        api_response = api_instance.data_model_properties(object_id, id=id)
        print("The response of DataModelApi->data_model_properties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->data_model_properties: %s\n" % e)
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

# **data_model_property**
> PropertyDTO data_model_property(object_id, id)

Retrieve a property by ID

If you know the ID of a property, use this API to retrieve that property specifically. You must also know the analytic object's ID..

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query
from visier.model_query.models.property_dto import PropertyDTO
from visier.model_query.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query.Configuration(
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
configuration = visier.model_query.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query.DataModelApi(api_client)
    object_id = 'object_id_example' # str | The ID of the analytic object to retrieve.
    id = ['id_example'] # List[str] | The ID of the property to retrieve.

    try:
        # Retrieve a property by ID
        api_response = api_instance.data_model_property(object_id, id)
        print("The response of DataModelApi->data_model_property:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->data_model_property: %s\n" % e)
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

# **data_model_selection_concept**
> SelectionConceptDTO data_model_selection_concept(object_id, id)

Retrieve an analytic object's selection concept by ID

If you know the ID of a selection concept, use this API to retrieve that selection concept specifically. You must also know the analytic object's ID.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query
from visier.model_query.models.selection_concept_dto import SelectionConceptDTO
from visier.model_query.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query.Configuration(
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
configuration = visier.model_query.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query.DataModelApi(api_client)
    object_id = 'object_id_example' # str | The ID of the analytic object to retrieve.
    id = 'id_example' # str | The ID of the selection concept to retrieve.

    try:
        # Retrieve an analytic object's selection concept by ID
        api_response = api_instance.data_model_selection_concept(object_id, id)
        print("The response of DataModelApi->data_model_selection_concept:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->data_model_selection_concept: %s\n" % e)
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

# **data_model_selection_concepts**
> SelectionConceptsDTO data_model_selection_concepts(object_id, id=id)

Retrieve an analytic object's selection concepts

Use this API to retrieve a list of selection concepts for a specific analytic object.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query
from visier.model_query.models.selection_concepts_dto import SelectionConceptsDTO
from visier.model_query.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.model_query.Configuration(
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
configuration = visier.model_query.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.model_query.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.model_query.DataModelApi(api_client)
    object_id = 'object_id_example' # str | The ID of the analytic object to retrieve.
    id = ['id_example'] # List[str] | The IDs of the selection concepts to retrieve. Default is all selection concepts. (optional)

    try:
        # Retrieve an analytic object's selection concepts
        api_response = api_instance.data_model_selection_concepts(object_id, id=id)
        print("The response of DataModelApi->data_model_selection_concepts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataModelApi->data_model_selection_concepts: %s\n" % e)
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

