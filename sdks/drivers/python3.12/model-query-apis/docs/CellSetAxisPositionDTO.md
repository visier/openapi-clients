# CellSetAxisPositionDTO

The position along the axis of a cell set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **List[str]** | A list of strings representing the members within a dimension path. For example,  a dimension for Location may have the paths \&quot;Canada, BC, Vancouver\&quot; and \&quot;US, California, San Francisco\&quot;. | [optional] 
**display_name** | **str** | The display name of the position. This is optional and is omitted if unavailable or not requested. | [optional] 
**display_name_path** | **List[str]** | Optional display name path of the member. | [optional] 

## Example

```python
from visier.model_query.models.cell_set_axis_position_dto import CellSetAxisPositionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CellSetAxisPositionDTO from a JSON string
cell_set_axis_position_dto_instance = CellSetAxisPositionDTO.from_json(json)
# print the JSON string representation of the object
print(CellSetAxisPositionDTO.to_json())

# convert the object into a dict
cell_set_axis_position_dto_dict = cell_set_axis_position_dto_instance.to_dict()
# create an instance of CellSetAxisPositionDTO from a dict
cell_set_axis_position_dto_from_dict = CellSetAxisPositionDTO.from_dict(cell_set_axis_position_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


