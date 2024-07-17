# UsersDeleteAPIRequestDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_ids** | **List[str]** | A list of objects representing users to delete. Maximum 100 users can be deleted in a single request. | [optional] 

## Example

```python
from visier.api.user_management.models.users_delete_api_request_dto import UsersDeleteAPIRequestDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UsersDeleteAPIRequestDTO from a JSON string
users_delete_api_request_dto_instance = UsersDeleteAPIRequestDTO.from_json(json)
# print the JSON string representation of the object
print(UsersDeleteAPIRequestDTO.to_json())

# convert the object into a dict
users_delete_api_request_dto_dict = users_delete_api_request_dto_instance.to_dict()
# create an instance of UsersDeleteAPIRequestDTO from a dict
users_delete_api_request_dto_from_dict = UsersDeleteAPIRequestDTO.from_dict(users_delete_api_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


