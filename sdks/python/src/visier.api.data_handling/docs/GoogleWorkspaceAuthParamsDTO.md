# GoogleWorkspaceAuthParamsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_code** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 

## Example

```python
from visier.api.data_handling.models.google_workspace_auth_params_dto import GoogleWorkspaceAuthParamsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleWorkspaceAuthParamsDTO from a JSON string
google_workspace_auth_params_dto_instance = GoogleWorkspaceAuthParamsDTO.from_json(json)
# print the JSON string representation of the object
print(GoogleWorkspaceAuthParamsDTO.to_json())

# convert the object into a dict
google_workspace_auth_params_dto_dict = google_workspace_auth_params_dto_instance.to_dict()
# create an instance of GoogleWorkspaceAuthParamsDTO from a dict
google_workspace_auth_params_dto_from_dict = GoogleWorkspaceAuthParamsDTO.from_dict(google_workspace_auth_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


