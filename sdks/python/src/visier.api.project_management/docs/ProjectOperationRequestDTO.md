# ProjectOperationRequestDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** | The operation to perform on a draft project. Valid values:  * &#x60;commitAndPublish&#x60;: Commits the requesting user&#39;s changes and publishes the draft project to production. | [optional] 

## Example

```python
from visier.api.project_management.models.project_operation_request_dto import ProjectOperationRequestDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectOperationRequestDTO from a JSON string
project_operation_request_dto_instance = ProjectOperationRequestDTO.from_json(json)
# print the JSON string representation of the object
print(ProjectOperationRequestDTO.to_json())

# convert the object into a dict
project_operation_request_dto_dict = project_operation_request_dto_instance.to_dict()
# create an instance of ProjectOperationRequestDTO from a dict
project_operation_request_dto_from_dict = ProjectOperationRequestDTO.from_dict(project_operation_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


