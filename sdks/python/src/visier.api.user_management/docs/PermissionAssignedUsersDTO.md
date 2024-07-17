# PermissionAssignedUsersDTO

Users that are assigned a specific permission.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The number of results to return. The maximum number of tenants to retrieve is 100. | [optional] 
**start** | **int** | The index to start retrieving results from, also known as offset. The index begins at 0. | [optional] 
**tenants** | [**List[PermissionAssignedByTenantDTO]**](PermissionAssignedByTenantDTO.md) | A list of objects representing the users that are assigned the specific permission, organized by the tenants the users belong to. | [optional] 

## Example

```python
from visier.api.user_management.models.permission_assigned_users_dto import PermissionAssignedUsersDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionAssignedUsersDTO from a JSON string
permission_assigned_users_dto_instance = PermissionAssignedUsersDTO.from_json(json)
# print the JSON string representation of the object
print(PermissionAssignedUsersDTO.to_json())

# convert the object into a dict
permission_assigned_users_dto_dict = permission_assigned_users_dto_instance.to_dict()
# create an instance of PermissionAssignedUsersDTO from a dict
permission_assigned_users_dto_from_dict = PermissionAssignedUsersDTO.from_dict(permission_assigned_users_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


