# MetricsDTO

A collection of metrics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metrics** | [**List[MetricDTO]**](MetricDTO.md) |  | [optional] 

## Example

```python
from visier.api.model_query.models.metrics_dto import MetricsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsDTO from a JSON string
metrics_dto_instance = MetricsDTO.from_json(json)
# print the JSON string representation of the object
print(MetricsDTO.to_json())

# convert the object into a dict
metrics_dto_dict = metrics_dto_instance.to_dict()
# create an instance of MetricsDTO from a dict
metrics_dto_from_dict = MetricsDTO.from_dict(metrics_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


