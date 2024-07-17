# AssignRevokePermissionsResponseDTO

The results of the permission assignment or removal.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenants** | [**List[AssignRevokePermissionByTenantDTO]**](AssignRevokePermissionByTenantDTO.md) | A list of objects representing the users that were assigned permissions, organized by the tenants the users belong to. | [optional] 

## Example

```python
from visier.api.user_management.models.assign_revoke_permissions_response_dto import AssignRevokePermissionsResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AssignRevokePermissionsResponseDTO from a JSON string
assign_revoke_permissions_response_dto_instance = AssignRevokePermissionsResponseDTO.from_json(json)
# print the JSON string representation of the object
print(AssignRevokePermissionsResponseDTO.to_json())

# convert the object into a dict
assign_revoke_permissions_response_dto_dict = assign_revoke_permissions_response_dto_instance.to_dict()
# create an instance of AssignRevokePermissionsResponseDTO from a dict
assign_revoke_permissions_response_dto_from_dict = AssignRevokePermissionsResponseDTO.from_dict(assign_revoke_permissions_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


