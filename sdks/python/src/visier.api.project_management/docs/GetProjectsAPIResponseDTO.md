# GetProjectsAPIResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approval_projects** | [**List[ProjectDTO]**](ProjectDTO.md) | A list of objects representing the accessible approval projects for the user. | [optional] 
**archived_projects** | [**List[ProjectDTO]**](ProjectDTO.md) | A list of objects representing the accessible archived projects for the user. | [optional] 
**open_projects** | [**List[ProjectDTO]**](ProjectDTO.md) | A list of objects representing the accessible open projects for the user. | [optional] 
**rejected_projects** | [**List[ProjectDTO]**](ProjectDTO.md) | A list of objects representing the accessible rejected projects for the user. | [optional] 

## Example

```python
from visier.api.project_management.models.get_projects_api_response_dto import GetProjectsAPIResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of GetProjectsAPIResponseDTO from a JSON string
get_projects_api_response_dto_instance = GetProjectsAPIResponseDTO.from_json(json)
# print the JSON string representation of the object
print(GetProjectsAPIResponseDTO.to_json())

# convert the object into a dict
get_projects_api_response_dto_dict = get_projects_api_response_dto_instance.to_dict()
# create an instance of GetProjectsAPIResponseDTO from a dict
get_projects_api_response_dto_from_dict = GetProjectsAPIResponseDTO.from_dict(get_projects_api_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


