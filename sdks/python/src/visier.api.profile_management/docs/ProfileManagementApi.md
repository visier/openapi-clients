# visier.api.profile_management.ProfileManagementApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_analytic_profile**](ProfileManagementApi.md#assign_analytic_profile) | **PUT** /v1/admin/profiles/accessible-tenants/{profileId}/assign | Assign an analytic tenant profile to administrating tenant users
[**assign_profile**](ProfileManagementApi.md#assign_profile) | **PUT** /v1/admin/profiles/{profileId}/assign | Assign a profile to a list of users
[**get_all_profiles**](ProfileManagementApi.md#get_all_profiles) | **GET** /v1/admin/profiles | Retrieve a list of all profiles
[**get_analytic_profile_detail**](ProfileManagementApi.md#get_analytic_profile_detail) | **GET** /v1/admin/profiles/accessible-tenants/{profileId} | Retrieve the details of an analytic tenant profile
[**get_analytic_profiles**](ProfileManagementApi.md#get_analytic_profiles) | **GET** /v1/admin/profiles/accessible-tenants | Retrieve a list of analytic tenant profiles
[**get_analytic_user_profile**](ProfileManagementApi.md#get_analytic_user_profile) | **GET** /v1/admin/users/{userId}/accessible-tenant-profiles | Retrieve an administrating tenant user&#39;s analytic tenant profiles
[**get_profile_detail**](ProfileManagementApi.md#get_profile_detail) | **GET** /v1/admin/profiles/{profileId} | Retrieve the details of a profile
[**get_user_profile**](ProfileManagementApi.md#get_user_profile) | **GET** /v1/admin/users/{userId}/profiles | Retrieve a user&#39;s profiles
[**remove_analytic_profile**](ProfileManagementApi.md#remove_analytic_profile) | **DELETE** /v1/admin/profiles/accessible-tenants/{profileId}/remove | Remove an analytic tenant profile from administrating tenant users
[**remove_profile**](ProfileManagementApi.md#remove_profile) | **DELETE** /v1/admin/profiles/{profileId}/remove | Remove a profile from a list of users


# **assign_analytic_profile**
> AccessibleTenantProfileAssignmentResponseDTO assign_analytic_profile(profile_id, accessible_tenant_profile_assignment_request_dto)

Assign an analytic tenant profile to administrating tenant users

This API allows you to assign an analytic tenant profile to a list of administrating tenant users  for a list of analytic tenants.   Note:   - Administrating tenants only.   - You can revoke a profile from a user with this request by updating the validityEndTime to be     \"less than\" the current time (that is, in the past).

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.profile_management
from visier.api.profile_management.models.accessible_tenant_profile_assignment_request_dto import AccessibleTenantProfileAssignmentRequestDTO
from visier.api.profile_management.models.accessible_tenant_profile_assignment_response_dto import AccessibleTenantProfileAssignmentResponseDTO
from visier.api.profile_management.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.profile_management.Configuration(
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
configuration = visier.api.profile_management.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.profile_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.profile_management.ProfileManagementApi(api_client)
    profile_id = 'profile_id_example' # str | The ID of the profile to assign.
    accessible_tenant_profile_assignment_request_dto = visier.api.profile_management.AccessibleTenantProfileAssignmentRequestDTO() # AccessibleTenantProfileAssignmentRequestDTO | 

    try:
        # Assign an analytic tenant profile to administrating tenant users
        api_response = api_instance.assign_analytic_profile(profile_id, accessible_tenant_profile_assignment_request_dto)
        print("The response of ProfileManagementApi->assign_analytic_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileManagementApi->assign_analytic_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The ID of the profile to assign. | 
 **accessible_tenant_profile_assignment_request_dto** | [**AccessibleTenantProfileAssignmentRequestDTO**](AccessibleTenantProfileAssignmentRequestDTO.md)|  | 

### Return type

[**AccessibleTenantProfileAssignmentResponseDTO**](AccessibleTenantProfileAssignmentResponseDTO.md)

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

# **assign_profile**
> LocalTenantProfileAssignmentResponseDTO assign_profile(profile_id, local_tenant_profile_assignment_request_dto)

Assign a profile to a list of users

This API allows you to assign a profile to a list of users. For administrating tenants,  this assigns an administrating tenant profile to a list of users.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.profile_management
from visier.api.profile_management.models.local_tenant_profile_assignment_request_dto import LocalTenantProfileAssignmentRequestDTO
from visier.api.profile_management.models.local_tenant_profile_assignment_response_dto import LocalTenantProfileAssignmentResponseDTO
from visier.api.profile_management.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.profile_management.Configuration(
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
configuration = visier.api.profile_management.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.profile_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.profile_management.ProfileManagementApi(api_client)
    profile_id = 'profile_id_example' # str | The ID of the profile to assign to a list of users.
    local_tenant_profile_assignment_request_dto = visier.api.profile_management.LocalTenantProfileAssignmentRequestDTO() # LocalTenantProfileAssignmentRequestDTO | 

    try:
        # Assign a profile to a list of users
        api_response = api_instance.assign_profile(profile_id, local_tenant_profile_assignment_request_dto)
        print("The response of ProfileManagementApi->assign_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileManagementApi->assign_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The ID of the profile to assign to a list of users. | 
 **local_tenant_profile_assignment_request_dto** | [**LocalTenantProfileAssignmentRequestDTO**](LocalTenantProfileAssignmentRequestDTO.md)|  | 

### Return type

[**LocalTenantProfileAssignmentResponseDTO**](LocalTenantProfileAssignmentResponseDTO.md)

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

# **get_all_profiles**
> ProfilesGetAPIResponseDTO get_all_profiles()

Retrieve a list of all profiles

This API allows you to get a list of all available profiles. For administrating tenants,  this retrieves all administrating tenant profiles.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.profile_management
from visier.api.profile_management.models.profiles_get_api_response_dto import ProfilesGetAPIResponseDTO
from visier.api.profile_management.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.profile_management.Configuration(
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
configuration = visier.api.profile_management.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.profile_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.profile_management.ProfileManagementApi(api_client)

    try:
        # Retrieve a list of all profiles
        api_response = api_instance.get_all_profiles()
        print("The response of ProfileManagementApi->get_all_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileManagementApi->get_all_profiles: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ProfilesGetAPIResponseDTO**](ProfilesGetAPIResponseDTO.md)

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

# **get_analytic_profile_detail**
> ProfileGetAPIResponseDTO get_analytic_profile_detail(profile_id)

Retrieve the details of an analytic tenant profile

This API allows you to get the details of an analytic tenant profile.   Note: Administrating tenants only.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.profile_management
from visier.api.profile_management.models.profile_get_api_response_dto import ProfileGetAPIResponseDTO
from visier.api.profile_management.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.profile_management.Configuration(
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
configuration = visier.api.profile_management.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.profile_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.profile_management.ProfileManagementApi(api_client)
    profile_id = 'profile_id_example' # str | The ID of the profile to retrieve details for.

    try:
        # Retrieve the details of an analytic tenant profile
        api_response = api_instance.get_analytic_profile_detail(profile_id)
        print("The response of ProfileManagementApi->get_analytic_profile_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileManagementApi->get_analytic_profile_detail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The ID of the profile to retrieve details for. | 

### Return type

[**ProfileGetAPIResponseDTO**](ProfileGetAPIResponseDTO.md)

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

# **get_analytic_profiles**
> ProfilesGetAPIResponseDTO get_analytic_profiles()

Retrieve a list of analytic tenant profiles

This API allows you to retrieve a list of profiles available for analytic tenants.   Note: Administrating tenants only.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.profile_management
from visier.api.profile_management.models.profiles_get_api_response_dto import ProfilesGetAPIResponseDTO
from visier.api.profile_management.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.profile_management.Configuration(
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
configuration = visier.api.profile_management.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.profile_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.profile_management.ProfileManagementApi(api_client)

    try:
        # Retrieve a list of analytic tenant profiles
        api_response = api_instance.get_analytic_profiles()
        print("The response of ProfileManagementApi->get_analytic_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileManagementApi->get_analytic_profiles: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ProfilesGetAPIResponseDTO**](ProfilesGetAPIResponseDTO.md)

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

# **get_analytic_user_profile**
> AllProfileAssignedForAccessibleTenantDTO get_analytic_user_profile(user_id)

Retrieve an administrating tenant user's analytic tenant profiles

This API allows you to retrieve a specified user's assigned profiles for analytic tenants.   Note: Administrating tenants only.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.profile_management
from visier.api.profile_management.models.all_profile_assigned_for_accessible_tenant_dto import AllProfileAssignedForAccessibleTenantDTO
from visier.api.profile_management.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.profile_management.Configuration(
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
configuration = visier.api.profile_management.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.profile_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.profile_management.ProfileManagementApi(api_client)
    user_id = 'user_id_example' # str | The ID of the user you want to retrieve.

    try:
        # Retrieve an administrating tenant user's analytic tenant profiles
        api_response = api_instance.get_analytic_user_profile(user_id)
        print("The response of ProfileManagementApi->get_analytic_user_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileManagementApi->get_analytic_user_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user you want to retrieve. | 

### Return type

[**AllProfileAssignedForAccessibleTenantDTO**](AllProfileAssignedForAccessibleTenantDTO.md)

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

# **get_profile_detail**
> ProfileGetAPIResponseDTO get_profile_detail(profile_id)

Retrieve the details of a profile

This API allows you to get the details of a specific profile. For administrating tenants, this retrieves  the details of administrating tenant profiles.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.profile_management
from visier.api.profile_management.models.profile_get_api_response_dto import ProfileGetAPIResponseDTO
from visier.api.profile_management.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.profile_management.Configuration(
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
configuration = visier.api.profile_management.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.profile_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.profile_management.ProfileManagementApi(api_client)
    profile_id = 'profile_id_example' # str | The ID of the profile to retrieve details for.

    try:
        # Retrieve the details of a profile
        api_response = api_instance.get_profile_detail(profile_id)
        print("The response of ProfileManagementApi->get_profile_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileManagementApi->get_profile_detail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The ID of the profile to retrieve details for. | 

### Return type

[**ProfileGetAPIResponseDTO**](ProfileGetAPIResponseDTO.md)

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

# **get_user_profile**
> AllProfileAssignedForLocalTenantDTO get_user_profile(user_id)

Retrieve a user's profiles

This API allows you to retrieve a specified user's assigned profiles. For administrating tenants,  this retrieves a user's administrating tenant profiles.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.profile_management
from visier.api.profile_management.models.all_profile_assigned_for_local_tenant_dto import AllProfileAssignedForLocalTenantDTO
from visier.api.profile_management.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.profile_management.Configuration(
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
configuration = visier.api.profile_management.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.profile_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.profile_management.ProfileManagementApi(api_client)
    user_id = 'user_id_example' # str | The ID of the user you want to retrieve.

    try:
        # Retrieve a user's profiles
        api_response = api_instance.get_user_profile(user_id)
        print("The response of ProfileManagementApi->get_user_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileManagementApi->get_user_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user you want to retrieve. | 

### Return type

[**AllProfileAssignedForLocalTenantDTO**](AllProfileAssignedForLocalTenantDTO.md)

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

# **remove_analytic_profile**
> AccessibleTenantProfileRevokeResponseDTO remove_analytic_profile(profile_id, accessible_tenant_profile_revoke_request_dto)

Remove an analytic tenant profile from administrating tenant users

This API allows you to remove an analytic tenant profile from a list of administrating tenant users for a list of analytic tenants.   Note: Administrating tenants only.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.profile_management
from visier.api.profile_management.models.accessible_tenant_profile_revoke_request_dto import AccessibleTenantProfileRevokeRequestDTO
from visier.api.profile_management.models.accessible_tenant_profile_revoke_response_dto import AccessibleTenantProfileRevokeResponseDTO
from visier.api.profile_management.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.profile_management.Configuration(
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
configuration = visier.api.profile_management.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.profile_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.profile_management.ProfileManagementApi(api_client)
    profile_id = 'profile_id_example' # str | The ID of the profile to remove.
    accessible_tenant_profile_revoke_request_dto = visier.api.profile_management.AccessibleTenantProfileRevokeRequestDTO() # AccessibleTenantProfileRevokeRequestDTO | 

    try:
        # Remove an analytic tenant profile from administrating tenant users
        api_response = api_instance.remove_analytic_profile(profile_id, accessible_tenant_profile_revoke_request_dto)
        print("The response of ProfileManagementApi->remove_analytic_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileManagementApi->remove_analytic_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The ID of the profile to remove. | 
 **accessible_tenant_profile_revoke_request_dto** | [**AccessibleTenantProfileRevokeRequestDTO**](AccessibleTenantProfileRevokeRequestDTO.md)|  | 

### Return type

[**AccessibleTenantProfileRevokeResponseDTO**](AccessibleTenantProfileRevokeResponseDTO.md)

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

# **remove_profile**
> LocalTenantProfileRevokeResponseDTO remove_profile(profile_id, local_tenant_profile_revoke_request_dto)

Remove a profile from a list of users

This API allows you to remove a profile from a list of users. For administrating tenants, this  removes an administrating tenant profile from a list of users.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):
* OAuth Authentication (OAuth2Auth):
* OAuth Authentication (OAuth2Auth):
* Bearer Authentication (BearerAuth):

```python
import visier.api.profile_management
from visier.api.profile_management.models.local_tenant_profile_revoke_request_dto import LocalTenantProfileRevokeRequestDTO
from visier.api.profile_management.models.local_tenant_profile_revoke_response_dto import LocalTenantProfileRevokeResponseDTO
from visier.api.profile_management.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.profile_management.Configuration(
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
configuration = visier.api.profile_management.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with visier.api.profile_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.profile_management.ProfileManagementApi(api_client)
    profile_id = 'profile_id_example' # str | The ID of the profile to remove to a list of users.
    local_tenant_profile_revoke_request_dto = visier.api.profile_management.LocalTenantProfileRevokeRequestDTO() # LocalTenantProfileRevokeRequestDTO | 

    try:
        # Remove a profile from a list of users
        api_response = api_instance.remove_profile(profile_id, local_tenant_profile_revoke_request_dto)
        print("The response of ProfileManagementApi->remove_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileManagementApi->remove_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The ID of the profile to remove to a list of users. | 
 **local_tenant_profile_revoke_request_dto** | [**LocalTenantProfileRevokeRequestDTO**](LocalTenantProfileRevokeRequestDTO.md)|  | 

### Return type

[**LocalTenantProfileRevokeResponseDTO**](LocalTenantProfileRevokeResponseDTO.md)

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

