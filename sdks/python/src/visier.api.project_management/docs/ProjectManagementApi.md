# visier.api.project_management.ProjectManagementApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project**](ProjectManagementApi.md#create_project) | **POST** /v1alpha/admin/projects | Create a new draft project
[**delete_project**](ProjectManagementApi.md#delete_project) | **DELETE** /v1alpha/admin/projects/{projectId} | Delete a draft project
[**get_project**](ProjectManagementApi.md#get_project) | **GET** /v1alpha/admin/projects/{projectId} | Retrieve a draft project&#39;s information
[**get_project_commits**](ProjectManagementApi.md#get_project_commits) | **GET** /v1alpha/admin/projects/{projectId}/commits | Retrieve a list of all committed changes in a project
[**get_projects**](ProjectManagementApi.md#get_projects) | **GET** /v1alpha/admin/projects | Retrieve a list of draft projects accessible to the user
[**run_project_operation**](ProjectManagementApi.md#run_project_operation) | **POST** /v1alpha/admin/projects/{projectId} | Perform an operation on a draft project


# **create_project**
> ProjectDTO create_project(project_dto)

Create a new draft project

*  This API allows you to create a new draft project in the tenant.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example


```python
import visier.api.project_management
from visier.api.project_management.models.project_dto import ProjectDTO
from visier.api.project_management.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.project_management.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with visier.api.project_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.project_management.ProjectManagementApi(api_client)
    project_dto = visier.api.project_management.ProjectDTO() # ProjectDTO | 

    try:
        # Create a new draft project
        api_response = api_instance.create_project(project_dto)
        print("The response of ProjectManagementApi->create_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementApi->create_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_dto** | [**ProjectDTO**](ProjectDTO.md)|  | 

### Return type

[**ProjectDTO**](ProjectDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> ProjectDTO delete_project(project_id)

Delete a draft project

*  This API allows you to delete a draft project in the tenant. The project will first be archived if applicable.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example


```python
import visier.api.project_management
from visier.api.project_management.models.project_dto import ProjectDTO
from visier.api.project_management.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.project_management.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with visier.api.project_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.project_management.ProjectManagementApi(api_client)
    project_id = 'project_id_example' # str | The unique ID of the draft project to be deleted.

    try:
        # Delete a draft project
        api_response = api_instance.delete_project(project_id)
        print("The response of ProjectManagementApi->delete_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementApi->delete_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The unique ID of the draft project to be deleted. | 

### Return type

[**ProjectDTO**](ProjectDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> ProjectDTO get_project(project_id, var_with=var_with, limit=limit)

Retrieve a draft project's information

*  This API allows you to retrieve the details of an accessible draft project. You must know the ID of the project to retrieve its details. To retrieve draft project IDs, see `GET v1alpha/admin/projects`.   A project is accessible if it is owned by the user or shared to the user.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example


```python
import visier.api.project_management
from visier.api.project_management.models.project_dto import ProjectDTO
from visier.api.project_management.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.project_management.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with visier.api.project_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.project_management.ProjectManagementApi(api_client)
    project_id = 'project_id_example' # str | 
    var_with = ['var_with_example'] # List[str] | The types of draft projects to include in the request response.  * If empty, returns all the `Open` draft projects.  * If `Open`, returns all Open draft projects.  * If `Approval`, returns all draft projects in the approval stage. Changes cannot made in Approval projects.  * If `Rejected`, returns all draft projects that have been rejected. Changes cannot be committed in Rejected projects.  * If `Archived`, returns all draft projects that have been archived. Changes cannot be committed in Archived projects. (optional)
    limit = 56 # int | The number of projects to return per type. The maximum number of projects to retrieve per type is 1000. The default is 100. (optional)

    try:
        # Retrieve a draft project's information
        api_response = api_instance.get_project(project_id, var_with=var_with, limit=limit)
        print("The response of ProjectManagementApi->get_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementApi->get_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **var_with** | [**List[str]**](str.md)| The types of draft projects to include in the request response.  * If empty, returns all the &#x60;Open&#x60; draft projects.  * If &#x60;Open&#x60;, returns all Open draft projects.  * If &#x60;Approval&#x60;, returns all draft projects in the approval stage. Changes cannot made in Approval projects.  * If &#x60;Rejected&#x60;, returns all draft projects that have been rejected. Changes cannot be committed in Rejected projects.  * If &#x60;Archived&#x60;, returns all draft projects that have been archived. Changes cannot be committed in Archived projects. | [optional] 
 **limit** | **int**| The number of projects to return per type. The maximum number of projects to retrieve per type is 1000. The default is 100. | [optional] 

### Return type

[**ProjectDTO**](ProjectDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_commits**
> GetProjectCommitsAPIResponseDTO get_project_commits(project_id, limit=limit, start=start)

Retrieve a list of all committed changes in a project

*  This API allows you to retrieve the full list of all committed changes in a project.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example


```python
import visier.api.project_management
from visier.api.project_management.models.get_project_commits_api_response_dto import GetProjectCommitsAPIResponseDTO
from visier.api.project_management.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.project_management.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with visier.api.project_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.project_management.ProjectManagementApi(api_client)
    project_id = 'project_id_example' # str | The unique identifier of the draft project you want to retrieve the committed changes for.
    limit = 56 # int | The maximum number of committed changes to return. Default is 400. (optional)
    start = 56 # int | The starting index of the first committed change to return. Default is 0. (optional)

    try:
        # Retrieve a list of all committed changes in a project
        api_response = api_instance.get_project_commits(project_id, limit=limit, start=start)
        print("The response of ProjectManagementApi->get_project_commits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementApi->get_project_commits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The unique identifier of the draft project you want to retrieve the committed changes for. | 
 **limit** | **int**| The maximum number of committed changes to return. Default is 400. | [optional] 
 **start** | **int**| The starting index of the first committed change to return. Default is 0. | [optional] 

### Return type

[**GetProjectCommitsAPIResponseDTO**](GetProjectCommitsAPIResponseDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects**
> GetProjectsAPIResponseDTO get_projects(var_with=var_with, limit=limit)

Retrieve a list of draft projects accessible to the user

*  This API allows you to get a list of draft projects accessible to the requesting user in the tenant.   A project is accessible if it is owned by the user or shared to the user.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example


```python
import visier.api.project_management
from visier.api.project_management.models.get_projects_api_response_dto import GetProjectsAPIResponseDTO
from visier.api.project_management.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.project_management.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with visier.api.project_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.project_management.ProjectManagementApi(api_client)
    var_with = ['var_with_example'] # List[str] | The types of draft projects to include in the request response.  * If empty, returns all the `Open` draft projects.  * If `Open`, returns all Open draft projects.  * If `Approval`, returns all draft projects in the approval stage. Changes cannot made in Approval projects.  * If `Rejected`, returns all draft projects that have been rejected. Changes cannot be committed in Rejected projects.  * If `Archived`, returns all draft projects that have been archived. Changes cannot be committed in Archived projects. (optional)
    limit = 56 # int | The number of projects to return per type. The maximum number of projects to retrieve per type is 1000. The default is 100. (optional)

    try:
        # Retrieve a list of draft projects accessible to the user
        api_response = api_instance.get_projects(var_with=var_with, limit=limit)
        print("The response of ProjectManagementApi->get_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementApi->get_projects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_with** | [**List[str]**](str.md)| The types of draft projects to include in the request response.  * If empty, returns all the &#x60;Open&#x60; draft projects.  * If &#x60;Open&#x60;, returns all Open draft projects.  * If &#x60;Approval&#x60;, returns all draft projects in the approval stage. Changes cannot made in Approval projects.  * If &#x60;Rejected&#x60;, returns all draft projects that have been rejected. Changes cannot be committed in Rejected projects.  * If &#x60;Archived&#x60;, returns all draft projects that have been archived. Changes cannot be committed in Archived projects. | [optional] 
 **limit** | **int**| The number of projects to return per type. The maximum number of projects to retrieve per type is 1000. The default is 100. | [optional] 

### Return type

[**GetProjectsAPIResponseDTO**](GetProjectsAPIResponseDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_project_operation**
> ProjectOperationResponseDTO run_project_operation(project_id, project_operation_request_dto)

Perform an operation on a draft project

*  This API allows you to perform operations on a draft project. The following operations are supported:  * `commitAndPublish`: Commits project changes and publishes the project to production.   <br>**Note:** <em>This API is in **alpha**. While in alpha, APIs may change in a breaking way without notice; functionality may be removed, and no deprecation notices will be issued.  If you are interested in using this API, please contact your Customer Success Manager (CSM).</em>

### Example


```python
import visier.api.project_management
from visier.api.project_management.models.project_operation_request_dto import ProjectOperationRequestDTO
from visier.api.project_management.models.project_operation_response_dto import ProjectOperationResponseDTO
from visier.api.project_management.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = visier.api.project_management.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with visier.api.project_management.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = visier.api.project_management.ProjectManagementApi(api_client)
    project_id = 'project_id_example' # str | 
    project_operation_request_dto = visier.api.project_management.ProjectOperationRequestDTO() # ProjectOperationRequestDTO | 

    try:
        # Perform an operation on a draft project
        api_response = api_instance.run_project_operation(project_id, project_operation_request_dto)
        print("The response of ProjectManagementApi->run_project_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementApi->run_project_operation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **project_operation_request_dto** | [**ProjectOperationRequestDTO**](ProjectOperationRequestDTO.md)|  | 

### Return type

[**ProjectOperationResponseDTO**](ProjectOperationResponseDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

