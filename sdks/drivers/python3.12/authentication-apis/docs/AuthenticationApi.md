# visier.authentication.AuthenticationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authentication_asid_token_authentication**](AuthenticationApi.md#authentication_asid_token_authentication) | **POST** /v1/admin/visierSecureToken | Request a Visier authentication token.


# **authentication_asid_token_authentication**
> str authentication_asid_token_authentication(username=username, password=password)

Request a Visier authentication token.

Generate a secure ASID token.

### Example


```python
import visier.authentication
from visier.authentication.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.authentication.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with visier.authentication.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.authentication.AuthenticationApi(api_client)
    username = 'username_example' # str | The unique identifier of the API user requesting a security token. (optional)
    password = 'password_example' # str | The password that corresponds to the user making the request. (optional)

    try:
        # Request a Visier authentication token.
        api_response = api_instance.authentication_asid_token_authentication(username=username, password=password)
        print("The response of AuthenticationApi->authentication_asid_token_authentication:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->authentication_asid_token_authentication: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The unique identifier of the API user requesting a security token. | [optional] 
 **password** | **str**| The password that corresponds to the user making the request. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Authentication token response |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

