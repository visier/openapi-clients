# UserCreationAPIRequestDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_enabled** | **str** | If false, the user account is disabled. | [optional] 
**display_name** | **str** | An identifiable name to display within Visier. For example, \&quot;John Smith\&quot;. | [optional] 
**email** | **str** | The user&#39;s email. This is used if the user&#39;s email is different from their username. For example, \&quot;john.doe@visier.com\&quot;. | [optional] 
**employee_id** | **str** | If applicable, and if available, the user employee ID in the data. | [optional] 
**username** | **str** | The user&#39;s username. This is typically the user&#39;s email, such as john@visier.com. | [optional] 

## Example

```python
from visier.api.user_management.models.user_creation_api_request_dto import UserCreationAPIRequestDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UserCreationAPIRequestDTO from a JSON string
user_creation_api_request_dto_instance = UserCreationAPIRequestDTO.from_json(json)
# print the JSON string representation of the object
print(UserCreationAPIRequestDTO.to_json())

# convert the object into a dict
user_creation_api_request_dto_dict = user_creation_api_request_dto_instance.to_dict()
# create an instance of UserCreationAPIRequestDTO from a dict
user_creation_api_request_dto_from_dict = UserCreationAPIRequestDTO.from_dict(user_creation_api_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


