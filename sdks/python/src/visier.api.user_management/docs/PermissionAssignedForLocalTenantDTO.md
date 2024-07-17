# PermissionAssignedForLocalTenantDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A user-defined description of the permission. | [optional] 
**display_name** | **str** | An identifiable permission name to display in Visier, such as \&quot;Diversity Access\&quot;. | [optional] 
**permission_id** | **str** | The unique identifier associated with the permission. | [optional] 

## Example

```python
from visier.api.user_management.models.permission_assigned_for_local_tenant_dto import PermissionAssignedForLocalTenantDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionAssignedForLocalTenantDTO from a JSON string
permission_assigned_for_local_tenant_dto_instance = PermissionAssignedForLocalTenantDTO.from_json(json)
# print the JSON string representation of the object
print(PermissionAssignedForLocalTenantDTO.to_json())

# convert the object into a dict
permission_assigned_for_local_tenant_dto_dict = permission_assigned_for_local_tenant_dto_instance.to_dict()
# create an instance of PermissionAssignedForLocalTenantDTO from a dict
permission_assigned_for_local_tenant_dto_from_dict = PermissionAssignedForLocalTenantDTO.from_dict(permission_assigned_for_local_tenant_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


