# UserGroupsChangeDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_groups** | [**List[UserGroupChangeDefinitionDTO]**](UserGroupChangeDefinitionDTO.md) | The user groups and their definitions. | [optional] 

## Example

```python
from visier.api.user_management.models.user_groups_change_dto import UserGroupsChangeDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupsChangeDTO from a JSON string
user_groups_change_dto_instance = UserGroupsChangeDTO.from_json(json)
# print the JSON string representation of the object
print(UserGroupsChangeDTO.to_json())

# convert the object into a dict
user_groups_change_dto_dict = user_groups_change_dto_instance.to_dict()
# create an instance of UserGroupsChangeDTO from a dict
user_groups_change_dto_from_dict = UserGroupsChangeDTO.from_dict(user_groups_change_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


