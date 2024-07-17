# RoleModulesConfigDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_package_ids** | **List[str]** | The unique IDs of the content packages assigned to the permission. | [optional] 

## Example

```python
from visier.api.permission_management.models.role_modules_config_dto import RoleModulesConfigDTO

# TODO update the JSON string below
json = "{}"
# create an instance of RoleModulesConfigDTO from a JSON string
role_modules_config_dto_instance = RoleModulesConfigDTO.from_json(json)
# print the JSON string representation of the object
print(RoleModulesConfigDTO.to_json())

# convert the object into a dict
role_modules_config_dto_dict = role_modules_config_dto_instance.to_dict()
# create an instance of RoleModulesConfigDTO from a dict
role_modules_config_dto_from_dict = RoleModulesConfigDTO.from_dict(role_modules_config_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


