# PermissionResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | An identifiable permission name to display in Visier, such as \&quot;Diversity Access\&quot;. | [optional] 
**permission_id** | **str** | The unique identifier associated with the permission. | [optional] 

## Example

```python
from visier.api.user_management.models.permission_response_dto import PermissionResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionResponseDTO from a JSON string
permission_response_dto_instance = PermissionResponseDTO.from_json(json)
# print the JSON string representation of the object
print(PermissionResponseDTO.to_json())

# convert the object into a dict
permission_response_dto_dict = permission_response_dto_instance.to_dict()
# create an instance of PermissionResponseDTO from a dict
permission_response_dto_from_dict = PermissionResponseDTO.from_dict(permission_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


