# QueryTimeIntervalsDTO

A QueryTimeIntervals defines a series of time intervals to query, including the \"from\" time, period type, period count,  number of intervals, time direction, and shift to apply to each time interval.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | **str** | The direction to extend. Defaults is BACKWARD. | [optional] 
**dynamic_date_from** | **str** | Dynamically select the date from which to extend. Valid values are &#x60;SOURCE&#x60; or &#x60;COMPLETE_PERIOD&#x60;. Both options use the &#x60;source&#x60; query definition element to determine the date.   If &#x60;dynamicDateFrom&#x60; is &#x60;SOURCE&#x60;, the query returns data from a date determined by the &#x60;source&#x60; query definition element. If &#x60;dynamicDateFrom&#x60; is &#x60;COMPLETE_PERIOD&#x60;, the query returns data starting from the latest or earliest date with a complete period of data. When &#x60;dynamicDateFrom&#x60; is specified:  * If &#x60;source&#x60; is &#x60;metric&#x60;, then &#x60;dynamicDateFrom&#x60; considers the date range of available data for the metric.  * If &#x60;source&#x60; is &#x60;formula&#x60;, then &#x60;dynamicDateFrom&#x60; considers the date range of available data for the metric in the formula.  * If &#x60;source&#x60; is &#x60;metrics&#x60;, then &#x60;dynamicDateFrom&#x60; considers the date range of available data for the metric in the formula.  Then, if &#x60;direction&#x60; is &#x60;BACKWARD&#x60;, query backward from the data **end** date and if &#x60;direction&#x60; is &#x60;FORWARD&#x60;, query forward from the data **start** date.   This allows you to keep getting the latest or earliest data without changing your query every time there&#39;s new or updated data.   Note: For multi-metric queries, if &#x60;direction&#x60; is &#x60;BACKWARD&#x60;, query backward from the earliest data end date of all metrics and if &#x60;direction&#x60; is &#x60;FORWARD&#x60;, query forward from the latest data start date of all metrics.   This ensures that all metrics have data in the specified time range.   Example: If a tenant has Headcount metric data available from 2023-01-01 to 2024-01-01 (End date exclusive), specifying &#x60;dynamicDateFrom&#x60;: &#x60;SOURCE&#x60; with &#x60;direction&#x60;: &#x60;BACKWARD&#x60;   means the query will retrieve data backward from 2024-01-01. The effect is the same as if specifying a &#x60;fromDateTime&#x60; of 2024-01-01&#39;T&#39;00:00:00.000.    Example: If a tenant has Employee subject data available from 2023-01-10 to 2023-04-01 (End date exclusive), specifying &#x60;dynamicDateFrom&#x60;: &#x60;COMPLETE_PERIOD&#x60; with &#x60;direction&#x60;: &#x60;FORWARD&#x60;   means the query will retrieve data forward from 2023-02-01. The effect is the same as if specifying a &#x60;fromDateTime&#x60; of 2023-02-01&#39;T&#39;00:00:00.000.    Example: If a tenant has Employee subject data available from 2023-01-01 to 2023-03-15 (End date exclusive), specifying &#x60;dynamicDateFrom&#x60;: &#x60;COMPLETE_PERIOD&#x60; with &#x60;direction&#x60;: &#x60;BACKWARD&#x60;   means the query will retrieve data backward from 2023-03-01. The effect is the same as if specifying a &#x60;fromDateTime&#x60; of 2023-03-01&#39;T&#39;00:00:00.000.    Example: If a tenant has Headcount data available from 2023-01-01 to 2024-09-01 and Exit Count data available from 2023-01-01 to 2024-01-01, specifying &#x60;dynamicDateFrom&#x60;: &#x60;SOURCE&#x60; with &#x60;direction&#x60;: &#x60;BACKWARD&#x60; means the query will retrieve data backward from 2024-01-01.   Exit Count has an earlier data end date than Headcount, so &#x60;dynamicDateFrom&#x60; retrieves data backward from Exit Count&#39;s data end date to ensure both metrics have data in the specified time range.   Example: Retrieve Headcount (employeeCount) extending 1 month backward from Headcount&#39;s dynamic source date       {           \&quot;query\&quot;: {               \&quot;source\&quot;: {                   \&quot;metric\&quot;: \&quot;employeeCount\&quot;               },               \&quot;timeIntervals\&quot;: {                   \&quot;dynamicDateFrom\&quot;: \&quot;SOURCE\&quot;,                   \&quot;intervalPeriodType\&quot;: \&quot;MONTH\&quot;,                   \&quot;intervalCount\&quot;: 1,                   \&quot;direction\&quot;: \&quot;BACKWARD\&quot;               }           }       } | [optional] 
**from_date_time** | **str** | The instant from which to extend, as an ISO-8601 formatted date time string. This value is exclusive.  Valid formats: yyyy-MM-dd, yyyy-MM-dd&#39;T&#39;HH:mm:ss, yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS.  Events that occur on this date are excluded. Subject-based data that ends on this date is included. | [optional] 
**from_instant** | **str** | The instant from which to extend, in milliseconds since 1970-01-01T00:00:00Z.  Events that occur on this date are excluded. Subject-based data that ends on this date is included.  Note: Epochs are expressed as 64-bit integers and represented as stringified longs in JSON due to JSON&#39;s  inherent limitation in representing large numbers. | [optional] 
**interval_count** | **int** | The number of intervals. Default is 1. | [optional] 
**interval_period_count** | **int** | The number of time periods per interval. Default is 1. | [optional] 
**interval_period_type** | **str** | The time period type for each interval. Default is MONTH. | [optional] 
**shift** | [**TimeShiftDTO**](TimeShiftDTO.md) | The amount of time to shift the time interval by, such as backward by one year. | [optional] 
**trailing_period_count** | **int** | The number of time periods per trailing period. If &#x60;trailingPeriodType&#x60; is defined and &#x60;trailingPeriodCount&#x60; is undefined, the default trailing period count is 1.  Note: This parameter is only applicable to metrics that can calculate trailing time. If defined on a metric that doesn&#39;t have trailing time, the platform ignores the parameter. | [optional] 
**trailing_period_type** | **str** | The time period type for each trailing period. If &#x60;trailingPeriodCount&#x60; is defined and &#x60;trailingPeriodType&#x60; is undefined, the default trailing period type is &#x60;MONTH&#x60;.  If both &#x60;trailingPeriodType&#x60; and &#x60;trailingPeriodCount&#x60; are undefined, &#x60;intervalPeriodCount&#x60; is used as the trailing period count.  Note: This parameter is only applicable to metrics that can calculate trailing time. If defined on a metric that doesn&#39;t have trailing time, the platform ignores the parameter. | [optional] 

## Example

```python
from visier.model_query_apis.models.query_time_intervals_dto import QueryTimeIntervalsDTO

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


