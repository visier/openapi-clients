# QueryMemberMapPropertyDTO

A QueryMemberMapProperty defines an existing member map and its dimension to query.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_map** | [**DimensionReferenceDTO**](DimensionReferenceDTO.md) | A member map and its qualifying path to query. | [optional] 
**target_dimension_name** | **str** | The name of the member map&#39;s dimension that you want to query. The member selection is based on this dimension. | [optional] 

## Example

```python
from visier.api.model_query.models.query_member_map_property_dto import QueryMemberMapPropertyDTO

# TODO update the JSON string below
json = "{}"
# create an instance of QueryMemberMapPropertyDTO from a JSON string
query_member_map_property_dto_instance = QueryMemberMapPropertyDTO.from_json(json)
# print the JSON string representation of the object
print(QueryMemberMapPropertyDTO.to_json())

# convert the object into a dict
query_member_map_property_dto_dict = query_member_map_property_dto_instance.to_dict()
# create an instance of QueryMemberMapPropertyDTO from a dict
query_member_map_property_dto_from_dict = QueryMemberMapPropertyDTO.from_dict(query_member_map_property_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


