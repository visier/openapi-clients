# PlanningPlanDTO

The definition of a plan. Plans are defined on planning models, and each plan may define multiple scenarios or snapshots.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the plan.  Note: See &#x60;PlanningPlans&#x60; to get the ID. | [optional] 
**name** | **str** | The name of the plan. | [optional] 
**subject_id** | **str** | The ID of subject for the plan. | [optional] 
**default_contexts** | [**List[PlanningPlanContextDTO]**](PlanningPlanContextDTO.md) | The contexts defined for the plan. | [optional] 
**plan_dimension_ids** | **List[str]** | The IDs of the dimensions defined for the plan. | [optional] 
**scenarios** | [**List[ScenarioOrSnapshotDTO]**](ScenarioOrSnapshotDTO.md) | The available scenarios for the plan. | [optional] 
**snapshots** | [**List[ScenarioOrSnapshotDTO]**](ScenarioOrSnapshotDTO.md) | The available snapshots for the plan. | [optional] 

## Example

```python
from visier.model_query.models.planning_plan_dto import PlanningPlanDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PlanningPlanDTO from a JSON string
planning_plan_dto_instance = PlanningPlanDTO.from_json(json)
# print the JSON string representation of the object
print(PlanningPlanDTO.to_json())

# convert the object into a dict
planning_plan_dto_dict = planning_plan_dto_instance.to_dict()
# create an instance of PlanningPlanDTO from a dict
planning_plan_dto_from_dict = PlanningPlanDTO.from_dict(planning_plan_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


