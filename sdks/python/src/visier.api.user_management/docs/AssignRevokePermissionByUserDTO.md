# AssignRevokePermissionByUserDTO

The results of the permission assignment or removal by user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A meaningful message about the user permission. | [optional] 
**user_id** | **str** | The unique identifier associated with the user. | [optional] 
**username** | **str** | The user&#39;s username. This is typically the user&#39;s email, such as john@visier.com. | [optional] 

## Example

```python
from visier.api.user_management.models.assign_revoke_permission_by_user_dto import AssignRevokePermissionByUserDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AssignRevokePermissionByUserDTO from a JSON string
assign_revoke_permission_by_user_dto_instance = AssignRevokePermissionByUserDTO.from_json(json)
# print the JSON string representation of the object
print(AssignRevokePermissionByUserDTO.to_json())

# convert the object into a dict
assign_revoke_permission_by_user_dto_dict = assign_revoke_permission_by_user_dto_instance.to_dict()
# create an instance of AssignRevokePermissionByUserDTO from a dict
assign_revoke_permission_by_user_dto_from_dict = AssignRevokePermissionByUserDTO.from_dict(assign_revoke_permission_by_user_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


