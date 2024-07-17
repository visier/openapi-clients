# UserGroupsDeleteRequestDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_groups** | [**List[UserGroupDeleteDTO]**](UserGroupDeleteDTO.md) | The user groups to delete. | [optional] 

## Example

```python
from visier.api.user_management.models.user_groups_delete_request_dto import UserGroupsDeleteRequestDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupsDeleteRequestDTO from a JSON string
user_groups_delete_request_dto_instance = UserGroupsDeleteRequestDTO.from_json(json)
# print the JSON string representation of the object
print(UserGroupsDeleteRequestDTO.to_json())

# convert the object into a dict
user_groups_delete_request_dto_dict = user_groups_delete_request_dto_instance.to_dict()
# create an instance of UserGroupsDeleteRequestDTO from a dict
user_groups_delete_request_dto_from_dict = UserGroupsDeleteRequestDTO.from_dict(user_groups_delete_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


