# visier.api.data_version_export.DataVersionExportV1AlphaApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_file**](DataVersionExportV1AlphaApi.md#download_file) | **GET** /v1alpha/data/data-version-exports/exports/{exportUuid}/files/{fileId} | Download a file from a data version export.
[**get_available_data_versions**](DataVersionExportV1AlphaApi.md#get_available_data_versions) | **GET** /v1alpha/data/data-version-exports/data-versions | Retrieve a list of all data versions
[**get_available_exports**](DataVersionExportV1AlphaApi.md#get_available_exports) | **GET** /v1alpha/data/data-version-exports/exports | Retrieve the details of all data version exports
[**get_export**](DataVersionExportV1AlphaApi.md#get_export) | **GET** /v1alpha/data/data-version-exports/exports/{exportUuid} | Retrieve the details of a data version export.
[**get_export_job_status**](DataVersionExportV1AlphaApi.md#get_export_job_status) | **GET** /v1alpha/data/data-version-exports/jobs/{jobUuid} | Retrieve a data version export job&#39;s status
[**schedule_export_job**](DataVersionExportV1AlphaApi.md#schedule_export_job) | **POST** /v1alpha/data/data-version-exports/jobs | Schedule a data version export job


# **download_file**
> bytearray download_file(export_uuid, file_id)

Download a file from a data version export.

This API allows you to download a file from a data version export. Data version export files are in CSV format, compressed with gzip.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.data_version_export
from visier.api.data_version_export.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.data_version_export.Configuration(
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
configuration = visier.api.data_version_export.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.data_version_export.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.data_version_export.DataVersionExportV1AlphaApi(api_client)
    export_uuid = 'export_uuid_example' # str | The unique identifier of the data version export.
    file_id = 56 # int | The unique integer identifier of the file within the data version export.

    try:
        # Download a file from a data version export.
        api_response = api_instance.download_file(export_uuid, file_id)
        print("The response of DataVersionExportV1AlphaApi->download_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataVersionExportV1AlphaApi->download_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_uuid** | **str**| The unique identifier of the data version export. | 
 **file_id** | **int**| The unique integer identifier of the file within the data version export. | 

### Return type

**bytearray**

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [OAuth2Auth](../README.md#OAuth2Auth), [OAuth2Auth](../README.md#OAuth2Auth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/gzip, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File contents |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_data_versions**
> DataVersionExportDataVersionsDTO get_available_data_versions()

Retrieve a list of all data versions

This API allows you to retrieve a list of all data versions in the tenant.   **Note:** This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.data_version_export
from visier.api.data_version_export.models.data_version_export_data_versions_dto import DataVersionExportDataVersionsDTO
from visier.api.data_version_export.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.data_version_export.Configuration(
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
configuration = visier.api.data_version_export.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.data_version_export.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.data_version_export.DataVersionExportV1AlphaApi(api_client)

    try:
        # Retrieve a list of all data versions
        api_response = api_instance.get_available_data_versions()
        print("The response of DataVersionExportV1AlphaApi->get_available_data_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataVersionExportV1AlphaApi->get_available_data_versions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DataVersionExportDataVersionsDTO**](DataVersionExportDataVersionsDTO.md)

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

# **get_available_exports**
> DataVersionExportsDTO get_available_exports()

Retrieve the details of all data version exports

This API allows you to retrieve the information for all available data version exports.  **Note:** Data version exports are available for 14 days after export job completes.   **Note:** This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.data_version_export
from visier.api.data_version_export.models.data_version_exports_dto import DataVersionExportsDTO
from visier.api.data_version_export.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.data_version_export.Configuration(
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
configuration = visier.api.data_version_export.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.data_version_export.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.data_version_export.DataVersionExportV1AlphaApi(api_client)

    try:
        # Retrieve the details of all data version exports
        api_response = api_instance.get_available_exports()
        print("The response of DataVersionExportV1AlphaApi->get_available_exports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataVersionExportV1AlphaApi->get_available_exports: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DataVersionExportsDTO**](DataVersionExportsDTO.md)

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

# **get_export**
> DataVersionExportsDTO get_export(export_uuid)

Retrieve the details of a data version export.

This API allows you to retrieve information for a specific data version export.  **Note:** Data version exports are available for 14 days after export job completes.   **Note:** This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.data_version_export
from visier.api.data_version_export.models.data_version_exports_dto import DataVersionExportsDTO
from visier.api.data_version_export.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.data_version_export.Configuration(
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
configuration = visier.api.data_version_export.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.data_version_export.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.data_version_export.DataVersionExportV1AlphaApi(api_client)
    export_uuid = 'export_uuid_example' # str | The unique identifier of the data version export.

    try:
        # Retrieve the details of a data version export.
        api_response = api_instance.get_export(export_uuid)
        print("The response of DataVersionExportV1AlphaApi->get_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataVersionExportV1AlphaApi->get_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_uuid** | **str**| The unique identifier of the data version export. | 

### Return type

[**DataVersionExportsDTO**](DataVersionExportsDTO.md)

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

# **get_export_job_status**
> DataVersionExportJobStatusDTO get_export_job_status(job_uuid)

Retrieve a data version export job's status

This API allows you to retrieve the status of a data version export job. After the job completes successfully, this endpoint returns an `exportUuid` that you can use to retrieve the export information and download export files.   **Note:** This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.data_version_export
from visier.api.data_version_export.models.data_version_export_job_status_dto import DataVersionExportJobStatusDTO
from visier.api.data_version_export.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.data_version_export.Configuration(
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
configuration = visier.api.data_version_export.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.data_version_export.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.data_version_export.DataVersionExportV1AlphaApi(api_client)
    job_uuid = 'job_uuid_example' # str | The unique identifier of the data version export job.

    try:
        # Retrieve a data version export job's status
        api_response = api_instance.get_export_job_status(job_uuid)
        print("The response of DataVersionExportV1AlphaApi->get_export_job_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataVersionExportV1AlphaApi->get_export_job_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_uuid** | **str**| The unique identifier of the data version export job. | 

### Return type

[**DataVersionExportJobStatusDTO**](DataVersionExportJobStatusDTO.md)

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

# **schedule_export_job**
> DataVersionExportScheduleJobResponseDTO schedule_export_job(data_version_export_schedule_job_request_dto)

Schedule a data version export job

This API allows you to schedule a data version export job. The job schedules immediately and will begin when resources are available. The response returns a `jobUuid` that you can use to check the export job status.   **Note:** There is a limit of 10 export jobs per tenant per day.   **Note:** This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.data_version_export
from visier.api.data_version_export.models.data_version_export_schedule_job_request_dto import DataVersionExportScheduleJobRequestDTO
from visier.api.data_version_export.models.data_version_export_schedule_job_response_dto import DataVersionExportScheduleJobResponseDTO
from visier.api.data_version_export.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.data_version_export.Configuration(
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
configuration = visier.api.data_version_export.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.data_version_export.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.data_version_export.DataVersionExportV1AlphaApi(api_client)
    data_version_export_schedule_job_request_dto = visier.api.data_version_export.DataVersionExportScheduleJobRequestDTO() # DataVersionExportScheduleJobRequestDTO | 

    try:
        # Schedule a data version export job
        api_response = api_instance.schedule_export_job(data_version_export_schedule_job_request_dto)
        print("The response of DataVersionExportV1AlphaApi->schedule_export_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataVersionExportV1AlphaApi->schedule_export_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_version_export_schedule_job_request_dto** | [**DataVersionExportScheduleJobRequestDTO**](DataVersionExportScheduleJobRequestDTO.md)|  | 

### Return type

[**DataVersionExportScheduleJobResponseDTO**](DataVersionExportScheduleJobResponseDTO.md)

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

