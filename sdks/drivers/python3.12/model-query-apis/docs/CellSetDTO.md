# CellSetDTO

The set of cells returned from executing an aggregation query.  A CellSet represents a structured, multidimensional array of values.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cells** | [**List[CellDTO]**](CellDTO.md) | The set of cells that represent the result of your query. | [optional] 
**axes** | [**List[CellSetAxisDTO]**](CellSetAxisDTO.md) | The set of axes for the cell set that represent the objects the data is grouped by. | [optional] 
**lineage** | [**LineageDTO**](LineageDTO.md) | Lineage information for this cell set. This can be omitted if the cell has no lineage or the user did not request lineage information. | [optional] 

## Example

```python
from visier.model_query.models.cell_set_dto import CellSetDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CellSetDTO from a JSON string
cell_set_dto_instance = CellSetDTO.from_json(json)
# print the JSON string representation of the object
print(CellSetDTO.to_json())

# convert the object into a dict
cell_set_dto_dict = cell_set_dto_instance.to_dict()
# create an instance of CellSetDTO from a dict
cell_set_dto_from_dict = CellSetDTO.from_dict(cell_set_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


