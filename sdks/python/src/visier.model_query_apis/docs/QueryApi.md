# visier.model_query_apis.QueryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aggregate**](QueryApi.md#aggregate) | **POST** /v1/data/query/aggregate | Query aggregate data
[**list**](QueryApi.md#list) | **POST** /v1/data/query/list | Query a list of details
[**snapshot**](QueryApi.md#snapshot) | **POST** /v1/data/query/snapshot | Query a series of detailed snapshots
[**sql_like**](QueryApi.md#sql_like) | **POST** /v1/data/query/sql | Query aggregate or list data using SQL-like syntax


# **aggregate**
> CellSetDTO aggregate(aggregation_query_execution_dto)

Query aggregate data

To retrieve aggregated values from your data in Visier, you can perform an aggregation. Usually, an aggregation  retrieves values over a period of time, such as multiple months. You can also group and filter your data in an  aggregation query to retrieve detailed information.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query_apis
from visier.model_query_apis.models.aggregation_query_execution_dto import AggregationQueryExecutionDTO
from visier.model_query_apis.models.cell_set_dto import CellSetDTO
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
    api_instance = visier.model_query_apis.QueryApi(api_client)
    aggregation_query_execution_dto = visier.model_query_apis.AggregationQueryExecutionDTO() # AggregationQueryExecutionDTO | 

    try:
        # Query aggregate data
        api_response = api_instance.aggregate(aggregation_query_execution_dto)
        print("The response of QueryApi->aggregate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueryApi->aggregate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aggregation_query_execution_dto** | [**AggregationQueryExecutionDTO**](AggregationQueryExecutionDTO.md)|  | 

### Return type

[**CellSetDTO**](CellSetDTO.md)

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

# **list**
> ListResponse list(list_query_execution_dto)

Query a list of details

To retrieve a list of values for specific objects, you can perform a list query. A list query provides information  about values for selected data points, and is not an aggregated value. In Visier's interface, a list query is  comparable to View Details for a specific data point in a visualization.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query_apis
from visier.model_query_apis.models.list_query_execution_dto import ListQueryExecutionDTO
from visier.model_query_apis.models.list_response import ListResponse
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
    api_instance = visier.model_query_apis.QueryApi(api_client)
    list_query_execution_dto = visier.model_query_apis.ListQueryExecutionDTO() # ListQueryExecutionDTO | 

    try:
        # Query a list of details
        api_response = api_instance.list(list_query_execution_dto)
        print("The response of QueryApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueryApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_query_execution_dto** | [**ListQueryExecutionDTO**](ListQueryExecutionDTO.md)|  | 

### Return type

[**ListResponse**](ListResponse.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [OAuth2Auth](../README.md#OAuth2Auth), [OAuth2Auth](../README.md#OAuth2Auth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/octet-stream, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List query response |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snapshot**
> ListResponse snapshot(snapshot_query_execution_dto)

Query a series of detailed snapshots

To retrieve a collection of `list` query-style snapshots taken at the defined intervals, execute a `snapshot` query.  Each snapshot in the result is associated with a timestamp, or the \"effective date\" at which date snapshot data was valid.  This API allows you to request a detailed time series from Visier.   Structurally, a `snapshot` query is similar to a `list` query, but has the following differences:  * The `snapshot` query may contain a column, `effectiveDateProperty`, that specifies the time for each snapshot. To include the `effectiveDateProperty` column, add the following object to the columns array:     ```json     {         \"columnName\": \"Snapshot_Date\",         \"columnDefinition\": {             \"effectiveDateProperty\": {}         }     }     ```  * The `snapshot` query uses `timeIntervals` (like an `aggregate` query) instead of `timeInterval` (like a `list` query) because the `snapshot` query     must specify the number of snapshots to generate. To specify the number of snapshots to generate, use the `intervalCount` property in the `timeIntervals` object, as shown next.     ```json     {         \"timeIntervals\": {         \"fromDateTime\": \"2022-01-01\",         \"intervalPeriodType\": \"MONTH\",         \"intervalPeriodCount\": 6,         \"intervalCount\": 4     }     ```

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query_apis
from visier.model_query_apis.models.list_response import ListResponse
from visier.model_query_apis.models.snapshot_query_execution_dto import SnapshotQueryExecutionDTO
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
    api_instance = visier.model_query_apis.QueryApi(api_client)
    snapshot_query_execution_dto = visier.model_query_apis.SnapshotQueryExecutionDTO() # SnapshotQueryExecutionDTO | 

    try:
        # Query a series of detailed snapshots
        api_response = api_instance.snapshot(snapshot_query_execution_dto)
        print("The response of QueryApi->snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueryApi->snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_query_execution_dto** | [**SnapshotQueryExecutionDTO**](SnapshotQueryExecutionDTO.md)|  | 

### Return type

[**ListResponse**](ListResponse.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [OAuth2Auth](../README.md#OAuth2Auth), [OAuth2Auth](../README.md#OAuth2Auth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/octet-stream, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List query response |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sql_like**
> CellSetDTO sql_like(sql_like_query_execution_dto)

Query aggregate or list data using SQL-like syntax

To retrieve a list of values for specific objects or aggregate values from metrics, you can write queries using SQL-like syntax.  The response format matches the query type whether aggregate or list. If requested, aggregate query results may be flattened into tabular format.    A SQL-like query is an aggregate if it contains at least one metric. Aggregate queries must specify a time interval divided into periods; for example:  ```sql  SELECT    employeeCount() AS \"Employee Count\",    level(Gender, \"Gender\") AS Gender  FROM    Employee  WHERE   Visier_Time IN periods(date(\"2023-01-01\"), 4, period(3, Month));  ```   A SQL-like query is a list if it does not contain any metrics. List queries define time intervals as simple intervals; for example:  ```sql  SELECT    EmployeeID AS \"Employee ID\",    level(Gender, \"Gender\") AS Gender  FROM    Employee  WHERE   Visier_Time BETWEEN date(\"2022-01-01\") AND date(\"2023-01-01\");  ```

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.model_query_apis
from visier.model_query_apis.models.cell_set_dto import CellSetDTO
from visier.model_query_apis.models.sql_like_query_execution_dto import SqlLikeQueryExecutionDTO
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
    api_instance = visier.model_query_apis.QueryApi(api_client)
    sql_like_query_execution_dto = visier.model_query_apis.SqlLikeQueryExecutionDTO() # SqlLikeQueryExecutionDTO | 

    try:
        # Query aggregate or list data using SQL-like syntax
        api_response = api_instance.sql_like(sql_like_query_execution_dto)
        print("The response of QueryApi->sql_like:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueryApi->sql_like: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sql_like_query_execution_dto** | [**SqlLikeQueryExecutionDTO**](SqlLikeQueryExecutionDTO.md)|  | 

### Return type

[**CellSetDTO**](CellSetDTO.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [OAuth2Auth](../README.md#OAuth2Auth), [OAuth2Auth](../README.md#OAuth2Auth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/octet-stream, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List query response |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

