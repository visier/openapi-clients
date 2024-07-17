# AdminCapabilityConfigDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_capabilities_access** | **bool** | If &#x60;true&#x60;, the permission has all possible capabilities. | [optional] 
**capabilities** | **List[str]** | A list of the capabilities assigned in the permission. Not required if &#x60;allCapabilitiesAccess&#x60; is true. | [optional] 

## Example

```python
from visier.api.permission_management.models.admin_capability_config_dto import AdminCapabilityConfigDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AdminCapabilityConfigDTO from a JSON string
admin_capability_config_dto_instance = AdminCapabilityConfigDTO.from_json(json)
# print the JSON string representation of the object
print(AdminCapabilityConfigDTO.to_json())

# convert the object into a dict
admin_capability_config_dto_dict = admin_capability_config_dto_instance.to_dict()
# create an instance of AdminCapabilityConfigDTO from a dict
admin_capability_config_dto_from_dict = AdminCapabilityConfigDTO.from_dict(admin_capability_config_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


