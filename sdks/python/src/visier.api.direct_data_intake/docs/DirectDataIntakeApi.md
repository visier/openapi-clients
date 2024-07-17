# visier.api.direct_data_intake.DirectDataIntakeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**commit_transaction**](DirectDataIntakeApi.md#commit_transaction) | **POST** /v1/data/directloads/{draftId}/transactions/{transactionId} | Commit a transaction
[**get_config**](DirectDataIntakeApi.md#get_config) | **GET** /v1/data/directloads/{draftId}/configs | Get the direct data intake configuration
[**job_status**](DirectDataIntakeApi.md#job_status) | **GET** /v1/data/directloads/{draftId}/transactions/{transactionId} | Check transaction status
[**object_schema**](DirectDataIntakeApi.md#object_schema) | **GET** /v1/data/directloads/{draftId}/schemas/{objectName} | Retrieve an object&#39;s data load schema
[**put_config**](DirectDataIntakeApi.md#put_config) | **PUT** /v1/data/directloads/{draftId}/configs | Update the direct data intake configuration
[**rollback_transaction**](DirectDataIntakeApi.md#rollback_transaction) | **DELETE** /v1/data/directloads/{draftId}/transactions/{transactionId} | Roll back a transaction
[**start_transaction**](DirectDataIntakeApi.md#start_transaction) | **POST** /v1/data/directloads/{draftId}/transactions | Start a direct data intake transaction


# **commit_transaction**
> DirectDataUploadFileResponseDTO commit_transaction(draft_id, transaction_id)

Commit a transaction

Process a transaction and its uploaded data files. This starts a processing job to load the data files into Visier.   After committing a transaction, you cannot upload additional files to the transaction. Use the `Check transaction status` API to monitor the progress of the processing job.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.direct_data_intake
from visier.api.direct_data_intake.models.direct_data_upload_file_response_dto import DirectDataUploadFileResponseDTO
from visier.api.direct_data_intake.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.direct_data_intake.Configuration(
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
configuration = visier.api.direct_data_intake.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.direct_data_intake.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.direct_data_intake.DirectDataIntakeApi(api_client)
    draft_id = 'draft_id_example' # str | The unique identifier of the project to load data into. Currently, the only supported value is `prod` to update the production version.
    transaction_id = 'transaction_id_example' # str | The unique identifier of the transaction.

    try:
        # Commit a transaction
        api_response = api_instance.commit_transaction(draft_id, transaction_id)
        print("The response of DirectDataIntakeApi->commit_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DirectDataIntakeApi->commit_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **draft_id** | **str**| The unique identifier of the project to load data into. Currently, the only supported value is &#x60;prod&#x60; to update the production version. | 
 **transaction_id** | **str**| The unique identifier of the transaction. | 

### Return type

[**DirectDataUploadFileResponseDTO**](DirectDataUploadFileResponseDTO.md)

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

# **get_config**
> DirectDataLoadConfigDTO get_config(draft_id)

Get the direct data intake configuration

Get the direct data intake configuration.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.direct_data_intake
from visier.api.direct_data_intake.models.direct_data_load_config_dto import DirectDataLoadConfigDTO
from visier.api.direct_data_intake.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.direct_data_intake.Configuration(
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
configuration = visier.api.direct_data_intake.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.direct_data_intake.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.direct_data_intake.DirectDataIntakeApi(api_client)
    draft_id = 'draft_id_example' # str | The unique identifier of the project to load data into. Currently, the only supported value is `prod` to update the production version.

    try:
        # Get the direct data intake configuration
        api_response = api_instance.get_config(draft_id)
        print("The response of DirectDataIntakeApi->get_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DirectDataIntakeApi->get_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **draft_id** | **str**| The unique identifier of the project to load data into. Currently, the only supported value is &#x60;prod&#x60; to update the production version. | 

### Return type

[**DirectDataLoadConfigDTO**](DirectDataLoadConfigDTO.md)

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
> DirectDataJobStatusResponseDTO job_status(draft_id, transaction_id)

Check transaction status

Retrieve the status of a committed transaction’s processing job.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.direct_data_intake
from visier.api.direct_data_intake.models.direct_data_job_status_response_dto import DirectDataJobStatusResponseDTO
from visier.api.direct_data_intake.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.direct_data_intake.Configuration(
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
configuration = visier.api.direct_data_intake.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.direct_data_intake.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.direct_data_intake.DirectDataIntakeApi(api_client)
    draft_id = 'draft_id_example' # str | The unique identifier of the project to load data into. Currently, the only supported value is `prod` to update the production version.
    transaction_id = 'transaction_id_example' # str | The unique identifier of the transaction.

    try:
        # Check transaction status
        api_response = api_instance.job_status(draft_id, transaction_id)
        print("The response of DirectDataIntakeApi->job_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DirectDataIntakeApi->job_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **draft_id** | **str**| The unique identifier of the project to load data into. Currently, the only supported value is &#x60;prod&#x60; to update the production version. | 
 **transaction_id** | **str**| The unique identifier of the transaction. | 

### Return type

[**DirectDataJobStatusResponseDTO**](DirectDataJobStatusResponseDTO.md)

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

# **object_schema**
> DirectDataSchemaFieldDTO object_schema(draft_id, object_name)

Retrieve an object's data load schema

Gets the load schema for a specified object. The object's load schema represents the structure that the data upload file must follow to upload data to the object.   In the load schema, the listed columns must be present in the data file as column headers and exactly match the load schema (case sensitive), however,  only the columns whose `isMandatory` field is `true` must contain values in the data file.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.direct_data_intake
from visier.api.direct_data_intake.models.direct_data_schema_field_dto import DirectDataSchemaFieldDTO
from visier.api.direct_data_intake.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.direct_data_intake.Configuration(
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
configuration = visier.api.direct_data_intake.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.direct_data_intake.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.direct_data_intake.DirectDataIntakeApi(api_client)
    draft_id = 'draft_id_example' # str | The unique identifier of the project to load data into. Currently, the only supported value is `prod` to update the production version.
    object_name = 'object_name_example' # str | The name of the object to return the load schema for.

    try:
        # Retrieve an object's data load schema
        api_response = api_instance.object_schema(draft_id, object_name)
        print("The response of DirectDataIntakeApi->object_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DirectDataIntakeApi->object_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **draft_id** | **str**| The unique identifier of the project to load data into. Currently, the only supported value is &#x60;prod&#x60; to update the production version. | 
 **object_name** | **str**| The name of the object to return the load schema for. | 

### Return type

[**DirectDataSchemaFieldDTO**](DirectDataSchemaFieldDTO.md)

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

# **put_config**
> DirectDataLoadConfigDTO put_config(draft_id, direct_data_load_config_dto)

Update the direct data intake configuration

Configure the data intake settings, such as the direct data intake job type. Only provide values for the configuration options that should change.   Configuration options that are not present in the PUT request are ignored and left unchanged.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.direct_data_intake
from visier.api.direct_data_intake.models.direct_data_load_config_dto import DirectDataLoadConfigDTO
from visier.api.direct_data_intake.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.direct_data_intake.Configuration(
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
configuration = visier.api.direct_data_intake.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.direct_data_intake.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.direct_data_intake.DirectDataIntakeApi(api_client)
    draft_id = 'draft_id_example' # str | The unique identifier of the project to load data into. Currently, the only supported value is `prod` to update the production version.
    direct_data_load_config_dto = visier.api.direct_data_intake.DirectDataLoadConfigDTO() # DirectDataLoadConfigDTO | 

    try:
        # Update the direct data intake configuration
        api_response = api_instance.put_config(draft_id, direct_data_load_config_dto)
        print("The response of DirectDataIntakeApi->put_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DirectDataIntakeApi->put_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **draft_id** | **str**| The unique identifier of the project to load data into. Currently, the only supported value is &#x60;prod&#x60; to update the production version. | 
 **direct_data_load_config_dto** | [**DirectDataLoadConfigDTO**](DirectDataLoadConfigDTO.md)|  | 

### Return type

[**DirectDataLoadConfigDTO**](DirectDataLoadConfigDTO.md)

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

# **rollback_transaction**
> DirectDataUploadFileResponseDTO rollback_transaction(draft_id, transaction_id)

Roll back a transaction

Rolls back the specified transaction. This discards all files uploaded within the transaction and deletes the transaction.   After rolling back a transaction, you cannot use the transaction to upload data files.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.direct_data_intake
from visier.api.direct_data_intake.models.direct_data_upload_file_response_dto import DirectDataUploadFileResponseDTO
from visier.api.direct_data_intake.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.direct_data_intake.Configuration(
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
configuration = visier.api.direct_data_intake.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.direct_data_intake.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.direct_data_intake.DirectDataIntakeApi(api_client)
    draft_id = 'draft_id_example' # str | The unique identifier of the project to load data into. Currently, the only supported value is `prod` to update the production version.
    transaction_id = 'transaction_id_example' # str | The unique identifier of the transaction.

    try:
        # Roll back a transaction
        api_response = api_instance.rollback_transaction(draft_id, transaction_id)
        print("The response of DirectDataIntakeApi->rollback_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DirectDataIntakeApi->rollback_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **draft_id** | **str**| The unique identifier of the project to load data into. Currently, the only supported value is &#x60;prod&#x60; to update the production version. | 
 **transaction_id** | **str**| The unique identifier of the transaction. | 

### Return type

[**DirectDataUploadFileResponseDTO**](DirectDataUploadFileResponseDTO.md)

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

# **start_transaction**
> DirectDataTransactionStartResponseDTO start_transaction(draft_id)

Start a direct data intake transaction

Create a transaction to contain your data files. To upload files to objects in Visier, you must first start a transaction.   After starting a transaction and uploading files to the transaction, you can commit the transaction to process the uploaded files or roll back the transaction to discard the uploaded files.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.direct_data_intake
from visier.api.direct_data_intake.models.direct_data_transaction_start_response_dto import DirectDataTransactionStartResponseDTO
from visier.api.direct_data_intake.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.direct_data_intake.Configuration(
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
configuration = visier.api.direct_data_intake.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.direct_data_intake.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.direct_data_intake.DirectDataIntakeApi(api_client)
    draft_id = 'draft_id_example' # str | The unique identifier of the project to load data into. Currently, the only supported value is `prod` to update the production version.

    try:
        # Start a direct data intake transaction
        api_response = api_instance.start_transaction(draft_id)
        print("The response of DirectDataIntakeApi->start_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DirectDataIntakeApi->start_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **draft_id** | **str**| The unique identifier of the project to load data into. Currently, the only supported value is &#x60;prod&#x60; to update the production version. | 

### Return type

[**DirectDataTransactionStartResponseDTO**](DirectDataTransactionStartResponseDTO.md)

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

