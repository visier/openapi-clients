# SelectionConceptDTO

Selection concepts select a population of subject members of a given subject or event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the selection concept  Note: See &#x60;SelectionConcepts&#x60; to get the ID. | [optional] 
**display_name** | **str** | The localized display name of the selection concept. | [optional] 
**description** | **str** | The localized description of the selection concept. | [optional] 
**visible_in_app** | **bool** | &#x60;true&#x60; if this selection concept is set to be visible in your solution. | [optional] 
**tags** | [**List[TagMapElementDTO]**](TagMapElementDTO.md) | The optional collection of tags defined for this element. | [optional] 

## Example

```python
from visier.model_query.models.selection_concept_dto import SelectionConceptDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SelectionConceptDTO from a JSON string
selection_concept_dto_instance = SelectionConceptDTO.from_json(json)
# print the JSON string representation of the object
print(SelectionConceptDTO.to_json())

# convert the object into a dict
selection_concept_dto_dict = selection_concept_dto_instance.to_dict()
# create an instance of SelectionConceptDTO from a dict
selection_concept_dto_from_dict = SelectionConceptDTO.from_dict(selection_concept_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


