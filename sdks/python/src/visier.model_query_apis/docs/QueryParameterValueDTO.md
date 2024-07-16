# QueryParameterValueDTO

An object that contains parameter values for either member or numeric parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation_type_value** | [**AggregationTypeParameterValueDTO**](AggregationTypeParameterValueDTO.md) | A value for an aggregation parameter. | [optional] 
**member_value** | [**MemberParameterValueDTO**](MemberParameterValueDTO.md) | A value for a member parameter. | [optional] 
**numeric_value** | [**NumericParameterValueDTO**](NumericParameterValueDTO.md) | A value for a numeric parameter. | [optional] 
**plan_value** | [**PlanParameterValueDTO**](PlanParameterValueDTO.md) | A value for a plan parameter. | [optional] 

## Example

```python
from visier.model_query_apis.models.query_parameter_value_dto import QueryParameterValueDTO

# TODO update the JSON string below
json = "{}"
# create an instance of QueryParameterValueDTO from a JSON string
query_parameter_value_dto_instance = QueryParameterValueDTO.from_json(json)
# print the JSON string representation of the object
print(QueryParameterValueDTO.to_json())

# convert the object into a dict
query_parameter_value_dto_dict = query_parameter_value_dto_instance.to_dict()
# create an instance of QueryParameterValueDTO from a dict
query_parameter_value_dto_from_dict = QueryParameterValueDTO.from_dict(query_parameter_value_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


