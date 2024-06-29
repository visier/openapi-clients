# QueryPropertyDTO

A QueryProperty defines a property of a data point returned from a query.  This is not the same as a `property` in Visier's data mode.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**formula** | **str** | A formula-based property. | [optional] 
**var_property** | [**PropertyReferenceDTO**](PropertyReferenceDTO.md) | A property reference. | [optional] 
**selection_concept** | [**SelectionConceptReferenceDTO**](SelectionConceptReferenceDTO.md) | A selection concept-based property that returns true or false. | [optional] 
**dimension** | [**DimensionReferenceDTO**](DimensionReferenceDTO.md) | A dimension-based property that returns the full name path of the dimension member that the data point is mapped to. | [optional] 
**member_map_property** | [**QueryMemberMapPropertyDTO**](QueryMemberMapPropertyDTO.md) | A member map-based property that uses an existing member map in Visier. | [optional] 
**effective_date_property** | **object** | A property that yields the effective date for the record | [optional] 

## Example

```python
from visier.model_query.models.query_property_dto import QueryPropertyDTO

# TODO update the JSON string below
json = "{}"
# create an instance of QueryPropertyDTO from a JSON string
query_property_dto_instance = QueryPropertyDTO.from_json(json)
# print the JSON string representation of the object
print(QueryPropertyDTO.to_json())

# convert the object into a dict
query_property_dto_dict = query_property_dto_instance.to_dict()
# create an instance of QueryPropertyDTO from a dict
query_property_dto_from_dict = QueryPropertyDTO.from_dict(query_property_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


