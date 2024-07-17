# UsersAPIFailureDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | An identifiable name to display within Visier. For example, \&quot;John Smith\&quot;. | [optional] 
**error** | [**UsersAPIErrorMessageDTO**](UsersAPIErrorMessageDTO.md) | The error thrown during creation. | [optional] 
**user_id** | **str** | The unique identifier associated with the user. | [optional] 
**user_name** | **str** | The user&#39;s username. This is typically the user&#39;s email, such as john@jupiter.com. | [optional] 

## Example

```python
from visier.api.user_management.models.users_api_failure_dto import UsersAPIFailureDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UsersAPIFailureDTO from a JSON string
users_api_failure_dto_instance = UsersAPIFailureDTO.from_json(json)
# print the JSON string representation of the object
print(UsersAPIFailureDTO.to_json())

# convert the object into a dict
users_api_failure_dto_dict = users_api_failure_dto_instance.to_dict()
# create an instance of UsersAPIFailureDTO from a dict
users_api_failure_dto_from_dict = UsersAPIFailureDTO.from_dict(users_api_failure_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


