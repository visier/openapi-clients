# QueryDimensionLevelSelectionDTO

A QueryDimensionLevelSelection allows you to select a dimension level and its members without  explicitly listing each member. To see the correct notation for levels, see `Dimension`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimension** | [**DimensionReferenceDTO**](DimensionReferenceDTO.md) | A dimension and its qualifying path to query. | [optional] 
**level_ids** | **List[str]** | The ordered collection of level identifiers for the dimension. See &#x60;Dimension&#x60;. | [optional] 

## Example

```python
from visier.api.model_query.models.query_dimension_level_selection_dto import QueryDimensionLevelSelectionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of QueryDimensionLevelSelectionDTO from a JSON string
query_dimension_level_selection_dto_instance = QueryDimensionLevelSelectionDTO.from_json(json)
# print the JSON string representation of the object
print(QueryDimensionLevelSelectionDTO.to_json())

# convert the object into a dict
query_dimension_level_selection_dto_dict = query_dimension_level_selection_dto_instance.to_dict()
# create an instance of QueryDimensionLevelSelectionDTO from a dict
query_dimension_level_selection_dto_from_dict = QueryDimensionLevelSelectionDTO.from_dict(query_dimension_level_selection_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


