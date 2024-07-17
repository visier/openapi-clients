# UserUpdateAPIRequestDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_enabled** | **str** | If true, the user account is enabled. | [optional] 
**display_name** | **str** | An identifiable name to display within Visier. For example, \&quot;John Smith\&quot;. | [optional] 
**email** | **str** | The user&#39;s email address. | [optional] 
**employee_id** | **str** | If applicable, and if available, the user employee ID in the data. | [optional] 

## Example

```python
from visier.api.user_management.models.user_update_api_request_dto import UserUpdateAPIRequestDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UserUpdateAPIRequestDTO from a JSON string
user_update_api_request_dto_instance = UserUpdateAPIRequestDTO.from_json(json)
# print the JSON string representation of the object
print(UserUpdateAPIRequestDTO.to_json())

# convert the object into a dict
user_update_api_request_dto_dict = user_update_api_request_dto_instance.to_dict()
# create an instance of UserUpdateAPIRequestDTO from a dict
user_update_api_request_dto_from_dict = UserUpdateAPIRequestDTO.from_dict(user_update_api_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


