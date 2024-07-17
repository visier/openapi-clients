# StaticDimensionFilterDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimension_id** | **str** | The dimension ID associated with the filter. | [optional] 
**dimension_status** | **str** | The dimension&#39;s validity status. Valid values: Valid, NoData, NotFound.  * **Valid**: The object exists and has loaded data.  * **NoData**: The object exists but doesn&#39;t have loaded data.  * **NotFound**: The object doesn&#39;t exist. | [optional] 
**member_selections** | [**List[MemberSelectionDTO]**](MemberSelectionDTO.md) | A list of objects representing the dimension members assigned population access in the member filter. | [optional] 
**subject_reference_path** | **List[str]** | The subject reference path. | [optional] 

## Example

```python
from visier.api.permission_management.models.static_dimension_filter_dto import StaticDimensionFilterDTO

# TODO update the JSON string below
json = "{}"
# create an instance of StaticDimensionFilterDTO from a JSON string
static_dimension_filter_dto_instance = StaticDimensionFilterDTO.from_json(json)
# print the JSON string representation of the object
print(StaticDimensionFilterDTO.to_json())

# convert the object into a dict
static_dimension_filter_dto_dict = static_dimension_filter_dto_instance.to_dict()
# create an instance of StaticDimensionFilterDTO from a dict
static_dimension_filter_dto_from_dict = StaticDimensionFilterDTO.from_dict(static_dimension_filter_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


