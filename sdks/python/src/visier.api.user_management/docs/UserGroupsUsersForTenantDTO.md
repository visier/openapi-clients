# UserGroupsUsersForTenantDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_code** | **str** | The unique identifier associated with the tenant. | [optional] 
**users** | [**List[SimpleUserDTO]**](SimpleUserDTO.md) | A list of objects representing the users in the user group. | [optional] 

## Example

```python
from visier.api.user_management.models.user_groups_users_for_tenant_dto import UserGroupsUsersForTenantDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupsUsersForTenantDTO from a JSON string
user_groups_users_for_tenant_dto_instance = UserGroupsUsersForTenantDTO.from_json(json)
# print the JSON string representation of the object
print(UserGroupsUsersForTenantDTO.to_json())

# convert the object into a dict
user_groups_users_for_tenant_dto_dict = user_groups_users_for_tenant_dto_instance.to_dict()
# create an instance of UserGroupsUsersForTenantDTO from a dict
user_groups_users_for_tenant_dto_from_dict = UserGroupsUsersForTenantDTO.from_dict(user_groups_users_for_tenant_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


