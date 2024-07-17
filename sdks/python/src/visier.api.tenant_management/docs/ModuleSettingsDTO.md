# ModuleSettingsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locale** | **str** | The language of the module. For example, a module that is in English will have the locale \&quot;en\&quot;. | [optional] 
**special_handling_instruction** | **str** | An instruction message in the module selection dialog. This can be a note for administrators such as \&quot;Don&#39;t assign this module\&quot; or \&quot;Assign Module B instead\&quot;. | [optional] 
**unavailable_for_assignment** | **bool** | If true, the module cannot be assigned to tenants. | [optional] 

## Example

```python
from visier.api.tenant_management.models.module_settings_dto import ModuleSettingsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleSettingsDTO from a JSON string
module_settings_dto_instance = ModuleSettingsDTO.from_json(json)
# print the JSON string representation of the object
print(ModuleSettingsDTO.to_json())

# convert the object into a dict
module_settings_dto_dict = module_settings_dto_instance.to_dict()
# create an instance of ModuleSettingsDTO from a dict
module_settings_dto_from_dict = ModuleSettingsDTO.from_dict(module_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


