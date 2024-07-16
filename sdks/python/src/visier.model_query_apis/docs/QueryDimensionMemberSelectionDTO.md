# QueryDimensionMemberSelectionDTO

A QueryDimensionMemberSelection defines dimension members to select in the query.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimension** | [**DimensionReferenceDTO**](DimensionReferenceDTO.md) | A dimension and its qualifying path to query. | [optional] 
**members** | [**List[DimensionMemberReferenceDTO]**](DimensionMemberReferenceDTO.md) | A collection of dimension members to select in the query. This must contain at least one member. | [optional] 

## Example

```python
from visier.model_query_apis.models.query_dimension_member_selection_dto import QueryDimensionMemberSelectionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of QueryDimensionMemberSelectionDTO from a JSON string
query_dimension_member_selection_dto_instance = QueryDimensionMemberSelectionDTO.from_json(json)
# print the JSON string representation of the object
print(QueryDimensionMemberSelectionDTO.to_json())

# convert the object into a dict
query_dimension_member_selection_dto_dict = query_dimension_member_selection_dto_instance.to_dict()
# create an instance of QueryDimensionMemberSelectionDTO from a dict
query_dimension_member_selection_dto_from_dict = QueryDimensionMemberSelectionDTO.from_dict(query_dimension_member_selection_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


