# SelectionConceptReferenceDTO

The name and qualifying path of a selection concept to query.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The ID of the selection concept. See &#x60;SelectionConcepts&#x60; to get the ID. | [optional] 
**qualifying_path** | **str** | The qualifying path to the selection concept in Visier, such as the analytic object or event the selection  concept is associated with. If the path has multiple objects, each object is separated by a period. | [optional] 

## Example

```python
from visier.model_query_apis.models.selection_concept_reference_dto import SelectionConceptReferenceDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SelectionConceptReferenceDTO from a JSON string
selection_concept_reference_dto_instance = SelectionConceptReferenceDTO.from_json(json)
# print the JSON string representation of the object
print(SelectionConceptReferenceDTO.to_json())

# convert the object into a dict
selection_concept_reference_dto_dict = selection_concept_reference_dto_instance.to_dict()
# create an instance of SelectionConceptReferenceDTO from a dict
selection_concept_reference_dto_from_dict = SelectionConceptReferenceDTO.from_dict(selection_concept_reference_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


