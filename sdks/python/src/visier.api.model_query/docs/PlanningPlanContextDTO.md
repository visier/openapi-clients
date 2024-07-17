# PlanningPlanContextDTO

The filter context for a plan. Plan contexts are defined using a set of hierarchy members or a concept.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**concept_filter_context** | [**PlanningConceptFilterContextDTO**](PlanningConceptFilterContextDTO.md) | A plan context defined using a selection concept. | [optional] 
**hierarchy_filter_context** | [**PlanningHierarchyFilterContextDTO**](PlanningHierarchyFilterContextDTO.md) | A plan context defined using hierarchy members. | [optional] 

## Example

```python
from visier.api.model_query.models.planning_plan_context_dto import PlanningPlanContextDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PlanningPlanContextDTO from a JSON string
planning_plan_context_dto_instance = PlanningPlanContextDTO.from_json(json)
# print the JSON string representation of the object
print(PlanningPlanContextDTO.to_json())

# convert the object into a dict
planning_plan_context_dto_dict = planning_plan_context_dto_instance.to_dict()
# create an instance of PlanningPlanContextDTO from a dict
planning_plan_context_dto_from_dict = PlanningPlanContextDTO.from_dict(planning_plan_context_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


