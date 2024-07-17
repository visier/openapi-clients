# LineageDTO

Lineage information for a given cell set. This describes how a cell set is created from other cell sets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cell_sets** | [**List[CellSetDTO]**](CellSetDTO.md) | The cell sets that constitute this lineage. | [optional] 
**op** | **str** | The operation used to combine the cell sets of this lineage. | [optional] 

## Example

```python
from visier.api.model_query.models.lineage_dto import LineageDTO

# TODO update the JSON string below
json = "{}"
# create an instance of LineageDTO from a JSON string
lineage_dto_instance = LineageDTO.from_json(json)
# print the JSON string representation of the object
print(LineageDTO.to_json())

# convert the object into a dict
lineage_dto_dict = lineage_dto_instance.to_dict()
# create an instance of LineageDTO from a dict
lineage_dto_from_dict = LineageDTO.from_dict(lineage_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


