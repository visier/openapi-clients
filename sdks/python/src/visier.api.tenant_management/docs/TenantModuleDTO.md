# TenantModuleDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | An identifiable name that is displayed within Visier. For example, \&quot;TALENT\&quot;. | [optional] 
**module_settings** | [**ModuleSettingsDTO**](ModuleSettingsDTO.md) | The settings associated with the module. | [optional] 
**symbol_name** | **str** | The symbol name of the module. For example, \&quot;Talent_Management\&quot;. | [optional] 

## Example

```python
from visier.api.tenant_management.models.tenant_module_dto import TenantModuleDTO

# TODO update the JSON string below
json = "{}"
# create an instance of TenantModuleDTO from a JSON string
tenant_module_dto_instance = TenantModuleDTO.from_json(json)
# print the JSON string representation of the object
print(TenantModuleDTO.to_json())

# convert the object into a dict
tenant_module_dto_dict = tenant_module_dto_instance.to_dict()
# create an instance of TenantModuleDTO from a dict
tenant_module_dto_from_dict = TenantModuleDTO.from_dict(tenant_module_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


