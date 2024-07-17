# GetProjectCommitsAPIResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commits** | [**List[CommitDTO]**](CommitDTO.md) | A list of committed changes in the project. | [optional] 

## Example

```python
from visier.api.project_management.models.get_project_commits_api_response_dto import GetProjectCommitsAPIResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of GetProjectCommitsAPIResponseDTO from a JSON string
get_project_commits_api_response_dto_instance = GetProjectCommitsAPIResponseDTO.from_json(json)
# print the JSON string representation of the object
print(GetProjectCommitsAPIResponseDTO.to_json())

# convert the object into a dict
get_project_commits_api_response_dto_dict = get_project_commits_api_response_dto_instance.to_dict()
# create an instance of GetProjectCommitsAPIResponseDTO from a dict
get_project_commits_api_response_dto_from_dict = GetProjectCommitsAPIResponseDTO.from_dict(get_project_commits_api_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


