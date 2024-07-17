# SecurablePropertyDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analytic_object_id** | **str** | The property&#39;s analytic object ID. | [optional] 
**display_name** | **str** | An identifiable property name to display in Visier, such as \&quot;Job Pay Level\&quot;. | [optional] 
**is_primary_key** | **bool** | If true, this property is the analytic object&#39;s primary key. | [optional] 
**property_id** | **str** | The property ID. | [optional] 
**reference_symbol_name** | **str** | The reference symbol name. | [optional] 

## Example

```python
from visier.api.permission_management.models.securable_property_dto import SecurablePropertyDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SecurablePropertyDTO from a JSON string
securable_property_dto_instance = SecurablePropertyDTO.from_json(json)
# print the JSON string representation of the object
print(SecurablePropertyDTO.to_json())

# convert the object into a dict
securable_property_dto_dict = securable_property_dto_instance.to_dict()
# create an instance of SecurablePropertyDTO from a dict
securable_property_dto_from_dict = SecurablePropertyDTO.from_dict(securable_property_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


