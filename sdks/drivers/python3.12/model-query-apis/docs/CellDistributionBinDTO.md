# CellDistributionBinDTO

A cell distribution bin.  Each bin has a metric value (of the bin) and the number of observations contributing to the bin.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**support** | **str** |  | [optional] 

## Example

```python
from visier.model_query.models.cell_distribution_bin_dto import CellDistributionBinDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CellDistributionBinDTO from a JSON string
cell_distribution_bin_dto_instance = CellDistributionBinDTO.from_json(json)
# print the JSON string representation of the object
print(CellDistributionBinDTO.to_json())

# convert the object into a dict
cell_distribution_bin_dto_dict = cell_distribution_bin_dto_instance.to_dict()
# create an instance of CellDistributionBinDTO from a dict
cell_distribution_bin_dto_from_dict = CellDistributionBinDTO.from_dict(cell_distribution_bin_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


