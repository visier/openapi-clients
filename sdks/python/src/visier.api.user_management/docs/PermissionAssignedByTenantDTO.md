# PermissionAssignedByTenantDTO

The users assigned a specific permission, grouped by tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_code** | **str** | The unique identifier associated with the tenant. | [optional] 
**users** | [**List[PermissionAssignedUserDTO]**](PermissionAssignedUserDTO.md) | A list of objects representing the users that the permission is assigned to. | [optional] 

## Example

```python
from visier.api.user_management.models.permission_assigned_by_tenant_dto import PermissionAssignedByTenantDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionAssignedByTenantDTO from a JSON string
permission_assigned_by_tenant_dto_instance = PermissionAssignedByTenantDTO.from_json(json)
# print the JSON string representation of the object
print(PermissionAssignedByTenantDTO.to_json())

# convert the object into a dict
permission_assigned_by_tenant_dto_dict = permission_assigned_by_tenant_dto_instance.to_dict()
# create an instance of PermissionAssignedByTenantDTO from a dict
permission_assigned_by_tenant_dto_from_dict = PermissionAssignedByTenantDTO.from_dict(permission_assigned_by_tenant_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


