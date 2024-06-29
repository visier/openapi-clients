# QueryTimeIntervalDTO

A QueryTimeInterval defines the time interval to query, including the \"from\" time, period type,  period count, time direction, and shift to apply

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_instant** | **str** | The instant from which to extend, in milliseconds since 1970-01-01T00:00:00Z.  Events that occur on this date are excluded. Subject-based data that ends on this date is included.  Note: Epochs are expressed as 64-bit integers and represented as stringified longs in JSON due to  JSON&#39;s inherent limitation in representing large numbers. | [optional] 
**from_date_time** | **str** | The instant from which to extend, as an ISO-8601 formatted date time string.  Valid formats: yyyy-MM-dd, yyyy-MM-dd&#39;T&#39;HH:mm:ss, yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS.  Events that occur on this date are excluded. Subject-based data that ends on this date is included. | [optional] 
**interval_period_type** | **int** | The time period type for each interval. Default is MONTH. | [optional] 
**interval_period_count** | **int** | The number of time periods per interval. | [optional] 
**direction** | **int** | The direction to extend. Default is BACKWARD. | [optional] 
**shift** | [**TimeShiftDTO**](TimeShiftDTO.md) | The amount of time to shift the time interval by, such as backward by one year. Default is none. | [optional] 

## Example

```python
from visier.model_query.models.query_time_interval_dto import QueryTimeIntervalDTO

# TODO update the JSON string below
json = "{}"
# create an instance of QueryTimeIntervalDTO from a JSON string
query_time_interval_dto_instance = QueryTimeIntervalDTO.from_json(json)
# print the JSON string representation of the object
print(QueryTimeIntervalDTO.to_json())

# convert the object into a dict
query_time_interval_dto_dict = query_time_interval_dto_instance.to_dict()
# create an instance of QueryTimeIntervalDTO from a dict
query_time_interval_dto_from_dict = QueryTimeIntervalDTO.from_dict(query_time_interval_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


