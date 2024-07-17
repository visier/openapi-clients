# visier.api.direct_data_intake.DataIntakeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**upload_file**](DataIntakeApi.md#upload_file) | **PUT** /v1/data/directloads/{draftId}/transactions/{transactionId}/{objectName} | Upload files


# **upload_file**
> DirectDataUploadFileResponseDTO upload_file(draft_id, transaction_id, object_name, body=body)

Upload files

Send upload files to a previously-created transaction. Each upload file is associated with a target object in Visier. The files are not processed in Visier until you commit the transaction.

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
    api_instance = visier.api.direct_data_intake.DataIntakeApi(api_client)
    draft_id = 'draft_id_example' # str | The unique identifier of the project to load data into. Currently, the only supported value is `prod` to update the production version.
    transaction_id = 'transaction_id_example' # str | The unique identifier of the transaction to load data files into.
    object_name = 'object_name_example' # str | The name of the object to upload the data to.  If uploading data to a multi-value property (MVP), specify the property in `{object}--{property}` format; for example, `Employee--Employee_Budgeted_Compensation`.
    body = None # bytearray |  (optional)

    try:
        # Upload files
        api_response = api_instance.upload_file(draft_id, transaction_id, object_name, body=body)
        print("The response of DataIntakeApi->upload_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataIntakeApi->upload_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **draft_id** | **str**| The unique identifier of the project to load data into. Currently, the only supported value is &#x60;prod&#x60; to update the production version. | 
 **transaction_id** | **str**| The unique identifier of the transaction to load data files into. | 
 **object_name** | **str**| The name of the object to upload the data to.  If uploading data to a multi-value property (MVP), specify the property in &#x60;{object}--{property}&#x60; format; for example, &#x60;Employee--Employee_Budgeted_Compensation&#x60;. | 
 **body** | **bytearray**|  | [optional] 

### Return type

[**DirectDataUploadFileResponseDTO**](DirectDataUploadFileResponseDTO.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [OAuth2Auth](../README.md#OAuth2Auth), [OAuth2Auth](../README.md#OAuth2Auth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/octetstream
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

