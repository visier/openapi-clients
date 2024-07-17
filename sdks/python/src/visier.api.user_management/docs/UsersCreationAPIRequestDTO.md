# UsersCreationAPIRequestDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[UserCreationAPIRequestDTO]**](UserCreationAPIRequestDTO.md) | A list of objects representing users to create. Maximum 100 users can be created in a single request. | [optional] 

## Example

```python
from visier.api.user_management.models.users_creation_api_request_dto import UsersCreationAPIRequestDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UsersCreationAPIRequestDTO from a JSON string
users_creation_api_request_dto_instance = UsersCreationAPIRequestDTO.from_json(json)
# print the JSON string representation of the object
print(UsersCreationAPIRequestDTO.to_json())

# convert the object into a dict
users_creation_api_request_dto_dict = users_creation_api_request_dto_instance.to_dict()
# create an instance of UsersCreationAPIRequestDTO from a dict
users_creation_api_request_dto_from_dict = UsersCreationAPIRequestDTO.from_dict(users_creation_api_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


