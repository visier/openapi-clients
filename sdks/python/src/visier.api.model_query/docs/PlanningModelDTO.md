# PlanningModelDTO

The basic information about the planning model. A planning model captures the planning intent, plan items, and the relationship between them.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The localized description of the planning model. | [optional] 
**display_name** | **str** | The localized display name of the planning model. | [optional] 
**id** | **str** | The unique identifier of the planning model.  Note: See &#x60;PlanningModels&#x60; to get the ID. | [optional] 

## Example

```python
from visier.api.model_query.models.planning_model_dto import PlanningModelDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PlanningModelDTO from a JSON string
planning_model_dto_instance = PlanningModelDTO.from_json(json)
# print the JSON string representation of the object
print(PlanningModelDTO.to_json())

# convert the object into a dict
planning_model_dto_dict = planning_model_dto_instance.to_dict()
# create an instance of PlanningModelDTO from a dict
planning_model_dto_from_dict = PlanningModelDTO.from_dict(planning_model_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


