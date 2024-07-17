# UserGroupAssignedForLocalTenantDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | An identifiable user group name to display in Visier, such as \&quot;Leadership User Group\&quot;. | [optional] 
**user_group_id** | **str** | The user group ID. | [optional] 

## Example

```python
from visier.api.user_management.models.user_group_assigned_for_local_tenant_dto import UserGroupAssignedForLocalTenantDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupAssignedForLocalTenantDTO from a JSON string
user_group_assigned_for_local_tenant_dto_instance = UserGroupAssignedForLocalTenantDTO.from_json(json)
# print the JSON string representation of the object
print(UserGroupAssignedForLocalTenantDTO.to_json())

# convert the object into a dict
user_group_assigned_for_local_tenant_dto_dict = user_group_assigned_for_local_tenant_dto_instance.to_dict()
# create an instance of UserGroupAssignedForLocalTenantDTO from a dict
user_group_assigned_for_local_tenant_dto_from_dict = UserGroupAssignedForLocalTenantDTO.from_dict(user_group_assigned_for_local_tenant_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


