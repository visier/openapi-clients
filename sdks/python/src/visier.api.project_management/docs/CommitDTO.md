# CommitDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A description of the committed change. | [optional] 
**id** | **str** | The unique ID of the committed change. | [optional] 
**name** | **str** | An identifiable name of the committed change to display in Visier. | [optional] 

## Example

```python
from visier.api.project_management.models.commit_dto import CommitDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CommitDTO from a JSON string
commit_dto_instance = CommitDTO.from_json(json)
# print the JSON string representation of the object
print(CommitDTO.to_json())

# convert the object into a dict
commit_dto_dict = commit_dto_instance.to_dict()
# create an instance of CommitDTO from a dict
commit_dto_from_dict = CommitDTO.from_dict(commit_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


