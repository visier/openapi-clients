# PlanningModelsDTO

A collection of planning modules.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**models** | [**List[PlanningModelDTO]**](PlanningModelDTO.md) |  | [optional] 

## Example

```python
from visier.model_query_apis.models.planning_models_dto import PlanningModelsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PlanningModelsDTO from a JSON string
planning_models_dto_instance = PlanningModelsDTO.from_json(json)
# print the JSON string representation of the object
print(PlanningModelsDTO.to_json())

# convert the object into a dict
planning_models_dto_dict = planning_models_dto_instance.to_dict()
# create an instance of PlanningModelsDTO from a dict
planning_models_dto_from_dict = PlanningModelsDTO.from_dict(planning_models_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


