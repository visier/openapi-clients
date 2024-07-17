# visier.api.data-intake
Visier APIs for sending raw or untransformed source data to Visier

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 22222222.99201.1389
- Package version: 1.0.0
- Generator version: 7.8.0-SNAPSHOT
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import visier.api.data_intake
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import visier.api.data_intake
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import visier.api.data_intake
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
    except ApiException as e:
        print("Exception when calling DataIntakeApi->get_processing_jobs_by_parent_receiving_job_id: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DataIntakeApi* | [**get_processing_jobs_by_parent_receiving_job_id**](docs/DataIntakeApi.md#get_processing_jobs_by_parent_receiving_job_id) | **GET** /v1/op/jobs/processing-jobs/{receivingJobId} | Retrieve processing job statuses by receiving job ID
*DataIntakeApi* | [**get_sources**](docs/DataIntakeApi.md#get_sources) | **GET** /v1/op/data-sources | Retrieve a list of sources
*DataIntakeApi* | [**push_data**](docs/DataIntakeApi.md#push_data) | **PUT** /v1/op/data-transfer-sessions/{transferSessionId}/add | Transfer data to sources via JSON
*DataIntakeApi* | [**push_data_cancel**](docs/DataIntakeApi.md#push_data_cancel) | **PUT** /v1/op/data-transfer-sessions/{transferSessionId}/cancel | Cancel a transfer session
*DataIntakeApi* | [**push_data_complete**](docs/DataIntakeApi.md#push_data_complete) | **POST** /v1/op/jobs/receiving-jobs | Complete a transfer session
*DataIntakeApi* | [**receiving_job_status**](docs/DataIntakeApi.md#receiving_job_status) | **GET** /v1/op/jobs/receiving-jobs/{receivingJobId} | Retrieve a receiving job’s status
*DataIntakeApi* | [**start_transfer**](docs/DataIntakeApi.md#start_transfer) | **POST** /v1/op/data-transfer-sessions | Start a transfer session
*DataIntakeApi* | [**upload_data**](docs/DataIntakeApi.md#upload_data) | **PUT** /v1/op/data-transfer-sessions/{transferSessionId}/upload | Transfer data to sources via file upload
*DataUploadApi* | [**v1_data_upload_files_filename_put**](docs/DataUploadApi.md#v1_data_upload_files_filename_put) | **PUT** /v1/data/upload/files/{filename} | Upload a data file to Visier
*DataUploadApi* | [**v1alpha_data_upload_files_filename_put**](docs/DataUploadApi.md#v1alpha_data_upload_files_filename_put) | **PUT** /v1alpha/data/upload/files/{filename} | Upload a data file to Visier


## Documentation For Models

 - [DataTransferResultDetail](docs/DataTransferResultDetail.md)
 - [GetProcessingJobsResponse](docs/GetProcessingJobsResponse.md)
 - [GoogleProtobufAny](docs/GoogleProtobufAny.md)
 - [Job](docs/Job.md)
 - [ProcessingJob](docs/ProcessingJob.md)
 - [PushDataCancelResponse](docs/PushDataCancelResponse.md)
 - [PushDataColumnDefinitionDTO](docs/PushDataColumnDefinitionDTO.md)
 - [PushDataCompleteRequest](docs/PushDataCompleteRequest.md)
 - [PushDataCompleteResponse](docs/PushDataCompleteResponse.md)
 - [PushDataResponse](docs/PushDataResponse.md)
 - [PushDataSourceDefinitionDTO](docs/PushDataSourceDefinitionDTO.md)
 - [PushDataSourceDefinitionsDTO](docs/PushDataSourceDefinitionsDTO.md)
 - [ReceivingJobStatusResponse](docs/ReceivingJobStatusResponse.md)
 - [Source](docs/Source.md)
 - [StartTransferResponse](docs/StartTransferResponse.md)
 - [Status](docs/Status.md)
 - [Tenant](docs/Tenant.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="ApiKeyAuth"></a>
### ApiKeyAuth

- **Type**: API key
- **API key parameter name**: apikey
- **Location**: HTTP header

<a id="BearerAuth"></a>
### BearerAuth

- **Type**: Bearer authentication

<a id="CookieAuth"></a>
### CookieAuth

- **Type**: API key
- **API key parameter name**: VisierASIDToken
- **Location**: 

<a id="OAuth2Auth"></a>
### OAuth2Auth

- **Type**: OAuth
- **Flow**: password
- **Authorization URL**: 
- **Scopes**: 
 - **read**: Grants read access
 - **write**: Grants write access

<a id="OAuth2Auth"></a>
### OAuth2Auth

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: /v1/auth/oauth2/authorize
- **Scopes**: 
 - **read**: Grants read access
 - **write**: Grants write access


## Author



