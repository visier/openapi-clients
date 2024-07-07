# PlanningConceptFilterContextDTO

A plan context defined using a selection concept.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The object name of the selection concept. | [optional] 

## Example

```python
from visier.model_query.models.planning_concept_filter_context_dto import PlanningConceptFilterContextDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PlanningConceptFilterContextDTO from a JSON string
planning_concept_filter_context_dto_instance = PlanningConceptFilterContextDTO.from_json(json)
# print the JSON string representation of the object
print(PlanningConceptFilterContextDTO.to_json())

# convert the object into a dict
planning_concept_filter_context_dto_dict = planning_concept_filter_context_dto_instance.to_dict()
# create an instance of PlanningConceptFilterContextDTO from a dict
planning_concept_filter_context_dto_from_dict = PlanningConceptFilterContextDTO.from_dict(planning_concept_filter_context_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


