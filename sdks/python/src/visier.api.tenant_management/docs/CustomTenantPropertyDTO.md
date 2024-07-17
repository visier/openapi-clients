# CustomTenantPropertyDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from visier.api.tenant_management.models.custom_tenant_property_dto import CustomTenantPropertyDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CustomTenantPropertyDTO from a JSON string
custom_tenant_property_dto_instance = CustomTenantPropertyDTO.from_json(json)
# print the JSON string representation of the object
print(CustomTenantPropertyDTO.to_json())

# convert the object into a dict
custom_tenant_property_dto_dict = custom_tenant_property_dto_instance.to_dict()
# create an instance of CustomTenantPropertyDTO from a dict
custom_tenant_property_dto_from_dict = CustomTenantPropertyDTO.from_dict(custom_tenant_property_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


