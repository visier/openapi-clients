# visier.api.system_status.SystemStatusApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_system_status**](SystemStatusApi.md#post_system_status) | **POST** /v1/admin/system-status | Check the overall current status of Visier&#39;s systems
[**system_status**](SystemStatusApi.md#system_status) | **GET** /v1/admin/system-status | Check the overall current status of Visier&#39;s systems


# **post_system_status**
> SystemStatusDTO post_system_status()

Check the overall current status of Visier's systems

Use this API to check the current overall status of Visier's systems.   The overall status is one of:  * ``UP`` : All systems are operational.  * `DOWN`: At least one system is not fully operational.   **Note:** This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import visier.api.system_status
from visier.api.system_status.models.system_status_dto import SystemStatusDTO
from visier.api.system_status.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.system_status.Configuration(
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

# Enter a context with an instance of the API client
with visier.api.system_status.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.system_status.SystemStatusApi(api_client)

    try:
        # Check the overall current status of Visier's systems
        api_response = api_instance.post_system_status()
        print("The response of SystemStatusApi->post_system_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemStatusApi->post_system_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SystemStatusDTO**](SystemStatusDTO.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_status**
> SystemStatusDTO system_status()

Check the overall current status of Visier's systems

Use this API to check the current overall status of Visier's systems.   The overall status is one of:  * ``UP`` : All systems are operational.  * `DOWN`: At least one system is not fully operational.   **Note:** This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import visier.api.system_status
from visier.api.system_status.models.system_status_dto import SystemStatusDTO
from visier.api.system_status.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.system_status.Configuration(
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

# Enter a context with an instance of the API client
with visier.api.system_status.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.system_status.SystemStatusApi(api_client)

    try:
        # Check the overall current status of Visier's systems
        api_response = api_instance.system_status()
        print("The response of SystemStatusApi->system_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemStatusApi->system_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SystemStatusDTO**](SystemStatusDTO.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

