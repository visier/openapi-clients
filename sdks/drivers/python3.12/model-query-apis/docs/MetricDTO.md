# MetricDTO

A metric is a calculation based on one or more attribute values of analytic objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the metric. Note: See &#x60;Metrics&#x60; to get the ID. | [optional] 
**display_name** | **str** | The localized display name of the metric. | [optional] 
**description** | **str** | The localized description of the metric. | [optional] 
**data_start_date** | **str** | The date from which data becomes available for this metric.  Note: Format is the number of milliseconds since midnight 01 January, 1970 UTC as a string.  Epochs are expressed as 64-bit integers and represented as stringified longs in JSON due to JSON&#39;s inherent  limitation in representing large numbers. | [optional] 
**data_end_date** | **str** | The date from which data is no longer available for this metric.  Note: Format is the number of milliseconds since midnight 01 January, 1970 UTC as a string.  Epochs are expressed as 64-bit integers and represented as stringified longs in JSON due to JSON&#39;s inherent  limitation in representing large numbers. | [optional] 
**analytic_object_id** | **str** | The unique ID of the analytic object. | [optional] 
**parameters** | [**List[ParameterDefinitionDTO]**](ParameterDefinitionDTO.md) | The collection of parameters defined for the metric. | [optional] 
**category** | **int** | The category of the metric. Will be one of: &#x60;REGULAR&#x60;, &#x60;DERIVED&#x60; or &#x60;PLANNING&#x60;. | [optional] 
**visible_in_app** | **bool** | // &#x60;true&#x60; if this metric is set to be visible in your solution. | [optional] 

## Example

```python
from visier.model_query.models.metric_dto import MetricDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MetricDTO from a JSON string
metric_dto_instance = MetricDTO.from_json(json)
# print the JSON string representation of the object
print(MetricDTO.to_json())

# convert the object into a dict
metric_dto_dict = metric_dto_instance.to_dict()
# create an instance of MetricDTO from a dict
metric_dto_from_dict = MetricDTO.from_dict(metric_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


