# QueryDimensionDataMemberSelectionDTO

A QueryDimensionLeafSelection allows you to define a member set consisting exclusively  of leaf-level, including data, members for the given dimension. Leaf members are those members that have  no descendents. A member may be a leaf member regardless of the level it is positioned at.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimension** | [**DimensionReferenceDTO**](DimensionReferenceDTO.md) | A dimension and its qualifying path to query. | [optional] 

## Example

```python
from visier.model_query.models.query_dimension_data_member_selection_dto import QueryDimensionDataMemberSelectionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of QueryDimensionDataMemberSelectionDTO from a JSON string
query_dimension_data_member_selection_dto_instance = QueryDimensionDataMemberSelectionDTO.from_json(json)
# print the JSON string representation of the object
print(QueryDimensionDataMemberSelectionDTO.to_json())

# convert the object into a dict
query_dimension_data_member_selection_dto_dict = query_dimension_data_member_selection_dto_instance.to_dict()
# create an instance of QueryDimensionDataMemberSelectionDTO from a dict
query_dimension_data_member_selection_dto_from_dict = QueryDimensionDataMemberSelectionDTO.from_dict(query_dimension_data_member_selection_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


