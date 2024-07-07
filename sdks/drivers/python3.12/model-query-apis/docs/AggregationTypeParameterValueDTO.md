# AggregationTypeParameterValueDTO

The value for an aggregation parameter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameter_id** | **str** | The unique ID of the aggregation parameter. | [optional] 
**aggregation_option_id** | **str** | The unique ID of the aggregation option. | [optional] 

## Example

```python
from visier.model_query.models.aggregation_type_parameter_value_dto import AggregationTypeParameterValueDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AggregationTypeParameterValueDTO from a JSON string
aggregation_type_parameter_value_dto_instance = AggregationTypeParameterValueDTO.from_json(json)
# print the JSON string representation of the object
print(AggregationTypeParameterValueDTO.to_json())

# convert the object into a dict
aggregation_type_parameter_value_dto_dict = aggregation_type_parameter_value_dto_instance.to_dict()
# create an instance of AggregationTypeParameterValueDTO from a dict
aggregation_type_parameter_value_dto_from_dict = AggregationTypeParameterValueDTO.from_dict(aggregation_type_parameter_value_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


