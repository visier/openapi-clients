# UserGroupChangeSuccessDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The display name of the created user group. | [optional] 
**tenant_code** | **str** | The code of the tenant the user group was created or updated in. | [optional] 
**user_group_id** | **str** | The unique identifier of the user group. | [optional] 

## Example

```python
from visier.api.user_management.models.user_group_change_success_dto import UserGroupChangeSuccessDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupChangeSuccessDTO from a JSON string
user_group_change_success_dto_instance = UserGroupChangeSuccessDTO.from_json(json)
# print the JSON string representation of the object
print(UserGroupChangeSuccessDTO.to_json())

# convert the object into a dict
user_group_change_success_dto_dict = user_group_change_success_dto_instance.to_dict()
# create an instance of UserGroupChangeSuccessDTO from a dict
user_group_change_success_dto_from_dict = UserGroupChangeSuccessDTO.from_dict(user_group_change_success_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


