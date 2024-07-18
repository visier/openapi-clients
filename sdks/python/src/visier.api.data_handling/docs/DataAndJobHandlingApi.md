# visier.api.data_handling.DataAndJobHandlingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_connector_credential**](DataAndJobHandlingApi.md#assign_connector_credential) | **POST** /v1/op/data-connectors/assignCredentials | Assign connector credentials to data connectors
[**cancel_jobs**](DataAndJobHandlingApi.md#cancel_jobs) | **POST** /v1/op/jobs/cancel | Cancel a list of jobs
[**create_connector_credential**](DataAndJobHandlingApi.md#create_connector_credential) | **POST** /v1/op/data-connector-credentials | Create a connector credential
[**data_connector_credentials**](DataAndJobHandlingApi.md#data_connector_credentials) | **GET** /v1/op/data-connector-credentials | Retrieve a list of all data connector credentials
[**data_connectors**](DataAndJobHandlingApi.md#data_connectors) | **GET** /v1/op/data-connectors | Retrieve a list of all data connectors
[**delete_connector_credential**](DataAndJobHandlingApi.md#delete_connector_credential) | **DELETE** /v1/op/data-connector-credentials/{id} | Delete a connector credential
[**disable_dv**](DataAndJobHandlingApi.md#disable_dv) | **PUT** /v1/op/data-versions/disable | Disable data versions for a list of analytic tenants
[**dispatching_job_status**](DataAndJobHandlingApi.md#dispatching_job_status) | **GET** /v1/op/jobs/dispatching-jobs/{jobId} | Retrieve a dispatching job&#39;s status
[**exclude_data_uplaods**](DataAndJobHandlingApi.md#exclude_data_uplaods) | **PUT** /v1/op/data/uploads/exclude | Exclude data uploads
[**extraction_job_and_status**](DataAndJobHandlingApi.md#extraction_job_and_status) | **GET** /v1/op/jobs/dispatching-jobs/{jobId}/extraction-jobs | Retrieve a dispatching job&#39;s extraction jobs with their statuses
[**include_data_uploads**](DataAndJobHandlingApi.md#include_data_uploads) | **PUT** /v1/op/data/uploads/include | Include data uploads
[**job_id_status**](DataAndJobHandlingApi.md#job_id_status) | **GET** /v1/op/job-status/jobs/{jobId} | Retrieve a specific job&#39;s status
[**job_status**](DataAndJobHandlingApi.md#job_status) | **GET** /v1/op/job-status/jobs | Retrieve the statuses of all jobs
[**latest_enabled_dv**](DataAndJobHandlingApi.md#latest_enabled_dv) | **GET** /v1/op/data-versions | Retrieve the latest enabled data versions for all analytic tenants
[**processing_job_and_status**](DataAndJobHandlingApi.md#processing_job_and_status) | **GET** /v1/op/jobs/dispatching-jobs/{jobId}/processing-jobs | Retrieve a dispatching job&#39;s processing jobs with their statuses
[**processing_job_status**](DataAndJobHandlingApi.md#processing_job_status) | **GET** /v1/op/jobs/processing-jobs/{receivingJobId} | Retrieve processing job statuses by receiving job ID
[**receiving_job_and_status**](DataAndJobHandlingApi.md#receiving_job_and_status) | **GET** /v1/op/jobs/dispatching-jobs/{jobId}/receiving-jobs | Retrieve a dispatching job&#39;s receiving jobs with their statuses
[**receiving_job_status**](DataAndJobHandlingApi.md#receiving_job_status) | **GET** /v1/op/jobs/receiving-jobs/{receivingJobId} | Retrieve a receiving job&#39;s status
[**retrieve_data_categories**](DataAndJobHandlingApi.md#retrieve_data_categories) | **GET** /v1/op/data/categories | Retrieve a list of all data categories
[**retrieve_data_uploads**](DataAndJobHandlingApi.md#retrieve_data_uploads) | **GET** /v1/op/data/uploads | Retrieve data uploads
[**start_extraction**](DataAndJobHandlingApi.md#start_extraction) | **POST** /v1/op/data/startExtractAndLoad | Trigger extraction jobs
[**start_load**](DataAndJobHandlingApi.md#start_load) | **POST** /v1/op/data/startload | Start the data load for an analytic tenant


# **assign_connector_credential**
> AssignConnectorCredentialsResponseDTO assign_connector_credential(assign_connector_credential_request)

Assign connector credentials to data connectors

This API allows you to assign a connector credential to a data connector.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.data_handling
from visier.api.data_handling.models.assign_connector_credential_request import AssignConnectorCredentialRequest
from visier.api.data_handling.models.assign_connector_credentials_response_dto import AssignConnectorCredentialsResponseDTO
from visier.api.data_handling.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.data_handling.Configuration(
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
configuration = visier.api.data_handling.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.data_handling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.data_handling.DataAndJobHandlingApi(api_client)
    assign_connector_credential_request = visier.api.data_handling.AssignConnectorCredentialRequest() # AssignConnectorCredentialRequest | 

    try:
        # Assign connector credentials to data connectors
        api_response = api_instance.assign_connector_credential(assign_connector_credential_request)
        print("The response of DataAndJobHandlingApi->assign_connector_credential:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataAndJobHandlingApi->assign_connector_credential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assign_connector_credential_request** | [**AssignConnectorCredentialRequest**](AssignConnectorCredentialRequest.md)|  | 

### Return type

[**AssignConnectorCredentialsResponseDTO**](AssignConnectorCredentialsResponseDTO.md)

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

# **cancel_jobs**
> JobCancellationResultsDTO cancel_jobs(cancel_job_batch_from_job_id_dto)

Cancel a list of jobs

Use this API to cancel a list of processing jobs, upload jobs, receiving jobs, and extraction jobs.   Note: Receiving jobs with the Running status cannot be cancelled.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.data_handling
from visier.api.data_handling.models.cancel_job_batch_from_job_id_dto import CancelJobBatchFromJobIdDTO
from visier.api.data_handling.models.job_cancellation_results_dto import JobCancellationResultsDTO
from visier.api.data_handling.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.data_handling.Configuration(
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
configuration = visier.api.data_handling.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.data_handling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.data_handling.DataAndJobHandlingApi(api_client)
    cancel_job_batch_from_job_id_dto = visier.api.data_handling.CancelJobBatchFromJobIdDTO() # CancelJobBatchFromJobIdDTO | 

    try:
        # Cancel a list of jobs
        api_response = api_instance.cancel_jobs(cancel_job_batch_from_job_id_dto)
        print("The response of DataAndJobHandlingApi->cancel_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataAndJobHandlingApi->cancel_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cancel_job_batch_from_job_id_dto** | [**CancelJobBatchFromJobIdDTO**](CancelJobBatchFromJobIdDTO.md)|  | 

### Return type

[**JobCancellationResultsDTO**](JobCancellationResultsDTO.md)

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

# **create_connector_credential**
> CredentialCreationAPIResponseDTO create_connector_credential(data_provider_auth_information_dto, tenant_code=tenant_code)

Create a connector credential

Use this API to create connector credentials for a specified tenant. Connector credentials allow Visier to  retrieve data from your source systems through an integration user in the source system.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.data_handling
from visier.api.data_handling.models.credential_creation_api_response_dto import CredentialCreationAPIResponseDTO
from visier.api.data_handling.models.data_provider_auth_information_dto import DataProviderAuthInformationDTO
from visier.api.data_handling.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.data_handling.Configuration(
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
configuration = visier.api.data_handling.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.data_handling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.data_handling.DataAndJobHandlingApi(api_client)
    data_provider_auth_information_dto = visier.api.data_handling.DataProviderAuthInformationDTO() # DataProviderAuthInformationDTO | 
    tenant_code = 'tenant_code_example' # str | The tenant code of a specific analytic tenant that you want to create the credential for. (optional)

    try:
        # Create a connector credential
        api_response = api_instance.create_connector_credential(data_provider_auth_information_dto, tenant_code=tenant_code)
        print("The response of DataAndJobHandlingApi->create_connector_credential:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataAndJobHandlingApi->create_connector_credential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_provider_auth_information_dto** | [**DataProviderAuthInformationDTO**](DataProviderAuthInformationDTO.md)|  | 
 **tenant_code** | **str**| The tenant code of a specific analytic tenant that you want to create the credential for. | [optional] 

### Return type

[**CredentialCreationAPIResponseDTO**](CredentialCreationAPIResponseDTO.md)

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

# **data_connector_credentials**
> ExtractorCredentialsAPIDTO data_connector_credentials(tenant_code=tenant_code, limit=limit, start=start)

Retrieve a list of all data connector credentials

Use this API to retrieve a list of the connector credentials in a specified tenant. Connector credentials allow  Visier to retrieve data from your source systems through an integration user in the source system.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.data_handling
from visier.api.data_handling.models.extractor_credentials_apidto import ExtractorCredentialsAPIDTO
from visier.api.data_handling.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.data_handling.Configuration(
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
configuration = visier.api.data_handling.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.data_handling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.data_handling.DataAndJobHandlingApi(api_client)
    tenant_code = 'tenant_code_example' # str | The tenant code of a specific analytic tenant that you want to retrieve for. (optional)
    limit = 56 # int | The limit to retrieve. (optional)
    start = 56 # int | The index to start retrieving results from, also known as offset. The index begins at 0. (optional)

    try:
        # Retrieve a list of all data connector credentials
        api_response = api_instance.data_connector_credentials(tenant_code=tenant_code, limit=limit, start=start)
        print("The response of DataAndJobHandlingApi->data_connector_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataAndJobHandlingApi->data_connector_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_code** | **str**| The tenant code of a specific analytic tenant that you want to retrieve for. | [optional] 
 **limit** | **int**| The limit to retrieve. | [optional] 
 **start** | **int**| The index to start retrieving results from, also known as offset. The index begins at 0. | [optional] 

### Return type

[**ExtractorCredentialsAPIDTO**](ExtractorCredentialsAPIDTO.md)

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

# **data_connectors**
> ImportDefinitionsAPIDTO data_connectors(tenant_code=tenant_code, limit=limit, start=start)

Retrieve a list of all data connectors

Use this API to retrieve a list of the data connectors in a specified tenant. Data connectors are an alternative  to generating flat files and transferring them to Visier via SFTP.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.data_handling
from visier.api.data_handling.models.import_definitions_apidto import ImportDefinitionsAPIDTO
from visier.api.data_handling.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.data_handling.Configuration(
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
configuration = visier.api.data_handling.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.data_handling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.data_handling.DataAndJobHandlingApi(api_client)
    tenant_code = 'tenant_code_example' # str | The tenant code of a specific analytic tenant that you want to retrieve for. (optional)
    limit = 56 # int | The limit to retrieve. (optional)
    start = 56 # int | The index to start retrieving results from, also known as offset. The index begins at 0. (optional)

    try:
        # Retrieve a list of all data connectors
        api_response = api_instance.data_connectors(tenant_code=tenant_code, limit=limit, start=start)
        print("The response of DataAndJobHandlingApi->data_connectors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataAndJobHandlingApi->data_connectors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_code** | **str**| The tenant code of a specific analytic tenant that you want to retrieve for. | [optional] 
 **limit** | **int**| The limit to retrieve. | [optional] 
 **start** | **int**| The index to start retrieving results from, also known as offset. The index begins at 0. | [optional] 

### Return type

[**ImportDefinitionsAPIDTO**](ImportDefinitionsAPIDTO.md)

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

# **delete_connector_credential**
> str delete_connector_credential(id, tenant_code=tenant_code)

Delete a connector credential

Use this API to delete connector credentials from your tenants. Credentials that are no longer valid  should be deleted.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.data_handling
from visier.api.data_handling.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.data_handling.Configuration(
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
configuration = visier.api.data_handling.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.data_handling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.data_handling.DataAndJobHandlingApi(api_client)
    id = 'id_example' # str | The credentialId of the credential you want to delete.
    tenant_code = 'tenant_code_example' # str | The tenant code of the analytic tenant in which the credential you're deleting. (optional)

    try:
        # Delete a connector credential
        api_response = api_instance.delete_connector_credential(id, tenant_code=tenant_code)
        print("The response of DataAndJobHandlingApi->delete_connector_credential:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataAndJobHandlingApi->delete_connector_credential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The credentialId of the credential you want to delete. | 
 **tenant_code** | **str**| The tenant code of the analytic tenant in which the credential you&#39;re deleting. | [optional] 

### Return type

**str**

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

# **disable_dv**
> DisableDVResponse disable_dv(disable_dv_request)

Disable data versions for a list of analytic tenants

If you discover that a data version is not what is expected after running metric value validation on a data load,  you may want to disable the data version for that processing job.   Use this API to disable the latest enabled data versions for affected analytic tenants or to disable a particular  data version for each analytic tenant.   Note: Disabling an older data version may not have an effect on the state of the solution.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.data_handling
from visier.api.data_handling.models.disable_dv_request import DisableDVRequest
from visier.api.data_handling.models.disable_dv_response import DisableDVResponse
from visier.api.data_handling.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.data_handling.Configuration(
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
configuration = visier.api.data_handling.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.data_handling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.data_handling.DataAndJobHandlingApi(api_client)
    disable_dv_request = visier.api.data_handling.DisableDVRequest() # DisableDVRequest | 

    try:
        # Disable data versions for a list of analytic tenants
        api_response = api_instance.disable_dv(disable_dv_request)
        print("The response of DataAndJobHandlingApi->disable_dv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataAndJobHandlingApi->disable_dv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disable_dv_request** | [**DisableDVRequest**](DisableDVRequest.md)|  | 

### Return type

[**DisableDVResponse**](DisableDVResponse.md)

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

# **dispatching_job_status**
> DispatchingJobStatusResponse dispatching_job_status(job_id)

Retrieve a dispatching job's status

Use this API to retrieve the status of a dispatching job, including its job ID and the number of jobs it generated.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.data_handling
from visier.api.data_handling.models.dispatching_job_status_response import DispatchingJobStatusResponse
from visier.api.data_handling.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.data_handling.Configuration(
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
configuration = visier.api.data_handling.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.data_handling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.data_handling.DataAndJobHandlingApi(api_client)
    job_id = 'job_id_example' # str | The ID of the job you want to retrieve.

    try:
        # Retrieve a dispatching job's status
        api_response = api_instance.dispatching_job_status(job_id)
        print("The response of DataAndJobHandlingApi->dispatching_job_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataAndJobHandlingApi->dispatching_job_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The ID of the job you want to retrieve. | 

### Return type

[**DispatchingJobStatusResponse**](DispatchingJobStatusResponse.md)

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

# **exclude_data_uplaods**
> TenantDataUploadsUpdateResponseDTO exclude_data_uplaods(exclude_data_uploads_request)

Exclude data uploads

Use this API to exclude either a specified list of data uploads or all data uploads for each analytic tenant.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.data_handling
from visier.api.data_handling.models.exclude_data_uploads_request import ExcludeDataUploadsRequest
from visier.api.data_handling.models.tenant_data_uploads_update_response_dto import TenantDataUploadsUpdateResponseDTO
from visier.api.data_handling.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.data_handling.Configuration(
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
configuration = visier.api.data_handling.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.data_handling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.data_handling.DataAndJobHandlingApi(api_client)
    exclude_data_uploads_request = visier.api.data_handling.ExcludeDataUploadsRequest() # ExcludeDataUploadsRequest | 

    try:
        # Exclude data uploads
        api_response = api_instance.exclude_data_uplaods(exclude_data_uploads_request)
        print("The response of DataAndJobHandlingApi->exclude_data_uplaods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataAndJobHandlingApi->exclude_data_uplaods: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exclude_data_uploads_request** | [**ExcludeDataUploadsRequest**](ExcludeDataUploadsRequest.md)|  | 

### Return type

[**TenantDataUploadsUpdateResponseDTO**](TenantDataUploadsUpdateResponseDTO.md)

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

# **extraction_job_and_status**
> ExtractionJobAndStatusResponse extraction_job_and_status(job_id, dispatching_job_id=dispatching_job_id, tenant_code=tenant_code, limit=limit, start=start)

Retrieve a dispatching job's extraction jobs with their statuses

Use this API to retrieve the statuses of extraction jobs associated with a dispatching job. The dispatching job  is a \"parent\" to extraction jobs, which retrieve data from your source systems through data connectors.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.data_handling
from visier.api.data_handling.models.extraction_job_and_status_response import ExtractionJobAndStatusResponse
from visier.api.data_handling.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.data_handling.Configuration(
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
configuration = visier.api.data_handling.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.data_handling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.data_handling.DataAndJobHandlingApi(api_client)
    job_id = 'job_id_example' # str | The ID of the dispatching job you want to retrieve.
    dispatching_job_id = 'dispatching_job_id_example' # str | The ID of the dispatching job that generated the extraction jobs. (optional)
    tenant_code = 'tenant_code_example' # str | The tenant code of a specific analytic tenant that you want to retrieve the extraction job status for.  Use this if you are only interested in the results for one analytic tenant. (optional)
    limit = 56 # int | The limit of extraction job statuses to retrieve. (optional)
    start = 56 # int | The index to start retrieving results from, also known as offset. The index begins at 0. (optional)

    try:
        # Retrieve a dispatching job's extraction jobs with their statuses
        api_response = api_instance.extraction_job_and_status(job_id, dispatching_job_id=dispatching_job_id, tenant_code=tenant_code, limit=limit, start=start)
        print("The response of DataAndJobHandlingApi->extraction_job_and_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataAndJobHandlingApi->extraction_job_and_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The ID of the dispatching job you want to retrieve. | 
 **dispatching_job_id** | **str**| The ID of the dispatching job that generated the extraction jobs. | [optional] 
 **tenant_code** | **str**| The tenant code of a specific analytic tenant that you want to retrieve the extraction job status for.  Use this if you are only interested in the results for one analytic tenant. | [optional] 
 **limit** | **int**| The limit of extraction job statuses to retrieve. | [optional] 
 **start** | **int**| The index to start retrieving results from, also known as offset. The index begins at 0. | [optional] 

### Return type

[**ExtractionJobAndStatusResponse**](ExtractionJobAndStatusResponse.md)

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

# **include_data_uploads**
> TenantDataUploadsUpdateResponseDTO include_data_uploads(include_data_uploads_request)

Include data uploads

Use this API to include either the specified list of data uploads or all data uploads for each analytic tenant.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.data_handling
from visier.api.data_handling.models.include_data_uploads_request import IncludeDataUploadsRequest
from visier.api.data_handling.models.tenant_data_uploads_update_response_dto import TenantDataUploadsUpdateResponseDTO
from visier.api.data_handling.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.data_handling.Configuration(
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
configuration = visier.api.data_handling.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.data_handling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.data_handling.DataAndJobHandlingApi(api_client)
    include_data_uploads_request = visier.api.data_handling.IncludeDataUploadsRequest() # IncludeDataUploadsRequest | 

    try:
        # Include data uploads
        api_response = api_instance.include_data_uploads(include_data_uploads_request)
        print("The response of DataAndJobHandlingApi->include_data_uploads:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataAndJobHandlingApi->include_data_uploads: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_data_uploads_request** | [**IncludeDataUploadsRequest**](IncludeDataUploadsRequest.md)|  | 

### Return type

[**TenantDataUploadsUpdateResponseDTO**](TenantDataUploadsUpdateResponseDTO.md)

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

# **job_id_status**
> ReceivingJobStatusResponse job_id_status(job_id)

Retrieve a specific job's status

Use this API to retrieve the list of statuses for a specific job with id `jobId`.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.data_handling
from visier.api.data_handling.models.receiving_job_status_response import ReceivingJobStatusResponse
from visier.api.data_handling.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.data_handling.Configuration(
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
configuration = visier.api.data_handling.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.data_handling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.data_handling.DataAndJobHandlingApi(api_client)
    job_id = 'job_id_example' # str | The unique ID of the job to retrieve the status for.

    try:
        # Retrieve a specific job's status
        api_response = api_instance.job_id_status(job_id)
        print("The response of DataAndJobHandlingApi->job_id_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataAndJobHandlingApi->job_id_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The unique ID of the job to retrieve the status for. | 

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

# **job_status**
> ReceivingJobStatusResponse job_status(start_time=start_time, end_time=end_time, status=status)

Retrieve the statuses of all jobs

Use this API to retrieve the list of statuses for all jobs.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.data_handling
from visier.api.data_handling.models.receiving_job_status_response import ReceivingJobStatusResponse
from visier.api.data_handling.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.data_handling.Configuration(
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
configuration = visier.api.data_handling.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.data_handling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.data_handling.DataAndJobHandlingApi(api_client)
    start_time = 'start_time_example' # str | The start time from which to retrieve job statuses. (optional)
    end_time = 'end_time_example' # str | The end time from which to retrieve job statuses. (optional)
    status = 'status_example' # str | The specific status to restrict the list of job to. (optional)

    try:
        # Retrieve the statuses of all jobs
        api_response = api_instance.job_status(start_time=start_time, end_time=end_time, status=status)
        print("The response of DataAndJobHandlingApi->job_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataAndJobHandlingApi->job_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **str**| The start time from which to retrieve job statuses. | [optional] 
 **end_time** | **str**| The end time from which to retrieve job statuses. | [optional] 
 **status** | **str**| The specific status to restrict the list of job to. | [optional] 

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

# **latest_enabled_dv**
> MultipleTenantDataVersionsListDTO latest_enabled_dv(tenant_code=tenant_code, limit=limit, start=start, number_of_versions=number_of_versions)

Retrieve the latest enabled data versions for all analytic tenants

If you discover any inconsistencies after running metric value validation, you may want to find the data versions  causing inconsistencies so you can later disable them.   Use this API to retrieve up to five (5) of the latest enabled data versions for all your analytic tenants or a  single specified analytic tenant.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.data_handling
from visier.api.data_handling.models.multiple_tenant_data_versions_list_dto import MultipleTenantDataVersionsListDTO
from visier.api.data_handling.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.data_handling.Configuration(
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
configuration = visier.api.data_handling.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.data_handling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.data_handling.DataAndJobHandlingApi(api_client)
    tenant_code = 'tenant_code_example' # str | The tenant code of a specific analytic tenant that you want to retrieve data versions for.  Use this if you are only interested in the results for one analytic tenant. (optional)
    limit = 56 # int | The limit of analytic tenants to retrieve data versions for.  This parameter is not used if the tenantCode parameter is specified. (optional)
    start = 56 # int | The index to start retrieving results from, also known as offset. The index begins at 0. (optional)
    number_of_versions = 56 # int | The number of latest enabled data versions to retrieve. The maximum value is 5. (optional)

    try:
        # Retrieve the latest enabled data versions for all analytic tenants
        api_response = api_instance.latest_enabled_dv(tenant_code=tenant_code, limit=limit, start=start, number_of_versions=number_of_versions)
        print("The response of DataAndJobHandlingApi->latest_enabled_dv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataAndJobHandlingApi->latest_enabled_dv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_code** | **str**| The tenant code of a specific analytic tenant that you want to retrieve data versions for.  Use this if you are only interested in the results for one analytic tenant. | [optional] 
 **limit** | **int**| The limit of analytic tenants to retrieve data versions for.  This parameter is not used if the tenantCode parameter is specified. | [optional] 
 **start** | **int**| The index to start retrieving results from, also known as offset. The index begins at 0. | [optional] 
 **number_of_versions** | **int**| The number of latest enabled data versions to retrieve. The maximum value is 5. | [optional] 

### Return type

[**MultipleTenantDataVersionsListDTO**](MultipleTenantDataVersionsListDTO.md)

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

# **processing_job_and_status**
> ProcessingJobAndStatusResponse processing_job_and_status(job_id, dispatching_job_id=dispatching_job_id, tenant_code=tenant_code, limit=limit, start=start)

Retrieve a dispatching job's processing jobs with their statuses

Use this API to retrieve the statuses of processing jobs associated with a dispatching job. The dispatching job  is a \"parent\" to extraction jobs, which in turn generate processing jobs and receiving jobs.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.data_handling
from visier.api.data_handling.models.processing_job_and_status_response import ProcessingJobAndStatusResponse
from visier.api.data_handling.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.data_handling.Configuration(
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
configuration = visier.api.data_handling.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.data_handling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.data_handling.DataAndJobHandlingApi(api_client)
    job_id = 'job_id_example' # str | The ID of the dispatching job you want to retrieve.
    dispatching_job_id = 'dispatching_job_id_example' # str | The ID of the dispatching job that generated the extraction jobs. (optional)
    tenant_code = 'tenant_code_example' # str | The tenant code of a specific analytic tenant that you want to retrieve the extraction job status for.  Use this if you are only interested in the results for one analytic tenant. (optional)
    limit = 56 # int | The limit of extraction job statuses to retrieve. (optional)
    start = 56 # int | The index to start retrieving results from, also known as offset. The index begins at 0. (optional)

    try:
        # Retrieve a dispatching job's processing jobs with their statuses
        api_response = api_instance.processing_job_and_status(job_id, dispatching_job_id=dispatching_job_id, tenant_code=tenant_code, limit=limit, start=start)
        print("The response of DataAndJobHandlingApi->processing_job_and_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataAndJobHandlingApi->processing_job_and_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The ID of the dispatching job you want to retrieve. | 
 **dispatching_job_id** | **str**| The ID of the dispatching job that generated the extraction jobs. | [optional] 
 **tenant_code** | **str**| The tenant code of a specific analytic tenant that you want to retrieve the extraction job status for.  Use this if you are only interested in the results for one analytic tenant. | [optional] 
 **limit** | **int**| The limit of extraction job statuses to retrieve. | [optional] 
 **start** | **int**| The index to start retrieving results from, also known as offset. The index begins at 0. | [optional] 

### Return type

[**ProcessingJobAndStatusResponse**](ProcessingJobAndStatusResponse.md)

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

# **processing_job_status**
> ProcessingJobStatusResponse processing_job_status(receiving_job_id, tenant_code=tenant_code, limit=limit, start=start)

Retrieve processing job statuses by receiving job ID

Use this API to retrieve a list of statuses for all processing jobs associated with the given receiving job ID.  Processing jobs deal with an individual analytic tenant's data load. A processing job is either triggered through  the UI or is one of many processing jobs spawned from a receiving job. When a processing job is triggered as part  of a set from an receiving job, it is associated to the receiving job through a Parent ID.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.data_handling
from visier.api.data_handling.models.processing_job_status_response import ProcessingJobStatusResponse
from visier.api.data_handling.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.data_handling.Configuration(
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
configuration = visier.api.data_handling.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.data_handling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.data_handling.DataAndJobHandlingApi(api_client)
    receiving_job_id = 'receiving_job_id_example' # str | The receiving job ID
    tenant_code = 'tenant_code_example' # str | The tenant code of the tenant you want to retrieve the processing jobs for.  Use this if you are only interested in the results for one analytic tenant. (optional)
    limit = 56 # int | The limit of processing jobs to retrieve per page. (optional)
    start = 56 # int | The index to start retrieving results from, also known as offset. The index begins at 0. (optional)

    try:
        # Retrieve processing job statuses by receiving job ID
        api_response = api_instance.processing_job_status(receiving_job_id, tenant_code=tenant_code, limit=limit, start=start)
        print("The response of DataAndJobHandlingApi->processing_job_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataAndJobHandlingApi->processing_job_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receiving_job_id** | **str**| The receiving job ID | 
 **tenant_code** | **str**| The tenant code of the tenant you want to retrieve the processing jobs for.  Use this if you are only interested in the results for one analytic tenant. | [optional] 
 **limit** | **int**| The limit of processing jobs to retrieve per page. | [optional] 
 **start** | **int**| The index to start retrieving results from, also known as offset. The index begins at 0. | [optional] 

### Return type

[**ProcessingJobStatusResponse**](ProcessingJobStatusResponse.md)

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

# **receiving_job_and_status**
> ReceivingJobAndStatusResponse receiving_job_and_status(job_id, dispatching_job_id=dispatching_job_id, tenant_code=tenant_code, limit=limit, start=start)

Retrieve a dispatching job's receiving jobs with their statuses

Use this API to retrieve the statuses of receiving jobs associated with a dispatching job. The dispatching job  is a \"parent\" to extraction jobs, which in turn generate processing jobs and receiving jobs.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.data_handling
from visier.api.data_handling.models.receiving_job_and_status_response import ReceivingJobAndStatusResponse
from visier.api.data_handling.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.data_handling.Configuration(
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
configuration = visier.api.data_handling.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.data_handling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.data_handling.DataAndJobHandlingApi(api_client)
    job_id = 'job_id_example' # str | The ID of the dispatching job you want to retrieve.
    dispatching_job_id = 'dispatching_job_id_example' # str | The ID of the dispatching job that generated the extraction jobs. (optional)
    tenant_code = 'tenant_code_example' # str | The tenant code of a specific analytic tenant that you want to retrieve the extraction job status for.  Use this if you are only interested in the results for one analytic tenant. (optional)
    limit = 56 # int | The limit of extraction job statuses to retrieve. (optional)
    start = 56 # int | The index to start retrieving results from, also known as offset. The index begins at 0. (optional)

    try:
        # Retrieve a dispatching job's receiving jobs with their statuses
        api_response = api_instance.receiving_job_and_status(job_id, dispatching_job_id=dispatching_job_id, tenant_code=tenant_code, limit=limit, start=start)
        print("The response of DataAndJobHandlingApi->receiving_job_and_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataAndJobHandlingApi->receiving_job_and_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The ID of the dispatching job you want to retrieve. | 
 **dispatching_job_id** | **str**| The ID of the dispatching job that generated the extraction jobs. | [optional] 
 **tenant_code** | **str**| The tenant code of a specific analytic tenant that you want to retrieve the extraction job status for.  Use this if you are only interested in the results for one analytic tenant. | [optional] 
 **limit** | **int**| The limit of extraction job statuses to retrieve. | [optional] 
 **start** | **int**| The index to start retrieving results from, also known as offset. The index begins at 0. | [optional] 

### Return type

[**ReceivingJobAndStatusResponse**](ReceivingJobAndStatusResponse.md)

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

# **receiving_job_status**
> ReceivingJobStatusResponse receiving_job_status(receiving_job_id, jobs=jobs, tenant_code=tenant_code, start=start, limit=limit)

Retrieve a receiving job's status

After sending data to Visier, you may want to know the status of the receiving job and the associated tenant  receiving jobs. A receiving job validates the transferred data and adds the transferred data to Visier's data  store.   Use this API to retrieve the receiving job status and summary of analytic tenant receiving jobs.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.data_handling
from visier.api.data_handling.models.receiving_job_status_response import ReceivingJobStatusResponse
from visier.api.data_handling.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.data_handling.Configuration(
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
configuration = visier.api.data_handling.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.data_handling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.data_handling.DataAndJobHandlingApi(api_client)
    receiving_job_id = 'receiving_job_id_example' # str | The jobId provided after sending data to Visier.
    jobs = True # bool | If \"true\", returns the status of receiving jobs spawned by the receiving job specified by jobId. (optional)
    tenant_code = 'tenant_code_example' # str | The tenant code of the tenant you want to retrieve the receiving jobs for. Use this if you are only interested  in the results for one analytic tenant. (optional)
    start = 56 # int | The index to start retrieving results from, also known as offset. The index begins at 0. (optional)
    limit = 56 # int | The number of job statuses to return per page. (optional)

    try:
        # Retrieve a receiving job's status
        api_response = api_instance.receiving_job_status(receiving_job_id, jobs=jobs, tenant_code=tenant_code, start=start, limit=limit)
        print("The response of DataAndJobHandlingApi->receiving_job_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataAndJobHandlingApi->receiving_job_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receiving_job_id** | **str**| The jobId provided after sending data to Visier. | 
 **jobs** | **bool**| If \&quot;true\&quot;, returns the status of receiving jobs spawned by the receiving job specified by jobId. | [optional] 
 **tenant_code** | **str**| The tenant code of the tenant you want to retrieve the receiving jobs for. Use this if you are only interested  in the results for one analytic tenant. | [optional] 
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

# **retrieve_data_categories**
> DataCategoriesResponseDTO retrieve_data_categories()

Retrieve a list of all data categories

Use this API to retrieve a list of all available data categories.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.data_handling
from visier.api.data_handling.models.data_categories_response_dto import DataCategoriesResponseDTO
from visier.api.data_handling.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.data_handling.Configuration(
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
configuration = visier.api.data_handling.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.data_handling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.data_handling.DataAndJobHandlingApi(api_client)

    try:
        # Retrieve a list of all data categories
        api_response = api_instance.retrieve_data_categories()
        print("The response of DataAndJobHandlingApi->retrieve_data_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataAndJobHandlingApi->retrieve_data_categories: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DataCategoriesResponseDTO**](DataCategoriesResponseDTO.md)

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

# **retrieve_data_uploads**
> TenantDataUploadsListResponseDTO retrieve_data_uploads(upload_job_id=upload_job_id, tenant_code=tenant_code, limit=limit, start=start, number_of_data_uploads=number_of_data_uploads)

Retrieve data uploads

Use this API to retrieve the data uploads and whether they're included in one of:  - A list of analytic tenants managed by you.  - A single specified analytic tenant.  - An upload job.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.data_handling
from visier.api.data_handling.models.tenant_data_uploads_list_response_dto import TenantDataUploadsListResponseDTO
from visier.api.data_handling.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.data_handling.Configuration(
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
configuration = visier.api.data_handling.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.data_handling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.data_handling.DataAndJobHandlingApi(api_client)
    upload_job_id = 'upload_job_id_example' # str | The job ID of an upload job. Use this if you are interested in the data uploads for a specific upload job. (optional)
    tenant_code = 56 # int | The tenant code of a specific analytic tenant that you want to retrieve the data uploads for. (optional)
    limit = 56 # int | The limit of analytic tenants to retrieve data uploads for. This parameter is not used if the tenantCode parameter is specified. (optional)
    start = 56 # int | The index to start retrieving results from, also known as offset. The index begins at 0. (optional)
    number_of_data_uploads = 56 # int | The maximum number of latest enabled data uploads to retrieve for each analytic tenant. The maximum value is 5. (optional)

    try:
        # Retrieve data uploads
        api_response = api_instance.retrieve_data_uploads(upload_job_id=upload_job_id, tenant_code=tenant_code, limit=limit, start=start, number_of_data_uploads=number_of_data_uploads)
        print("The response of DataAndJobHandlingApi->retrieve_data_uploads:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataAndJobHandlingApi->retrieve_data_uploads: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_job_id** | **str**| The job ID of an upload job. Use this if you are interested in the data uploads for a specific upload job. | [optional] 
 **tenant_code** | **int**| The tenant code of a specific analytic tenant that you want to retrieve the data uploads for. | [optional] 
 **limit** | **int**| The limit of analytic tenants to retrieve data uploads for. This parameter is not used if the tenantCode parameter is specified. | [optional] 
 **start** | **int**| The index to start retrieving results from, also known as offset. The index begins at 0. | [optional] 
 **number_of_data_uploads** | **int**| The maximum number of latest enabled data uploads to retrieve for each analytic tenant. The maximum value is 5. | [optional] 

### Return type

[**TenantDataUploadsListResponseDTO**](TenantDataUploadsListResponseDTO.md)

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

# **start_extraction**
> StartExtractionResponse start_extraction(start_extraction_request)

Trigger extraction jobs

Use this API to generate extraction jobs for a list of analytic tenants or for the administrating tenant.  This API creates a dispatching job that generates one extraction job per tenant. The extraction jobs retrieve  data from your source systems through data connectors. The dispatching job is the \"parent\" of the extraction  jobs and its job ID is returned in the response.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.data_handling
from visier.api.data_handling.models.start_extraction_request import StartExtractionRequest
from visier.api.data_handling.models.start_extraction_response import StartExtractionResponse
from visier.api.data_handling.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.data_handling.Configuration(
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
configuration = visier.api.data_handling.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.data_handling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.data_handling.DataAndJobHandlingApi(api_client)
    start_extraction_request = visier.api.data_handling.StartExtractionRequest() # StartExtractionRequest | 

    try:
        # Trigger extraction jobs
        api_response = api_instance.start_extraction(start_extraction_request)
        print("The response of DataAndJobHandlingApi->start_extraction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataAndJobHandlingApi->start_extraction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_extraction_request** | [**StartExtractionRequest**](StartExtractionRequest.md)|  | 

### Return type

[**StartExtractionResponse**](StartExtractionResponse.md)

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

# **start_load**
> DataLoadResponse start_load(data_load_request)

Start the data load for an analytic tenant

This API starts the data load process for all analytic tenants included in the specified data files uploaded  to the Visier SFTP server. On success, you receive a job ID that can be filtered and searched for within the  Jobs room in Visier. This job ID is associated with the receiving job, and related to all processing jobs that  spawn for each analytic tenant.   With the job ID, you can also call the next two APIs to retrieve the status of the receiving job and the status  list of all related processing jobs.   **Prerequisite:** You must first obtain Visier's public encryption key and upload the source data files to Visier's  SFTP server. Files must have a .zip.gpg extension, meaning the files are encrypted using the PGP protocol and compressed.   Visier provides SFTP server credentials and instructions. You can find the encryption key at https://www.visier.com/pgp/visier.public.pgp.asc.  After downloading the file, open the file in a text editor or by dragging it into your browser.   **Note:**   - To see the full status of all analytic tenant data loads, navigate to the Jobs room in a project.   - For performance and efficiency, Visier requires that the uncompressed batch file size is below 5 GB and that no     more than 5000 tenants are included in a batch.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.data_handling
from visier.api.data_handling.models.data_load_request import DataLoadRequest
from visier.api.data_handling.models.data_load_response import DataLoadResponse
from visier.api.data_handling.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.data_handling.Configuration(
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
configuration = visier.api.data_handling.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.data_handling.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.data_handling.DataAndJobHandlingApi(api_client)
    data_load_request = visier.api.data_handling.DataLoadRequest() # DataLoadRequest | 

    try:
        # Start the data load for an analytic tenant
        api_response = api_instance.start_load(data_load_request)
        print("The response of DataAndJobHandlingApi->start_load:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataAndJobHandlingApi->start_load: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_load_request** | [**DataLoadRequest**](DataLoadRequest.md)|  | 

### Return type

[**DataLoadResponse**](DataLoadResponse.md)

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

