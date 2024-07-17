# PermissionAssignedUserDTO

The user and the method through which the user was assigned the permission.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permission_from** | **str** | The method through which the user was assigned the permission. The permission may be assigned through  the following options:   - User: The permission was directly assigned to the user.   - UserGroup: The permission was assigned because the user belongs to a user group that is assigned the permission.   - UserAndUserGroup: The permission was directly assigned to the user and assigned because the user belongs to     a user group that is assigned the permission. | [optional] 
**user_id** | **str** | The unique identifier associated with the user. | [optional] 
**username** | **str** | The user&#39;s username. This is typically the user&#39;s email, such as john@visier.com. | [optional] 

## Example

```python
from visier.api.user_management.models.permission_assigned_user_dto import PermissionAssignedUserDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionAssignedUserDTO from a JSON string
permission_assigned_user_dto_instance = PermissionAssignedUserDTO.from_json(json)
# print the JSON string representation of the object
print(PermissionAssignedUserDTO.to_json())

# convert the object into a dict
permission_assigned_user_dto_dict = permission_assigned_user_dto_instance.to_dict()
# create an instance of PermissionAssignedUserDTO from a dict
permission_assigned_user_dto_from_dict = PermissionAssignedUserDTO.from_dict(permission_assigned_user_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


