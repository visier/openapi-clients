# DynamicPropertyMappingDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hierarchy_property_id** | **str** | The unique ID of the property. | [optional] 
**hierarchy_property_status** | **str** | The property&#39;s validity status. Valid values: &#x60;Valid&#x60;, &#x60;NotFound&#x60;.  * **Valid**: The object exists and has loaded data.  * **NotFound**: The object doesn&#39;t exist. | [optional] 
**user_property** | [**UserPropertyDTO**](UserPropertyDTO.md) | The user property that you want to link the name property or organization head to. | [optional] 

## Example

```python
from visier.api.permission_management.models.dynamic_property_mapping_dto import DynamicPropertyMappingDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicPropertyMappingDTO from a JSON string
dynamic_property_mapping_dto_instance = DynamicPropertyMappingDTO.from_json(json)
# print the JSON string representation of the object
print(DynamicPropertyMappingDTO.to_json())

# convert the object into a dict
dynamic_property_mapping_dto_dict = dynamic_property_mapping_dto_instance.to_dict()
# create an instance of DynamicPropertyMappingDTO from a dict
dynamic_property_mapping_dto_from_dict = DynamicPropertyMappingDTO.from_dict(dynamic_property_mapping_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


