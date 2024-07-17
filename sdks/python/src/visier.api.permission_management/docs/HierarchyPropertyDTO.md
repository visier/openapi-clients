# HierarchyPropertyDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | An identifiable property name to display in Visier, such as \&quot;Name Property\&quot;. | [optional] 
**hierarchy_property_id** | **str** | The unique ID of the property. | [optional] 

## Example

```python
from visier.api.permission_management.models.hierarchy_property_dto import HierarchyPropertyDTO

# TODO update the JSON string below
json = "{}"
# create an instance of HierarchyPropertyDTO from a JSON string
hierarchy_property_dto_instance = HierarchyPropertyDTO.from_json(json)
# print the JSON string representation of the object
print(HierarchyPropertyDTO.to_json())

# convert the object into a dict
hierarchy_property_dto_dict = hierarchy_property_dto_instance.to_dict()
# create an instance of HierarchyPropertyDTO from a dict
hierarchy_property_dto_from_dict = HierarchyPropertyDTO.from_dict(hierarchy_property_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


