# DimensionFilterDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dynamic_dimension_filter** | [**DynamicDimensionFilterDTO**](DynamicDimensionFilterDTO.md) |  | [optional] 
**static_dimension_filter** | [**StaticDimensionFilterDTO**](StaticDimensionFilterDTO.md) |  | [optional] 

## Example

```python
from visier.api.permission_management.models.dimension_filter_dto import DimensionFilterDTO

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


