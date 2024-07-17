# UsersAPIResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failures** | [**List[UsersAPIFailureDTO]**](UsersAPIFailureDTO.md) | The users for which the request failed. | [optional] 
**successes** | [**List[UsersAPISuccessDTO]**](UsersAPISuccessDTO.md) | The users for which the request succeeded. | [optional] 

## Example

```python
from visier.api.user_management.models.users_api_response_dto import UsersAPIResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UsersAPIResponseDTO from a JSON string
users_api_response_dto_instance = UsersAPIResponseDTO.from_json(json)
# print the JSON string representation of the object
print(UsersAPIResponseDTO.to_json())

# convert the object into a dict
users_api_response_dto_dict = users_api_response_dto_instance.to_dict()
# create an instance of UsersAPIResponseDTO from a dict
users_api_response_dto_from_dict = UsersAPIResponseDTO.from_dict(users_api_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


