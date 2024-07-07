# CellDistributionOptionsDTO

Cell distribution options for queries.  Include with aggregation queries to enable distribution calculation per cell.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bin_count** | **int** | The number of bins to return, minimum of 2, and a maximum of 100. | [optional] 

## Example

```python
from visier.model_query.models.cell_distribution_options_dto import CellDistributionOptionsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CellDistributionOptionsDTO from a JSON string
cell_distribution_options_dto_instance = CellDistributionOptionsDTO.from_json(json)
# print the JSON string representation of the object
print(CellDistributionOptionsDTO.to_json())

# convert the object into a dict
cell_distribution_options_dto_dict = cell_distribution_options_dto_instance.to_dict()
# create an instance of CellDistributionOptionsDTO from a dict
cell_distribution_options_dto_from_dict = CellDistributionOptionsDTO.from_dict(cell_distribution_options_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


