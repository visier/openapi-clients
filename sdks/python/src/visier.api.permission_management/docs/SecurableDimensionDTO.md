# SecurableDimensionDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analytic_object_ids** | **List[str]** | A list of analytic object IDs. | [optional] 
**dimension_id** | **str** | The dimension ID. | [optional] 
**display_name** | **str** | An identifiable dimension name to display in Visier, such as \&quot;Contract Type\&quot;. | [optional] 
**hierarchy_properties** | [**List[HierarchyPropertyDTO]**](HierarchyPropertyDTO.md) | The list of hierarchies you can map to a user in a permission&#39;s dynamic filter. | [optional] 

## Example

```python
from visier.api.permission_management.models.securable_dimension_dto import SecurableDimensionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SecurableDimensionDTO from a JSON string
securable_dimension_dto_instance = SecurableDimensionDTO.from_json(json)
# print the JSON string representation of the object
print(SecurableDimensionDTO.to_json())

# convert the object into a dict
securable_dimension_dto_dict = securable_dimension_dto_instance.to_dict()
# create an instance of SecurableDimensionDTO from a dict
securable_dimension_dto_from_dict = SecurableDimensionDTO.from_dict(securable_dimension_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


