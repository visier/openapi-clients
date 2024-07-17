# UserGroupDeleteResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failures** | [**List[UserGroupDeleteFailureDTO]**](UserGroupDeleteFailureDTO.md) | The user groups that were not deleted successfully. | [optional] 
**successes** | [**List[UserGroupDeleteSuccessDTO]**](UserGroupDeleteSuccessDTO.md) | The user groups that were successfully deleted. | [optional] 

## Example

```python
from visier.api.user_management.models.user_group_delete_response_dto import UserGroupDeleteResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupDeleteResponseDTO from a JSON string
user_group_delete_response_dto_instance = UserGroupDeleteResponseDTO.from_json(json)
# print the JSON string representation of the object
print(UserGroupDeleteResponseDTO.to_json())

# convert the object into a dict
user_group_delete_response_dto_dict = user_group_delete_response_dto_instance.to_dict()
# create an instance of UserGroupDeleteResponseDTO from a dict
user_group_delete_response_dto_from_dict = UserGroupDeleteResponseDTO.from_dict(user_group_delete_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


