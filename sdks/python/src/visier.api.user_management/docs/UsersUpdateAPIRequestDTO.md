# UsersUpdateAPIRequestDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[UsersUpdateAPIUserDTO]**](UsersUpdateAPIUserDTO.md) | A list of objects representing users to update. Maximum 100 users can be updated in a single request. | [optional] 

## Example

```python
from visier.api.user_management.models.users_update_api_request_dto import UsersUpdateAPIRequestDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UsersUpdateAPIRequestDTO from a JSON string
users_update_api_request_dto_instance = UsersUpdateAPIRequestDTO.from_json(json)
# print the JSON string representation of the object
print(UsersUpdateAPIRequestDTO.to_json())

# convert the object into a dict
users_update_api_request_dto_dict = users_update_api_request_dto_instance.to_dict()
# create an instance of UsersUpdateAPIRequestDTO from a dict
users_update_api_request_dto_from_dict = UsersUpdateAPIRequestDTO.from_dict(users_update_api_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


