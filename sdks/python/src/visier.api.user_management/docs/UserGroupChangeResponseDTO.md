# UserGroupChangeResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failures** | [**List[UserGroupChangeFailureDTO]**](UserGroupChangeFailureDTO.md) | The user groups that were not created. | [optional] 
**successes** | [**List[UserGroupChangeSuccessDTO]**](UserGroupChangeSuccessDTO.md) | The user groups that were created. | [optional] 

## Example

```python
from visier.api.user_management.models.user_group_change_response_dto import UserGroupChangeResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupChangeResponseDTO from a JSON string
user_group_change_response_dto_instance = UserGroupChangeResponseDTO.from_json(json)
# print the JSON string representation of the object
print(UserGroupChangeResponseDTO.to_json())

# convert the object into a dict
user_group_change_response_dto_dict = user_group_change_response_dto_instance.to_dict()
# create an instance of UserGroupChangeResponseDTO from a dict
user_group_change_response_dto_from_dict = UserGroupChangeResponseDTO.from_dict(user_group_change_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


