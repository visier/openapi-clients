# UsersToUserGroupsRequestDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_groups** | [**List[UsersToUserGroupRequestDTO]**](UsersToUserGroupRequestDTO.md) | A list of objects representing the user groups and users to assign or remove. | [optional] 

## Example

```python
from visier.api.user_management.models.users_to_user_groups_request_dto import UsersToUserGroupsRequestDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UsersToUserGroupsRequestDTO from a JSON string
users_to_user_groups_request_dto_instance = UsersToUserGroupsRequestDTO.from_json(json)
# print the JSON string representation of the object
print(UsersToUserGroupsRequestDTO.to_json())

# convert the object into a dict
users_to_user_groups_request_dto_dict = users_to_user_groups_request_dto_instance.to_dict()
# create an instance of UsersToUserGroupsRequestDTO from a dict
users_to_user_groups_request_dto_from_dict = UsersToUserGroupsRequestDTO.from_dict(users_to_user_groups_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


