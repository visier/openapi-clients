# UsersUpdateAPIUserDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_enabled** | **str** | If true, the user account is enabled. | [optional] 
**display_name** | **str** | An identifiable name to display within Visier. For example, \&quot;John Smith\&quot;. | [optional] 
**email** | **str** | The user&#39;s email address. | [optional] 
**employee_id** | **str** | If applicable, and if available, the user employee ID in the data. | [optional] 
**user_id** | **str** | The unique identifier associated with the user. | [optional] 

## Example

```python
from visier.api.user_management.models.users_update_api_user_dto import UsersUpdateAPIUserDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UsersUpdateAPIUserDTO from a JSON string
users_update_api_user_dto_instance = UsersUpdateAPIUserDTO.from_json(json)
# print the JSON string representation of the object
print(UsersUpdateAPIUserDTO.to_json())

# convert the object into a dict
users_update_api_user_dto_dict = users_update_api_user_dto_instance.to_dict()
# create an instance of UsersUpdateAPIUserDTO from a dict
users_update_api_user_dto_from_dict = UsersUpdateAPIUserDTO.from_dict(users_update_api_user_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


