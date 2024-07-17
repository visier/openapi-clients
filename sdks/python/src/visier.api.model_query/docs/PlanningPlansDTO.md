# PlanningPlansDTO

A collection of plan definitions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plans** | [**List[PlanningPlanDTO]**](PlanningPlanDTO.md) |  | [optional] 

## Example

```python
from visier.api.model_query.models.planning_plans_dto import PlanningPlansDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PlanningPlansDTO from a JSON string
planning_plans_dto_instance = PlanningPlansDTO.from_json(json)
# print the JSON string representation of the object
print(PlanningPlansDTO.to_json())

# convert the object into a dict
planning_plans_dto_dict = planning_plans_dto_instance.to_dict()
# create an instance of PlanningPlansDTO from a dict
planning_plans_dto_from_dict = PlanningPlansDTO.from_dict(planning_plans_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


