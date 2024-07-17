# UserGroupDeleteFailureDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The error message containing the cause of the failure. | [optional] 
**rci** | **str** | The root cause identifier to provide to Visier Technical Support if you require further troubleshooting. | [optional] 
**tenant_code** | **str** | The code of the tenant from which the user group could not be deleted. | [optional] 
**user_group_id** | **str** | The unique identifier of the user group that could not be deleted. | [optional] 

## Example

```python
from visier.api.user_management.models.user_group_delete_failure_dto import UserGroupDeleteFailureDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupDeleteFailureDTO from a JSON string
user_group_delete_failure_dto_instance = UserGroupDeleteFailureDTO.from_json(json)
# print the JSON string representation of the object
print(UserGroupDeleteFailureDTO.to_json())

# convert the object into a dict
user_group_delete_failure_dto_dict = user_group_delete_failure_dto_instance.to_dict()
# create an instance of UserGroupDeleteFailureDTO from a dict
user_group_delete_failure_dto_from_dict = UserGroupDeleteFailureDTO.from_dict(user_group_delete_failure_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


