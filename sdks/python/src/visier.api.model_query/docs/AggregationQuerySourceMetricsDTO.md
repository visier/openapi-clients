# AggregationQuerySourceMetricsDTO

The IDs and column names of multiple metrics.   **Note:**  Only available when the `Accept` header is text/csv. For more information, see `Aggregate`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | [**List[AggregationQuerySourceMetricDTO]**](AggregationQuerySourceMetricDTO.md) | An array of metric columns. | [optional] 

## Example

```python
from visier.api.model_query.models.aggregation_query_source_metrics_dto import AggregationQuerySourceMetricsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AggregationQuerySourceMetricsDTO from a JSON string
aggregation_query_source_metrics_dto_instance = AggregationQuerySourceMetricsDTO.from_json(json)
# print the JSON string representation of the object
print(AggregationQuerySourceMetricsDTO.to_json())

# convert the object into a dict
aggregation_query_source_metrics_dto_dict = aggregation_query_source_metrics_dto_instance.to_dict()
# create an instance of AggregationQuerySourceMetricsDTO from a dict
aggregation_query_source_metrics_dto_from_dict = AggregationQuerySourceMetricsDTO.from_dict(aggregation_query_source_metrics_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


