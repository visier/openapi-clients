# PermissionErrorDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Error message | [optional] 
**rci** | **str** | A root cause identifier that allows Visier to determine the source of the problem. | [optional] 

## Example

```python
from visier.api.permission_management.models.permission_error_dto import PermissionErrorDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionErrorDTO from a JSON string
permission_error_dto_instance = PermissionErrorDTO.from_json(json)
# print the JSON string representation of the object
print(PermissionErrorDTO.to_json())

# convert the object into a dict
permission_error_dto_dict = permission_error_dto_instance.to_dict()
# create an instance of PermissionErrorDTO from a dict
permission_error_dto_from_dict = PermissionErrorDTO.from_dict(permission_error_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


