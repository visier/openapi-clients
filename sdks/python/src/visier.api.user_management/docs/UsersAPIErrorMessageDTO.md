# UsersAPIErrorMessageDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Error message | [optional] 
**rci** | **str** | The unique identifier associated to this error | [optional] 

## Example

```python
from visier.api.user_management.models.users_api_error_message_dto import UsersAPIErrorMessageDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UsersAPIErrorMessageDTO from a JSON string
users_api_error_message_dto_instance = UsersAPIErrorMessageDTO.from_json(json)
# print the JSON string representation of the object
print(UsersAPIErrorMessageDTO.to_json())

# convert the object into a dict
users_api_error_message_dto_dict = users_api_error_message_dto_instance.to_dict()
# create an instance of UsersAPIErrorMessageDTO from a dict
users_api_error_message_dto_from_dict = UsersAPIErrorMessageDTO.from_dict(users_api_error_message_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


