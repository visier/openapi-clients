# AllUserGroupsAssignedForLocalTenantDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigned_user_groups** | [**List[UserGroupAssignedForLocalTenantDTO]**](UserGroupAssignedForLocalTenantDTO.md) | A list of objects representing the available user groups. | [optional] 

## Example

```python
from visier.api.user_management.models.all_user_groups_assigned_for_local_tenant_dto import AllUserGroupsAssignedForLocalTenantDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AllUserGroupsAssignedForLocalTenantDTO from a JSON string
all_user_groups_assigned_for_local_tenant_dto_instance = AllUserGroupsAssignedForLocalTenantDTO.from_json(json)
# print the JSON string representation of the object
print(AllUserGroupsAssignedForLocalTenantDTO.to_json())

# convert the object into a dict
all_user_groups_assigned_for_local_tenant_dto_dict = all_user_groups_assigned_for_local_tenant_dto_instance.to_dict()
# create an instance of AllUserGroupsAssignedForLocalTenantDTO from a dict
all_user_groups_assigned_for_local_tenant_dto_from_dict = AllUserGroupsAssignedForLocalTenantDTO.from_dict(all_user_groups_assigned_for_local_tenant_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


