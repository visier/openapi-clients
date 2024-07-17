# DimensionsDTO

A collection of dimensions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimensions** | [**List[DimensionDTO]**](DimensionDTO.md) |  | [optional] 

## Example

```python
from visier.api.model_query.models.dimensions_dto import DimensionsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DimensionsDTO from a JSON string
dimensions_dto_instance = DimensionsDTO.from_json(json)
# print the JSON string representation of the object
print(DimensionsDTO.to_json())

# convert the object into a dict
dimensions_dto_dict = dimensions_dto_instance.to_dict()
# create an instance of DimensionsDTO from a dict
dimensions_dto_from_dict = DimensionsDTO.from_dict(dimensions_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


