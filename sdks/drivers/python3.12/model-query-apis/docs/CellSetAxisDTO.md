# CellSetAxisDTO

The axis of a cell set associated with a dimension.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimension** | [**DimensionReferenceDTO**](DimensionReferenceDTO.md) | The dimension associated with the axis. | [optional] 
**positions** | [**List[CellSetAxisPositionDTO]**](CellSetAxisPositionDTO.md) | A list of paths that represent the data&#39;s positions along the axis. | [optional] 

## Example

```python
from visier.model_query.models.cell_set_axis_dto import CellSetAxisDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CellSetAxisDTO from a JSON string
cell_set_axis_dto_instance = CellSetAxisDTO.from_json(json)
# print the JSON string representation of the object
print(CellSetAxisDTO.to_json())

# convert the object into a dict
cell_set_axis_dto_dict = cell_set_axis_dto_instance.to_dict()
# create an instance of CellSetAxisDTO from a dict
cell_set_axis_dto_from_dict = CellSetAxisDTO.from_dict(cell_set_axis_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


