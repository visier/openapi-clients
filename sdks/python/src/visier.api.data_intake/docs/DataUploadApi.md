# visier.api.data_intake.DataUploadApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_data_upload_files_filename_put**](DataUploadApi.md#v1_data_upload_files_filename_put) | **PUT** /v1/data/upload/files/{filename} | Upload a data file to Visier
[**v1alpha_data_upload_files_filename_put**](DataUploadApi.md#v1alpha_data_upload_files_filename_put) | **PUT** /v1alpha/data/upload/files/{filename} | Upload a data file to Visier


# **v1_data_upload_files_filename_put**
> Status v1_data_upload_files_filename_put(filename, body=body)

Upload a data file to Visier

Use this API to upload data files to Visier. You can upload ZIP, CSV, XLS, and XLSX filetypes in plaintext or encrypted with Visier's PGP key.   Use of this API requires client redirect. This API redirects requests directly to Visier's upload infrastructure to support long-running uploads.   To ensure efficient uploading, we recommend that you use an HTTP client that supports the 100 Continue status code.   The maximum file upload size is 500 MB. We recommend using SFTP for larger file sizes.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.data_intake
from visier.api.data_intake.models.status import Status
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
    api_instance = visier.api.data_intake.DataUploadApi(api_client)
    filename = 'filename_example' # str | The filename of the data file to upload, including the file extension (such as .zip or .csv).
    body = None # bytearray |  (optional)

    try:
        # Upload a data file to Visier
        api_response = api_instance.v1_data_upload_files_filename_put(filename, body=body)
        print("The response of DataUploadApi->v1_data_upload_files_filename_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataUploadApi->v1_data_upload_files_filename_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**| The filename of the data file to upload, including the file extension (such as .zip or .csv). | 
 **body** | **bytearray**|  | [optional] 

### Return type

[**Status**](Status.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [OAuth2Auth](../README.md#OAuth2Auth), [OAuth2Auth](../README.md#OAuth2Auth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**307** | Redirect to Visier&#39;s upload infrastructure. |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1alpha_data_upload_files_filename_put**
> Status v1alpha_data_upload_files_filename_put(filename, body=body)

Upload a data file to Visier

This API has been promoted from Alpha, and is generally available with the `v1` prefix

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.data_intake
from visier.api.data_intake.models.status import Status
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
    api_instance = visier.api.data_intake.DataUploadApi(api_client)
    filename = 'filename_example' # str | The filename of the data file to upload, including the file extension (such as .zip or .csv).
    body = None # bytearray |  (optional)

    try:
        # Upload a data file to Visier
        api_response = api_instance.v1alpha_data_upload_files_filename_put(filename, body=body)
        print("The response of DataUploadApi->v1alpha_data_upload_files_filename_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataUploadApi->v1alpha_data_upload_files_filename_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**| The filename of the data file to upload, including the file extension (such as .zip or .csv). | 
 **body** | **bytearray**|  | [optional] 

### Return type

[**Status**](Status.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [OAuth2Auth](../README.md#OAuth2Auth), [OAuth2Auth](../README.md#OAuth2Auth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**307** | Redirect to Visier&#39;s upload infrastructure. |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

