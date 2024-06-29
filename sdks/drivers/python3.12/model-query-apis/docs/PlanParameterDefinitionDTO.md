# PlanParameterDefinitionDTO

The definition of a plan parameter. These parameters resolve planning model metrics to a specific plan and scenario  or snapshot values at query runtime.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the parameter. | [optional] 
**display_name** | **str** | The localized display name of the parameter. | [optional] 
**description** | **str** | The localized description of the parameter. | [optional] 
**model_name** | **str** | The name of the planning model to which the parameter applies. | [optional] 

## Example

```python
from visier.model_query.models.plan_parameter_definition_dto import PlanParameterDefinitionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PlanParameterDefinitionDTO from a JSON string
plan_parameter_definition_dto_instance = PlanParameterDefinitionDTO.from_json(json)
# print the JSON string representation of the object
print(PlanParameterDefinitionDTO.to_json())

# convert the object into a dict
plan_parameter_definition_dto_dict = plan_parameter_definition_dto_instance.to_dict()
# create an instance of PlanParameterDefinitionDTO from a dict
plan_parameter_definition_dto_from_dict = PlanParameterDefinitionDTO.from_dict(plan_parameter_definition_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


