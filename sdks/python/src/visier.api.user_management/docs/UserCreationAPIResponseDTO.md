# UserCreationAPIResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_enabled** | **str** | If true, the user account is enabled. | [optional] 
**display_name** | **str** | An identifiable name to display within Visier. For example, \&quot;John Smith\&quot;. | [optional] 
**email** | **str** | The user&#39;s email address. | [optional] 
**employee_id** | **str** | If applicable, and if available, the user employee ID in the data. | [optional] 
**user_id** | **str** | The unique identifier associated with the user. | [optional] 
**username** | **str** | The user&#39;s username. This is typically the user&#39;s email, such as john@jupiter.com. | [optional] 

## Example

```python
from visier.api.user_management.models.user_creation_api_response_dto import UserCreationAPIResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UserCreationAPIResponseDTO from a JSON string
user_creation_api_response_dto_instance = UserCreationAPIResponseDTO.from_json(json)
# print the JSON string representation of the object
print(UserCreationAPIResponseDTO.to_json())

# convert the object into a dict
user_creation_api_response_dto_dict = user_creation_api_response_dto_instance.to_dict()
# create an instance of UserCreationAPIResponseDTO from a dict
user_creation_api_response_dto_from_dict = UserCreationAPIResponseDTO.from_dict(user_creation_api_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


