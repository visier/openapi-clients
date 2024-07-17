# SelectionConceptsDTO

A collection of selection concepts

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selection_concepts** | [**List[SelectionConceptDTO]**](SelectionConceptDTO.md) |  | [optional] 

## Example

```python
from visier.api.model_query.models.selection_concepts_dto import SelectionConceptsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SelectionConceptsDTO from a JSON string
selection_concepts_dto_instance = SelectionConceptsDTO.from_json(json)
# print the JSON string representation of the object
print(SelectionConceptsDTO.to_json())

# convert the object into a dict
selection_concepts_dto_dict = selection_concepts_dto_instance.to_dict()
# create an instance of SelectionConceptsDTO from a dict
selection_concepts_dto_from_dict = SelectionConceptsDTO.from_dict(selection_concepts_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


