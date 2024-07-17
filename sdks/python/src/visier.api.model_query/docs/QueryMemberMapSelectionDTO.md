# QueryMemberMapSelectionDTO

A QueryMemberMapSelection groups data in a query by dimension members in a member map.  This allows grouping by a dimension that isn't typically valid on the analytic object being  queried by selecting a valid member map on the analytic object.  Note: This is unique to the data query API and cannot be reproduced in Visier's interface.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_map** | [**DimensionReferenceDTO**](DimensionReferenceDTO.md) | A member map and its qualifying path to query. | [optional] 
**members** | [**List[DimensionMemberReferenceDTO]**](DimensionMemberReferenceDTO.md) | A collection of the selected dimension members from the &#x60;targetDimension&#x60;. This must contain at least one member. | [optional] 
**target_dimension_name** | **str** | The name of the member map&#39;s dimension that you want to query. The member selection is based on this dimension. | [optional] 

## Example

```python
from visier.api.model_query.models.query_member_map_selection_dto import QueryMemberMapSelectionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of QueryMemberMapSelectionDTO from a JSON string
query_member_map_selection_dto_instance = QueryMemberMapSelectionDTO.from_json(json)
# print the JSON string representation of the object
print(QueryMemberMapSelectionDTO.to_json())

# convert the object into a dict
query_member_map_selection_dto_dict = query_member_map_selection_dto_instance.to_dict()
# create an instance of QueryMemberMapSelectionDTO from a dict
query_member_map_selection_dto_from_dict = QueryMemberMapSelectionDTO.from_dict(query_member_map_selection_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


