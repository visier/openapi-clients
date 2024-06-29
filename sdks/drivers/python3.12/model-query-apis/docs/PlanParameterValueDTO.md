# PlanParameterValueDTO

The value for a parameter on a planning metric, including the parameter ID and the plan the parameter is based on.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameter_id** | **str** | The unique ID of the plan parameter qualified by the object. | [optional] 
**plan_id** | **str** | The unique ID of the plan the parameter is based on. | [optional] 
**scenario_id** | **str** | The unique ID of the scenario the parameter is based on. | [optional] 
**snapshot_id** | **str** | The unique ID of the snapshot the parameter is based on. | [optional] 

## Example

```python
from visier.model_query.models.plan_parameter_value_dto import PlanParameterValueDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PlanParameterValueDTO from a JSON string
plan_parameter_value_dto_instance = PlanParameterValueDTO.from_json(json)
# print the JSON string representation of the object
print(PlanParameterValueDTO.to_json())

# convert the object into a dict
plan_parameter_value_dto_dict = plan_parameter_value_dto_instance.to_dict()
# create an instance of PlanParameterValueDTO from a dict
plan_parameter_value_dto_from_dict = PlanParameterValueDTO.from_dict(plan_parameter_value_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


