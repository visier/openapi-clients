# ParameterDefinitionDTO

Parameters generalize object definitions so that end users can provide values at query run time.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation_type_parameter** | [**AggregationTypeParameterDTO**](AggregationTypeParameterDTO.md) | An aggregation parameter. Such parameters enable control over how applicable metrics aggregate their results. | [optional] 
**member_parameter** | [**MemberParameterDefinitionDTO**](MemberParameterDefinitionDTO.md) | A filter parameter that can be set with dimension members for the end user to select. | [optional] 
**numeric_parameter** | [**NumericParameterDefinitionDTO**](NumericParameterDefinitionDTO.md) | A parameter with a numeric data type. A numeric parameter can be set with an optional default value and value range. | [optional] 
**plan_parameter** | [**PlanParameterDefinitionDTO**](PlanParameterDefinitionDTO.md) | A parameter on a planning metric. Plan parameters resolve planning model metrics to a specific plan and scenario or snapshot. | [optional] 

## Example

```python
from visier.model_query_apis.models.parameter_definition_dto import ParameterDefinitionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ParameterDefinitionDTO from a JSON string
parameter_definition_dto_instance = ParameterDefinitionDTO.from_json(json)
# print the JSON string representation of the object
print(ParameterDefinitionDTO.to_json())

# convert the object into a dict
parameter_definition_dto_dict = parameter_definition_dto_instance.to_dict()
# create an instance of ParameterDefinitionDTO from a dict
parameter_definition_dto_from_dict = ParameterDefinitionDTO.from_dict(parameter_definition_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


