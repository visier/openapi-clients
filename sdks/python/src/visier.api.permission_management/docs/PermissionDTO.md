# PermissionDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_capability_config** | [**AdminCapabilityConfigDTO**](AdminCapabilityConfigDTO.md) | The capabilities assigned in the permission. | [optional] 
**data_security_profiles** | [**List[DataSecurityProfileDTO]**](DataSecurityProfileDTO.md) | A list of objects representing the data security for each item in a permission. | [optional] 
**description** | **str** | A user-defined description of the permission. | [optional] 
**display_name** | **str** | An identifiable permission name to display in Visier, such as \&quot;Diversity Access\&quot;. | [optional] 
**permission_id** | **str** | The unique identifier associated with the permission. | [optional] 
**role_modules_config** | [**RoleModulesConfigDTO**](RoleModulesConfigDTO.md) | A list of content packages assigned to the permission. | [optional] 

## Example

```python
from visier.api.permission_management.models.permission_dto import PermissionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionDTO from a JSON string
permission_dto_instance = PermissionDTO.from_json(json)
# print the JSON string representation of the object
print(PermissionDTO.to_json())

# convert the object into a dict
permission_dto_dict = permission_dto_instance.to_dict()
# create an instance of PermissionDTO from a dict
permission_dto_from_dict = PermissionDTO.from_dict(permission_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


