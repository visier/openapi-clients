# AllPermissionsAssignedForLocalTenantDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigned_permissions** | [**List[PermissionAssignedForLocalTenantDTO]**](PermissionAssignedForLocalTenantDTO.md) | A list of objects representing the user&#39;s permissions. | [optional] 

## Example

```python
from visier.api.user_management.models.all_permissions_assigned_for_local_tenant_dto import AllPermissionsAssignedForLocalTenantDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AllPermissionsAssignedForLocalTenantDTO from a JSON string
all_permissions_assigned_for_local_tenant_dto_instance = AllPermissionsAssignedForLocalTenantDTO.from_json(json)
# print the JSON string representation of the object
print(AllPermissionsAssignedForLocalTenantDTO.to_json())

# convert the object into a dict
all_permissions_assigned_for_local_tenant_dto_dict = all_permissions_assigned_for_local_tenant_dto_instance.to_dict()
# create an instance of AllPermissionsAssignedForLocalTenantDTO from a dict
all_permissions_assigned_for_local_tenant_dto_from_dict = AllPermissionsAssignedForLocalTenantDTO.from_dict(all_permissions_assigned_for_local_tenant_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


