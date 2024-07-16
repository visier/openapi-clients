# QueryAxisDTO

An axis of a query used to group data points.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimension_data_member_selection** | [**QueryDimensionDataMemberSelectionDTO**](QueryDimensionDataMemberSelectionDTO.md) | An axis comprised of all leaf, including data, members of an existing dimension in Visier. | [optional] 
**dimension_leaf_member_selection** | [**QueryDimensionLeafSelectionDTO**](QueryDimensionLeafSelectionDTO.md) | An axis comprised of all non-data leaf members of an existing dimension in Visier. | [optional] 
**dimension_level_selection** | [**QueryDimensionLevelSelectionDTO**](QueryDimensionLevelSelectionDTO.md) | An axis that uses levels of existing dimensions in Visier. | [optional] 
**dimension_level_with_uncategorized_value_selection** | [**QueryDimensionLevelSelectionDTO**](QueryDimensionLevelSelectionDTO.md) | An axis that uses existing dimension levels in Visier, including uncategorized levels. | [optional] 
**dimension_member_selection** | [**QueryDimensionMemberSelectionDTO**](QueryDimensionMemberSelectionDTO.md) | An axis that uses existing dimension members in Visier. | [optional] 
**formula** | **str** | An axis expressed as a formula. | [optional] 
**member_map_selection** | [**QueryMemberMapSelectionDTO**](QueryMemberMapSelectionDTO.md) | An axis that uses an existing member map in Visier. | [optional] 
**numeric_ranges** | [**QueryNumericRangesDTO**](QueryNumericRangesDTO.md) | An axis that uses an existing range dimension in Visier and defines the ranges to query. | [optional] 
**selection_concept** | [**SelectionConceptReferenceDTO**](SelectionConceptReferenceDTO.md) | An axis that uses an existing selection concept in Visier.  The resulting axis consists of 3 positions: True, False, and Unknown. | [optional] 
**table_axis_options** | [**QueryAxisOptionsDTO**](QueryAxisOptionsDTO.md) | Additional transformations to perform on this axis. Only available when the Accept header is a table format, such as text/csv or application/jsonlines. | [optional] 

## Example

```python
from visier.model_query_apis.models.query_axis_dto import QueryAxisDTO

# TODO update the JSON string below
json = "{}"
# create an instance of QueryAxisDTO from a JSON string
query_axis_dto_instance = QueryAxisDTO.from_json(json)
# print the JSON string representation of the object
print(QueryAxisDTO.to_json())

# convert the object into a dict
query_axis_dto_dict = query_axis_dto_instance.to_dict()
# create an instance of QueryAxisDTO from a dict
query_axis_dto_from_dict = QueryAxisDTO.from_dict(query_axis_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


