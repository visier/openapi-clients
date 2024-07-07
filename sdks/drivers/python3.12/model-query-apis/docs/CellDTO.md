# CellDTO

An individual value in a cell set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The value of the cell. | [optional] 
**support** | **str** | The number of data points contributing to this cell. | [optional] 
**coordinates** | **List[int]** | A list of integers representing the coordinates of this cell, identifying its position along each axis. | [optional] 
**distribution** | [**List[CellDistributionBinDTO]**](CellDistributionBinDTO.md) | The optional distribution of this cell.  This will be populated if distribution calculation is requested, and supported by the query. | [optional] 

## Example

```python
from visier.model_query.models.cell_dto import CellDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CellDTO from a JSON string
cell_dto_instance = CellDTO.from_json(json)
# print the JSON string representation of the object
print(CellDTO.to_json())

# convert the object into a dict
cell_dto_dict = cell_dto_instance.to_dict()
# create an instance of CellDTO from a dict
cell_dto_from_dict = CellDTO.from_dict(cell_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


