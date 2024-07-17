# UserGroupsGetAPIResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The number of results to return. The maximum number of users to retrieve is 1000. | [optional] 
**start** | **int** | The index to start retrieving results from, also known as offset. | [optional] 
**user_groups** | [**List[UserGroupGetAPIResponseDTO]**](UserGroupGetAPIResponseDTO.md) | A list of user groups. | [optional] 

## Example

```python
from visier.api.user_management.models.user_groups_get_api_response_dto import UserGroupsGetAPIResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupsGetAPIResponseDTO from a JSON string
user_groups_get_api_response_dto_instance = UserGroupsGetAPIResponseDTO.from_json(json)
# print the JSON string representation of the object
print(UserGroupsGetAPIResponseDTO.to_json())

# convert the object into a dict
user_groups_get_api_response_dto_dict = user_groups_get_api_response_dto_instance.to_dict()
# create an instance of UserGroupsGetAPIResponseDTO from a dict
user_groups_get_api_response_dto_from_dict = UserGroupsGetAPIResponseDTO.from_dict(user_groups_get_api_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


