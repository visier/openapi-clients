# AssignRevokePermissionByPermissionDTO

The results of the permission assignment or removal.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permission** | [**PermissionAssignedForLocalTenantDTO**](PermissionAssignedForLocalTenantDTO.md) |  | [optional] 
**users** | [**List[AssignRevokePermissionByUserDTO]**](AssignRevokePermissionByUserDTO.md) | A list of objects representing the users that was permission was assigned to or removed from. | [optional] 

## Example

```python
from visier.api.user_management.models.assign_revoke_permission_by_permission_dto import AssignRevokePermissionByPermissionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AssignRevokePermissionByPermissionDTO from a JSON string
assign_revoke_permission_by_permission_dto_instance = AssignRevokePermissionByPermissionDTO.from_json(json)
# print the JSON string representation of the object
print(AssignRevokePermissionByPermissionDTO.to_json())

# convert the object into a dict
assign_revoke_permission_by_permission_dto_dict = assign_revoke_permission_by_permission_dto_instance.to_dict()
# create an instance of AssignRevokePermissionByPermissionDTO from a dict
assign_revoke_permission_by_permission_dto_from_dict = AssignRevokePermissionByPermissionDTO.from_dict(assign_revoke_permission_by_permission_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


