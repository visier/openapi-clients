# UserGroupDeleteSuccessDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_code** | **str** | The code of the tenant the user group was deleted from. | [optional] 
**user_group_id** | **str** | The unique identifier of the user group that was deleted. | [optional] 

## Example

```python
from visier.api.user_management.models.user_group_delete_success_dto import UserGroupDeleteSuccessDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupDeleteSuccessDTO from a JSON string
user_group_delete_success_dto_instance = UserGroupDeleteSuccessDTO.from_json(json)
# print the JSON string representation of the object
print(UserGroupDeleteSuccessDTO.to_json())

# convert the object into a dict
user_group_delete_success_dto_dict = user_group_delete_success_dto_instance.to_dict()
# create an instance of UserGroupDeleteSuccessDTO from a dict
user_group_delete_success_dto_from_dict = UserGroupDeleteSuccessDTO.from_dict(user_group_delete_success_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


