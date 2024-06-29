# QueryTimeIntervalsDTO

A QueryTimeInterval defines a series of time intervals to query, including the \"from\" time, period type, period count,  number of intervals, time direction, and shift to apply to each time interval.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_instant** | **str** | The instant from which to extend, in milliseconds since 1970-01-01T00:00:00Z.  Events that occur on this date are excluded. Subject-based data that ends on this date is included.  Note: Epochs are expressed as 64-bit integers and represented as stringified longs in JSON due to JSON&#39;s  inherent limitation in representing large numbers. | [optional] 
**from_date_time** | **str** | The instant from which to extend, as an ISO-8601 formatted date time string. This value is exclusive.  Valid formats: yyyy-MM-dd, yyyy-MM-dd&#39;T&#39;HH:mm:ss, yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS. | [optional] 
**interval_period_type** | **int** | The time period type for each interval. Default is MONTH. | [optional] 
**interval_period_count** | **int** | The number of time periods per interval. Default is 1. | [optional] 
**interval_count** | **int** | The number of intervals. Default is 1. | [optional] 
**direction** | **int** | The direction to extend. Defaults is BACKWARD. | [optional] 
**shift** | [**TimeShiftDTO**](TimeShiftDTO.md) | The amount of time to shift the time interval by, such as backward by one year. | [optional] 
**trailing_period_type** | **int** | The time period type for each trailing period. If &#x60;trailingPeriodCount&#x60; is defined and &#x60;trailingPeriodType&#x60; is undefined, the default trailing period type is &#x60;MONTH&#x60;.  If both &#x60;trailingPeriodType&#x60; and &#x60;trailingPeriodCount&#x60; are undefined, &#x60;intervalPeriodCount&#x60; is used as the trailing period count.  Note: This parameter is only applicable to metrics that can calculate trailing time. If defined on a metric that doesn&#39;t have trailing time, the platform ignores the parameter. | [optional] 
**trailing_period_count** | **int** | The number of time periods per trailing period. If &#x60;trailingPeriodType&#x60; is defined and &#x60;trailingPeriodCount&#x60; is undefined, the default trailing period count is 1.  Note: This parameter is only applicable to metrics that can calculate trailing time. If defined on a metric that doesn&#39;t have trailing time, the platform ignores the parameter. | [optional] 

## Example

```python
from visier.model_query.models.query_time_intervals_dto import QueryTimeIntervalsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of QueryTimeIntervalsDTO from a JSON string
query_time_intervals_dto_instance = QueryTimeIntervalsDTO.from_json(json)
# print the JSON string representation of the object
print(QueryTimeIntervalsDTO.to_json())

# convert the object into a dict
query_time_intervals_dto_dict = query_time_intervals_dto_instance.to_dict()
# create an instance of QueryTimeIntervalsDTO from a dict
query_time_intervals_dto_from_dict = QueryTimeIntervalsDTO.from_dict(query_time_intervals_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


