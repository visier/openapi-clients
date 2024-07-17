# UserGroupGetAPIResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | An identifiable user group name to display in Visier, such as \&quot;Leadership User Group\&quot;. | [optional] 
**permissions** | [**List[PermissionResponseDTO]**](PermissionResponseDTO.md) | A list of objects representing the user&#39;s permissions. | [optional] 
**user_group_id** | **str** | The unique identifier associated with the user group. | [optional] 

## Example

```python
from visier.api.user_management.models.user_group_get_api_response_dto import UserGroupGetAPIResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupGetAPIResponseDTO from a JSON string
user_group_get_api_response_dto_instance = UserGroupGetAPIResponseDTO.from_json(json)
# print the JSON string representation of the object
print(UserGroupGetAPIResponseDTO.to_json())

# convert the object into a dict
user_group_get_api_response_dto_dict = user_group_get_api_response_dto_instance.to_dict()
# create an instance of UserGroupGetAPIResponseDTO from a dict
user_group_get_api_response_dto_from_dict = UserGroupGetAPIResponseDTO.from_dict(user_group_get_api_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


