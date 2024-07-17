# UserGroupsUsersDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The limit of results to return. The maximum value is 1000. | [optional] 
**start** | **int** | The index to start retrieving values from, also known as offset. The index begins at 0. | [optional] 
**tenants** | [**List[UserGroupsUsersForTenantDTO]**](UserGroupsUsersForTenantDTO.md) | A list of objects representing the users that are explicitly assigned to the user group, organized by the tenants the users belong to. | [optional] 

## Example

```python
from visier.api.user_management.models.user_groups_users_dto import UserGroupsUsersDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupsUsersDTO from a JSON string
user_groups_users_dto_instance = UserGroupsUsersDTO.from_json(json)
# print the JSON string representation of the object
print(UserGroupsUsersDTO.to_json())

# convert the object into a dict
user_groups_users_dto_dict = user_groups_users_dto_instance.to_dict()
# create an instance of UserGroupsUsersDTO from a dict
user_groups_users_dto_from_dict = UserGroupsUsersDTO.from_dict(user_groups_users_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


