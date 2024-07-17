# AggregationTypeParameterDTO

The definition of an aggregation parameter. These parameters resolve metrics that use aggregation parameters.  For example, Visier Benchmarks metrics often use aggregation parameters to enable callers to aggregate metric values according to their average or different percentiles.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The localized description of the parameter. | [optional] 
**display_name** | **str** | The localized display name of the parameter. | [optional] 
**id** | **str** | The unique ID of the parameter. | [optional] 
**parameter_options** | [**List[AggregationTypeOptionDTO]**](AggregationTypeOptionDTO.md) | The options defined for the parameter. | [optional] 

## Example

```python
from visier.api.model_query.models.aggregation_type_parameter_dto import AggregationTypeParameterDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AggregationTypeParameterDTO from a JSON string
aggregation_type_parameter_dto_instance = AggregationTypeParameterDTO.from_json(json)
# print the JSON string representation of the object
print(AggregationTypeParameterDTO.to_json())

# convert the object into a dict
aggregation_type_parameter_dto_dict = aggregation_type_parameter_dto_instance.to_dict()
# create an instance of AggregationTypeParameterDTO from a dict
aggregation_type_parameter_dto_from_dict = AggregationTypeParameterDTO.from_dict(aggregation_type_parameter_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


