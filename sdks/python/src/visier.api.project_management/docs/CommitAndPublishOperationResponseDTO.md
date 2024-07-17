# CommitAndPublishOperationResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**published_version** | [**ProjectDTO**](ProjectDTO.md) | The project version that was published to production. | [optional] 

## Example

```python
from visier.api.project_management.models.commit_and_publish_operation_response_dto import CommitAndPublishOperationResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CommitAndPublishOperationResponseDTO from a JSON string
commit_and_publish_operation_response_dto_instance = CommitAndPublishOperationResponseDTO.from_json(json)
# print the JSON string representation of the object
print(CommitAndPublishOperationResponseDTO.to_json())

# convert the object into a dict
commit_and_publish_operation_response_dto_dict = commit_and_publish_operation_response_dto_instance.to_dict()
# create an instance of CommitAndPublishOperationResponseDTO from a dict
commit_and_publish_operation_response_dto_from_dict = CommitAndPublishOperationResponseDTO.from_dict(commit_and_publish_operation_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


