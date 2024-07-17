# UsersToUserGroupRequestDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_group_id** | **str** | The unique identifier associated with the user group. | [optional] 
**user_ids** | **List[str]** | A list of strings representing unique user IDs to assign to or remove from the user group. | [optional] 

## Example

```python
from visier.api.user_management.models.users_to_user_group_request_dto import UsersToUserGroupRequestDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UsersToUserGroupRequestDTO from a JSON string
users_to_user_group_request_dto_instance = UsersToUserGroupRequestDTO.from_json(json)
# print the JSON string representation of the object
print(UsersToUserGroupRequestDTO.to_json())

# convert the object into a dict
users_to_user_group_request_dto_dict = users_to_user_group_request_dto_instance.to_dict()
# create an instance of UsersToUserGroupRequestDTO from a dict
users_to_user_group_request_dto_from_dict = UsersToUserGroupRequestDTO.from_dict(users_to_user_group_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


