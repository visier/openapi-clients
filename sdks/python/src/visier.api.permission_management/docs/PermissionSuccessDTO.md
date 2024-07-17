# PermissionSuccessDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | An identifiable permission name to display in Visier, such as \&quot;Diversity Access\&quot;. | [optional] 
**permission_id** | **str** | The unique identifier associated with the permission. | [optional] 

## Example

```python
from visier.api.permission_management.models.permission_success_dto import PermissionSuccessDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionSuccessDTO from a JSON string
permission_success_dto_instance = PermissionSuccessDTO.from_json(json)
# print the JSON string representation of the object
print(PermissionSuccessDTO.to_json())

# convert the object into a dict
permission_success_dto_dict = permission_success_dto_instance.to_dict()
# create an instance of PermissionSuccessDTO from a dict
permission_success_dto_from_dict = PermissionSuccessDTO.from_dict(permission_success_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


