# QueryFilterDTO

A QueryFilter selects specific data points within a population.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cohort** | [**CohortFilterDTO**](CohortFilterDTO.md) | A filter that identifies a population at a specific time. | [optional] 
**formula** | **str** | A filter expressed as a formula. | [optional] 
**member_set** | [**MemberFilterDTO**](MemberFilterDTO.md) | A filter that includes or excludes dimension members. | [optional] 
**selection_concept** | [**SelectionConceptReferenceDTO**](SelectionConceptReferenceDTO.md) | A filter that uses an existing selection concept in Visier. | [optional] 

## Example

```python
from visier.api.model_query.models.query_filter_dto import QueryFilterDTO

# TODO update the JSON string below
json = "{}"
# create an instance of QueryFilterDTO from a JSON string
query_filter_dto_instance = QueryFilterDTO.from_json(json)
# print the JSON string representation of the object
print(QueryFilterDTO.to_json())

# convert the object into a dict
query_filter_dto_dict = query_filter_dto_instance.to_dict()
# create an instance of QueryFilterDTO from a dict
query_filter_dto_from_dict = QueryFilterDTO.from_dict(query_filter_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


