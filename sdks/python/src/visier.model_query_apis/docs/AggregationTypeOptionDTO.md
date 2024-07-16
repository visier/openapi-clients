# AggregationTypeOptionDTO

The definition of an aggregation option.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation_function** | **str** | The aggregation function of the parameter option. | [optional] 
**display_name** | **str** | The localized display name of the parameter option. | [optional] 
**id** | **str** | The unique ID of the parameter option. | [optional] 
**is_default** | **bool** | &#x60;true&#x60; if the parameter option is the default one and &#x60;false&#x60; otherwise. | [optional] 
**property_name** | **str** | The property name of the parameter option. | [optional] 

## Example

```python
from visier.model_query_apis.models.aggregation_type_option_dto import AggregationTypeOptionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AggregationTypeOptionDTO from a JSON string
aggregation_type_option_dto_instance = AggregationTypeOptionDTO.from_json(json)
# print the JSON string representation of the object
print(AggregationTypeOptionDTO.to_json())

# convert the object into a dict
aggregation_type_option_dto_dict = aggregation_type_option_dto_instance.to_dict()
# create an instance of AggregationTypeOptionDTO from a dict
aggregation_type_option_dto_from_dict = AggregationTypeOptionDTO.from_dict(aggregation_type_option_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


