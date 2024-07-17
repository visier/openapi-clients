# UserGetAPIResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_enabled** | **bool** | If false, the user account is disabled. | [optional] 
**display_name** | **str** | An identifiable name to display within Visier. For example, \&quot;John Smith\&quot;. | [optional] 
**email** | **str** | The user&#39;s email address. | [optional] 
**employee_id** | **str** | If applicable, and if available, the user employee ID in the data. | [optional] 
**last_login** | [**LastLoginDTO**](LastLoginDTO.md) | An object that represents the time that the user last logged into Visier. | [optional] 
**permissions** | [**AllPermissionsAssignedForLocalTenantDTO**](AllPermissionsAssignedForLocalTenantDTO.md) | A list of objects representing the user&#39;s permissions. | [optional] 
**profiles** | [**AllProfileAssignedForLocalTenantDTO**](AllProfileAssignedForLocalTenantDTO.md) | A list of objects representing the list of available profiles. | [optional] 
**user_groups** | [**AllUserGroupsAssignedForLocalTenantDTO**](AllUserGroupsAssignedForLocalTenantDTO.md) | A list of objects representing the available user groups. | [optional] 
**user_id** | **str** | The unique identifier associated with the user. | [optional] 
**username** | **str** | The user&#39;s username. This is typically the user&#39;s email, such as john@jupiter.com. | [optional] 

## Example

```python
from visier.api.user_management.models.user_get_api_response_dto import UserGetAPIResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UserGetAPIResponseDTO from a JSON string
user_get_api_response_dto_instance = UserGetAPIResponseDTO.from_json(json)
# print the JSON string representation of the object
print(UserGetAPIResponseDTO.to_json())

# convert the object into a dict
user_get_api_response_dto_dict = user_get_api_response_dto_instance.to_dict()
# create an instance of UserGetAPIResponseDTO from a dict
user_get_api_response_dto_from_dict = UserGetAPIResponseDTO.from_dict(user_get_api_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


