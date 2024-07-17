# UserGroupSingleDeleteResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failure** | [**UserGroupDeleteFailureDTO**](UserGroupDeleteFailureDTO.md) | The user group was not successfully deleted. | [optional] 
**success** | [**UserGroupDeleteSuccessDTO**](UserGroupDeleteSuccessDTO.md) | The user group was successfully deleted. | [optional] 

## Example

```python
from visier.api.user_management.models.user_group_single_delete_response_dto import UserGroupSingleDeleteResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupSingleDeleteResponseDTO from a JSON string
user_group_single_delete_response_dto_instance = UserGroupSingleDeleteResponseDTO.from_json(json)
# print the JSON string representation of the object
print(UserGroupSingleDeleteResponseDTO.to_json())

# convert the object into a dict
user_group_single_delete_response_dto_dict = user_group_single_delete_response_dto_instance.to_dict()
# create an instance of UserGroupSingleDeleteResponseDTO from a dict
user_group_single_delete_response_dto_from_dict = UserGroupSingleDeleteResponseDTO.from_dict(user_group_single_delete_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


