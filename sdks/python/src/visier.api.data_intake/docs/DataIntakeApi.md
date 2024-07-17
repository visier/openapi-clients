# visier.api.data_intake.DataIntakeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_processing_jobs_by_parent_receiving_job_id**](DataIntakeApi.md#get_processing_jobs_by_parent_receiving_job_id) | **GET** /v1/op/jobs/processing-jobs/{receivingJobId} | Retrieve processing job statuses by receiving job ID
[**get_sources**](DataIntakeApi.md#get_sources) | **GET** /v1/op/data-sources | Retrieve a list of sources
[**push_data**](DataIntakeApi.md#push_data) | **PUT** /v1/op/data-transfer-sessions/{transferSessionId}/add | Transfer data to sources via JSON
[**push_data_cancel**](DataIntakeApi.md#push_data_cancel) | **PUT** /v1/op/data-transfer-sessions/{transferSessionId}/cancel | Cancel a transfer session
[**push_data_complete**](DataIntakeApi.md#push_data_complete) | **POST** /v1/op/jobs/receiving-jobs | Complete a transfer session
[**receiving_job_status**](DataIntakeApi.md#receiving_job_status) | **GET** /v1/op/jobs/receiving-jobs/{receivingJobId} | Retrieve a receiving job’s status
[**start_transfer**](DataIntakeApi.md#start_transfer) | **POST** /v1/op/data-transfer-sessions | Start a transfer session
[**upload_data**](DataIntakeApi.md#upload_data) | **PUT** /v1/op/data-transfer-sessions/{transferSessionId}/upload | Transfer data to sources via file upload


# **get_processing_jobs_by_parent_receiving_job_id**
> GetProcessingJobsResponse get_processing_jobs_by_parent_receiving_job_id(receiving_job_id, tenant_code=tenant_code, limit=limit, start=start)

Retrieve processing job statuses by receiving job ID

Use this API to retrieve a list of statuses for all processing jobs associated with the given receiving job ID.   Processing jobs deal with an individual analytic tenant's data load. A processing job is either triggered through  the UI or is one of many processing jobs spawned from a receiving job. When a processing job is triggered as part  of a set from an receiving job, it is associated to the receiving job through a Parent ID.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.data_intake
from visier.api.data_intake.models.get_processing_jobs_response import GetProcessingJobsResponse
from visier.api.data_intake.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.data_intake.Configuration(
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
configuration = visier.api.data_intake.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.data_intake.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.data_intake.DataIntakeApi(api_client)
    receiving_job_id = 'receiving_job_id_example' # str | The receiving job ID.
    tenant_code = 'tenant_code_example' # str | The tenant code of the tenant you want to retrieve the processing jobs for. Use this if you are only interested in the results for one analytic tenant. (optional)
    limit = 56 # int | The limit of processing jobs to retrieve per page. (optional)
    start = 56 # int | The index to start retrieving results from, also known as offset. The index begins at 0. (optional)

    try:
        # Retrieve processing job statuses by receiving job ID
        api_response = api_instance.get_processing_jobs_by_parent_receiving_job_id(receiving_job_id, tenant_code=tenant_code, limit=limit, start=start)
        print("The response of DataIntakeApi->get_processing_jobs_by_parent_receiving_job_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataIntakeApi->get_processing_jobs_by_parent_receiving_job_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receiving_job_id** | **str**| The receiving job ID. | 
 **tenant_code** | **str**| The tenant code of the tenant you want to retrieve the processing jobs for. Use this if you are only interested in the results for one analytic tenant. | [optional] 
 **limit** | **int**| The limit of processing jobs to retrieve per page. | [optional] 
 **start** | **int**| The index to start retrieving results from, also known as offset. The index begins at 0. | [optional] 

### Return type

[**GetProcessingJobsResponse**](GetProcessingJobsResponse.md)

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

# **get_sources**
> PushDataSourceDefinitionsDTO get_sources()

Retrieve a list of sources

Prior to transferring data to Visier, you must identify the sources you want to target. Sources store data for  the solution and are used to map data to Visier's data model.   Note: To set up sources in your tenant, contact Visier Customer Success.  This API allows you to query the list of available sources, and identify the source schema and required fields.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.data_intake
from visier.api.data_intake.models.push_data_source_definitions_dto import PushDataSourceDefinitionsDTO
from visier.api.data_intake.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.data_intake.Configuration(
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
configuration = visier.api.data_intake.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.data_intake.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.data_intake.DataIntakeApi(api_client)

    try:
        # Retrieve a list of sources
        api_response = api_instance.get_sources()
        print("The response of DataIntakeApi->get_sources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataIntakeApi->get_sources: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PushDataSourceDefinitionsDTO**](PushDataSourceDefinitionsDTO.md)

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

# **push_data**
> PushDataResponse push_data(transfer_session_id, body, source_id=source_id, sequence=sequence, tenant_code=tenant_code)

Transfer data to sources via JSON

This API allows you to transfer data to Visier in batches of records. Each request includes a batch of records  formatted as a comma separated array with the first row containing the column headers in the request body. Each  subsequent request should also include the first row as a header.   Each request transfers a batch of records to a single source. Transfer sessions may include one or more batches before completion.   Each batch is identified by a sequence number. Sequence numbers help identify any batches  that were delivered incorrectly.   Each batch is limited to the following request size:  - Batch size limit: 10 MB  - Record count limit: 300,000 rows

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.data_intake
from visier.api.data_intake.models.push_data_response import PushDataResponse
from visier.api.data_intake.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.data_intake.Configuration(
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
configuration = visier.api.data_intake.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.data_intake.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.data_intake.DataIntakeApi(api_client)
    transfer_session_id = 'transfer_session_id_example' # str | The transfer session ID returned after the data transfer session starts.
    body = 'body_example' # str | 
    source_id = 'source_id_example' # str | The unique identifier associated with the source you want to transfer data to. (optional)
    sequence = 56 # int | The unique sequence number associated with a batch of records. (optional)
    tenant_code = 'tenant_code_example' # str | The code of the tenant you want to transfer data to. For example, WFF_j1r or WFF_j1r~c7o. (optional)

    try:
        # Transfer data to sources via JSON
        api_response = api_instance.push_data(transfer_session_id, body, source_id=source_id, sequence=sequence, tenant_code=tenant_code)
        print("The response of DataIntakeApi->push_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataIntakeApi->push_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_session_id** | **str**| The transfer session ID returned after the data transfer session starts. | 
 **body** | **str**|  | 
 **source_id** | **str**| The unique identifier associated with the source you want to transfer data to. | [optional] 
 **sequence** | **int**| The unique sequence number associated with a batch of records. | [optional] 
 **tenant_code** | **str**| The code of the tenant you want to transfer data to. For example, WFF_j1r or WFF_j1r~c7o. | [optional] 

### Return type

[**PushDataResponse**](PushDataResponse.md)

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

# **push_data_cancel**
> PushDataCancelResponse push_data_cancel(transfer_session_id)

Cancel a transfer session

This API allows you to cancel a transfer session after starting it. If a transfer session is cancelled, all  records within the transfer session do not persist in Visier’s data store.   If you cancel a transfer session, please start a new transfer session and resend the complete data set.   You might cancel a transfer session if:  - A request to send a batch of records failed.  - The original set of records is incomplete.  - An infrastructure error occurs.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.data_intake
from visier.api.data_intake.models.push_data_cancel_response import PushDataCancelResponse
from visier.api.data_intake.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.data_intake.Configuration(
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
configuration = visier.api.data_intake.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.data_intake.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.data_intake.DataIntakeApi(api_client)
    transfer_session_id = 'transfer_session_id_example' # str | The transfer session ID to cancel.

    try:
        # Cancel a transfer session
        api_response = api_instance.push_data_cancel(transfer_session_id)
        print("The response of DataIntakeApi->push_data_cancel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataIntakeApi->push_data_cancel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_session_id** | **str**| The transfer session ID to cancel. | 

### Return type

[**PushDataCancelResponse**](PushDataCancelResponse.md)

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

# **push_data_complete**
> PushDataCompleteResponse push_data_complete(push_data_complete_request)

Complete a transfer session

This API allows you to complete the specified transfer session by triggering a receiving job. A receiving job  validates the transferred data and adds the transferred data to Visier’s data store.   You can set an optional parameter to generate a data version through a processing job immediately after the receiving job completes.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.data_intake
from visier.api.data_intake.models.push_data_complete_request import PushDataCompleteRequest
from visier.api.data_intake.models.push_data_complete_response import PushDataCompleteResponse
from visier.api.data_intake.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.data_intake.Configuration(
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
configuration = visier.api.data_intake.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.data_intake.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.data_intake.DataIntakeApi(api_client)
    push_data_complete_request = visier.api.data_intake.PushDataCompleteRequest() # PushDataCompleteRequest | 

    try:
        # Complete a transfer session
        api_response = api_instance.push_data_complete(push_data_complete_request)
        print("The response of DataIntakeApi->push_data_complete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataIntakeApi->push_data_complete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **push_data_complete_request** | [**PushDataCompleteRequest**](PushDataCompleteRequest.md)|  | 

### Return type

[**PushDataCompleteResponse**](PushDataCompleteResponse.md)

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

# **receiving_job_status**
> ReceivingJobStatusResponse receiving_job_status(receiving_job_id, jobs=jobs, tenant_code=tenant_code, start=start, limit=limit)

Retrieve a receiving job’s status

After completing a transfer session, you may want to know the status of the receiving job and the associated tenant  receiving jobs. A receiving job validates the transferred data and adds the transferred data to Visier’s data store.   Use this API to retrieve the receiving job status and summary of analytic tenant receiving jobs.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.data_intake
from visier.api.data_intake.models.receiving_job_status_response import ReceivingJobStatusResponse
from visier.api.data_intake.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.data_intake.Configuration(
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
configuration = visier.api.data_intake.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.data_intake.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.data_intake.DataIntakeApi(api_client)
    receiving_job_id = 'receiving_job_id_example' # str | The **dataReceivingJobId** provided after a data transfer session completes. See **`/v1/op/jobs/receiving-jobs`**.
    jobs = True # bool | If true, returns the status of receiving jobs spawned by the receiving job specified by receivingJobId. (optional)
    tenant_code = 'tenant_code_example' # str | The tenant code of the tenant you want to retrieve the receiving jobs for. Use this if you are only interested in the results for one analytic tenant. (optional)
    start = 56 # int | The index to start retrieving results from, also known as offset. The index begins at 0. (optional)
    limit = 56 # int | The number of job statuses to return per page. (optional)

    try:
        # Retrieve a receiving job’s status
        api_response = api_instance.receiving_job_status(receiving_job_id, jobs=jobs, tenant_code=tenant_code, start=start, limit=limit)
        print("The response of DataIntakeApi->receiving_job_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataIntakeApi->receiving_job_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receiving_job_id** | **str**| The **dataReceivingJobId** provided after a data transfer session completes. See **&#x60;/v1/op/jobs/receiving-jobs&#x60;**. | 
 **jobs** | **bool**| If true, returns the status of receiving jobs spawned by the receiving job specified by receivingJobId. | [optional] 
 **tenant_code** | **str**| The tenant code of the tenant you want to retrieve the receiving jobs for. Use this if you are only interested in the results for one analytic tenant. | [optional] 
 **start** | **int**| The index to start retrieving results from, also known as offset. The index begins at 0. | [optional] 
 **limit** | **int**| The number of job statuses to return per page. | [optional] 

### Return type

[**ReceivingJobStatusResponse**](ReceivingJobStatusResponse.md)

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

# **start_transfer**
> StartTransferResponse start_transfer()

Start a transfer session

Use this API to start a new transfer session. A transfer session can include one or more batches of records to be  sent to Visier. Batches of records may be transferred as JSON or file payloads.   Recommended: For optimal performance, please include all batches of records in a single transfer session.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.data_intake
from visier.api.data_intake.models.start_transfer_response import StartTransferResponse
from visier.api.data_intake.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.data_intake.Configuration(
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
configuration = visier.api.data_intake.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.data_intake.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.data_intake.DataIntakeApi(api_client)

    try:
        # Start a transfer session
        api_response = api_instance.start_transfer()
        print("The response of DataIntakeApi->start_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataIntakeApi->start_transfer: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**StartTransferResponse**](StartTransferResponse.md)

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

# **upload_data**
> PushDataResponse upload_data(transfer_session_id, source_id=source_id, sequence=sequence, tenant_code=tenant_code)

Transfer data to sources via file upload

This API allows you to upload data to Visier as CSV or ZIP files. Each request transfers a single file. If the  data intended for Visier is stored in multiple files, you may compress them into a single ZIP file or make  multiple requests within the same transfer session.   File size limit: 3 GB   Each file is identified by a sequence number. Sequence numbers help identify any batches that were delivered incorrectly.   If you define a specific source in the request, all files within the request will target the declared source. If  a source is not defined, the filenames are matched against the source regex to correctly assign each file to a  source. To find out the source regex, please contact Visier Customer Success.   Note: If you include files that should target multiple sources in one ZIP file, do not define a source in the request.   Analytic tenants: For optimal transfer speed, provide one ZIP file per source.  Administrating tenants: For optimal transfer speed, provide one ZIP file containing all the required data files for your analytic tenants.  In the ZIP file, use one folder per analytic tenant. The ZIP file must adhere to the following file structure:   File1.zip  - Folder1: WFF_tenantCode1     - Filename1.csv     - Filename2.csv  - Folder2: WFF_tenantCode2     - Filename3.csv     - Filename4.csv

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.data_intake
from visier.api.data_intake.models.push_data_response import PushDataResponse
from visier.api.data_intake.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.data_intake.Configuration(
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
configuration = visier.api.data_intake.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.data_intake.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.data_intake.DataIntakeApi(api_client)
    transfer_session_id = 'transfer_session_id_example' # str | The transfer session ID returned after the data transfer session starts.
    source_id = 'source_id_example' # str | The unique identifier associated with the source you want to transfer data to. (optional)
    sequence = 'sequence_example' # str | The unique sequence number associated with a batch of records. (optional)
    tenant_code = 'tenant_code_example' # str | The code of the tenant you want to transfer data to. For example, WFF_j1r or WFF_j1r~c7o. (optional)

    try:
        # Transfer data to sources via file upload
        api_response = api_instance.upload_data(transfer_session_id, source_id=source_id, sequence=sequence, tenant_code=tenant_code)
        print("The response of DataIntakeApi->upload_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataIntakeApi->upload_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_session_id** | **str**| The transfer session ID returned after the data transfer session starts. | 
 **source_id** | **str**| The unique identifier associated with the source you want to transfer data to. | [optional] 
 **sequence** | **str**| The unique sequence number associated with a batch of records. | [optional] 
 **tenant_code** | **str**| The code of the tenant you want to transfer data to. For example, WFF_j1r or WFF_j1r~c7o. | [optional] 

### Return type

[**PushDataResponse**](PushDataResponse.md)

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

