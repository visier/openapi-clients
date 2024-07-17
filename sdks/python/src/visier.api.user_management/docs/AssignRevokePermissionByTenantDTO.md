# AssignRevokePermissionByTenantDTO

The permissions organized by tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A detailed description of the request outcome, if available. | [optional] 
**permissions** | [**List[AssignRevokePermissionByPermissionDTO]**](AssignRevokePermissionByPermissionDTO.md) | A list of objects representing the assigned or removed permissions. | [optional] 
**status** | **str** | The state of the permission assignment. Valid values are Succeed or Failed. | [optional] 
**tenant_code** | **str** | The unique identifier associated with the tenant. | [optional] 

## Example

```python
from visier.api.user_management.models.assign_revoke_permission_by_tenant_dto import AssignRevokePermissionByTenantDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AssignRevokePermissionByTenantDTO from a JSON string
assign_revoke_permission_by_tenant_dto_instance = AssignRevokePermissionByTenantDTO.from_json(json)
# print the JSON string representation of the object
print(AssignRevokePermissionByTenantDTO.to_json())

# convert the object into a dict
assign_revoke_permission_by_tenant_dto_dict = assign_revoke_permission_by_tenant_dto_instance.to_dict()
# create an instance of AssignRevokePermissionByTenantDTO from a dict
assign_revoke_permission_by_tenant_dto_from_dict = AssignRevokePermissionByTenantDTO.from_dict(assign_revoke_permission_by_tenant_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


