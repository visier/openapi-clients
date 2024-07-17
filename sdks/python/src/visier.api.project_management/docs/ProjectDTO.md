# ProjectDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capabilities** | **List[str]** | The current user&#39;s capabilities for the project. Users with &#x60;canWrite&#x60;, &#x60;canShare&#x60;, or &#x60;owner&#x60; capabilities can add and commit changes to the project.  **canRead**: The project has been shared to the user with &#x60;View&#x60; access.  **canWrite**: The project has been shared to the user with &#x60;Edit&#x60; access.  **canShare**: The project has been shared to the user with &#x60;Share&#x60; access.  **owner**: The user is the owner of the project.  Omit when creating a new project. | [optional] 
**description** | **str** | A description of the project. | [optional] 
**id** | **str** | The unique ID of the project. Omit when creating a new project. | [optional] 
**name** | **str** | An identifiable project name to display in Visier. | [optional] 
**release_version** | **str** | The release version of the project. | [optional] 
**ticket_number** | **str** | The change management ticket number of the project. | [optional] 
**version_number** | **int** | The version number of the project. | [optional] 

## Example

```python
from visier.api.project_management.models.project_dto import ProjectDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDTO from a JSON string
project_dto_instance = ProjectDTO.from_json(json)
# print the JSON string representation of the object
print(ProjectDTO.to_json())

# convert the object into a dict
project_dto_dict = project_dto_instance.to_dict()
# create an instance of ProjectDTO from a dict
project_dto_from_dict = ProjectDTO.from_dict(project_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


