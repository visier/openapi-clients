# visier.api.document_search.DocumentSearchApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**simple_search_document_headers**](DocumentSearchApi.md#simple_search_document_headers) | **GET** /v1alpha/search/simple/document-headers | Perform a simple search for Visier document headers


# **simple_search_document_headers**
> SimpleDocumentHeaderSearchResponseDTO simple_search_document_headers(q=q, limit=limit, offset=offset)

Perform a simple search for Visier document headers

Perform a simple search for Visier document headers, such as analysis titles. Simple search doesn't support keywords, Boolean expressions, or any other advanced search features.  Example: `GET /v1alpha/search/simple/document-headers?q=My+Query&limit=10` returns the first 10 document headers that best match the query string `My Query`.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.document_search
from visier.api.document_search.models.simple_document_header_search_response_dto import SimpleDocumentHeaderSearchResponseDTO
from visier.api.document_search.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.document_search.Configuration(
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
configuration = visier.api.document_search.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.document_search.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.document_search.DocumentSearchApi(api_client)
    q = 'q_example' # str | The search query string. (optional)
    limit = 56 # int | The maximum number of results to return. Defaults to 100. (optional)
    offset = 56 # int | The index to start retrieving results from, also known as offset. Defaults to 0. (optional)

    try:
        # Perform a simple search for Visier document headers
        api_response = api_instance.simple_search_document_headers(q=q, limit=limit, offset=offset)
        print("The response of DocumentSearchApi->simple_search_document_headers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentSearchApi->simple_search_document_headers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| The search query string. | [optional] 
 **limit** | **int**| The maximum number of results to return. Defaults to 100. | [optional] 
 **offset** | **int**| The index to start retrieving results from, also known as offset. Defaults to 0. | [optional] 

### Return type

[**SimpleDocumentHeaderSearchResponseDTO**](SimpleDocumentHeaderSearchResponseDTO.md)

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

