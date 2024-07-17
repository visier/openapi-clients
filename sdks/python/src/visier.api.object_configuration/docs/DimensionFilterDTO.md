# DimensionFilterDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimension_id** | **str** | The UUID of the dimension. | [optional] 
**dimension_members** | [**List[DimensionMemberDTO]**](DimensionMemberDTO.md) | A list of dimension members to map to the perspective node.   Note: If this array is empty, all dimension members will be removed for the node. | [optional] 
**symbol_name** | **str** | The symbol name of the dimension. | [optional] 

## Example

```python
from visier.api.object_configuration.models.dimension_filter_dto import DimensionFilterDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DimensionFilterDTO from a JSON string
dimension_filter_dto_instance = DimensionFilterDTO.from_json(json)
# print the JSON string representation of the object
print(DimensionFilterDTO.to_json())

# convert the object into a dict
dimension_filter_dto_dict = dimension_filter_dto_instance.to_dict()
# create an instance of DimensionFilterDTO from a dict
dimension_filter_dto_from_dict = DimensionFilterDTO.from_dict(dimension_filter_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


