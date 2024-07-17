# PermissionFailureDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | An identifiable permission name to display in Visier, such as \&quot;Diversity Access\&quot;. | [optional] 
**error** | [**PermissionErrorDTO**](PermissionErrorDTO.md) | The error associated with the failure. | [optional] 
**permission_id** | **str** | The unique identifier associated with the permission. | [optional] 

## Example

```python
from visier.api.permission_management.models.permission_failure_dto import PermissionFailureDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionFailureDTO from a JSON string
permission_failure_dto_instance = PermissionFailureDTO.from_json(json)
# print the JSON string representation of the object
print(PermissionFailureDTO.to_json())

# convert the object into a dict
permission_failure_dto_dict = permission_failure_dto_instance.to_dict()
# create an instance of PermissionFailureDTO from a dict
permission_failure_dto_from_dict = PermissionFailureDTO.from_dict(permission_failure_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


