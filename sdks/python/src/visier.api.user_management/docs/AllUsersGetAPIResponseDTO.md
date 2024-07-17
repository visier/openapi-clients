# AllUsersGetAPIResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The number of results to return. The maximum number of users to retrieve is 1000. | [optional] 
**start** | **int** | The index to start retrieving results from, also known as offset. The index begins at 0. | [optional] 
**users** | [**List[UserGetAPIResponseDTO]**](UserGetAPIResponseDTO.md) | A list of available users. | [optional] 

## Example

```python
from visier.api.user_management.models.all_users_get_api_response_dto import AllUsersGetAPIResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AllUsersGetAPIResponseDTO from a JSON string
all_users_get_api_response_dto_instance = AllUsersGetAPIResponseDTO.from_json(json)
# print the JSON string representation of the object
print(AllUsersGetAPIResponseDTO.to_json())

# convert the object into a dict
all_users_get_api_response_dto_dict = all_users_get_api_response_dto_instance.to_dict()
# create an instance of AllUsersGetAPIResponseDTO from a dict
all_users_get_api_response_dto_from_dict = AllUsersGetAPIResponseDTO.from_dict(all_users_get_api_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


