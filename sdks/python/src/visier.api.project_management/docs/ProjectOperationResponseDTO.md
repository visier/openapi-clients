# ProjectOperationResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit_and_publish** | [**CommitAndPublishOperationResponseDTO**](CommitAndPublishOperationResponseDTO.md) | The result of the &#x60;commitAndPublish&#x60; operation. | [optional] 

## Example

```python
from visier.api.project_management.models.project_operation_response_dto import ProjectOperationResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectOperationResponseDTO from a JSON string
project_operation_response_dto_instance = ProjectOperationResponseDTO.from_json(json)
# print the JSON string representation of the object
print(ProjectOperationResponseDTO.to_json())

# convert the object into a dict
project_operation_response_dto_dict = project_operation_response_dto_instance.to_dict()
# create an instance of ProjectOperationResponseDTO from a dict
project_operation_response_dto_from_dict = ProjectOperationResponseDTO.from_dict(project_operation_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


