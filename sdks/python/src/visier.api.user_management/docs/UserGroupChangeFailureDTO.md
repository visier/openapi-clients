# UserGroupChangeFailureDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The display name of the user group that couldn&#39;t be created. | [optional] 
**message** | **str** | The error message containing the cause of the failure. | [optional] 
**rci** | **str** | The root cause identifier to provide to Visier Technical Support if you require further troubleshooting. | [optional] 
**tenant_code** | **str** | The code of the tenant for which the user group could not be created or updated. | [optional] 

## Example

```python
from visier.api.user_management.models.user_group_change_failure_dto import UserGroupChangeFailureDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupChangeFailureDTO from a JSON string
user_group_change_failure_dto_instance = UserGroupChangeFailureDTO.from_json(json)
# print the JSON string representation of the object
print(UserGroupChangeFailureDTO.to_json())

# convert the object into a dict
user_group_change_failure_dto_dict = user_group_change_failure_dto_instance.to_dict()
# create an instance of UserGroupChangeFailureDTO from a dict
user_group_change_failure_dto_from_dict = UserGroupChangeFailureDTO.from_dict(user_group_change_failure_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


