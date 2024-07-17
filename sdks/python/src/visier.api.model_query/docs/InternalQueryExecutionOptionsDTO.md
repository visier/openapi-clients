# InternalQueryExecutionOptionsDTO

Internal options - not to be documented or used by external parties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**align_time_axis_to_period_end** | **bool** | If true, shifts the time axis members back by one millisecond.  Shifting the time axis members back by one millisecond makes them valid at the end of the period instead of at the start of the next period.  This aligns the returned data timestamps with the timestamps in the Visier application.   Example: If the timestamps are originally [&#x60;2019-06-01T00:00:00.000Z&#x60;, &#x60;2019-05-01T00:00:00.000Z&#x60;],  then &#x60;alignTimeAxisPeriodEnd&#x60; turns the timestamps into [&#x60;2019-05-31T23:59:59.999Z&#x60;, &#x60;2019-04-30T23:59:59.999Z&#x60;].   Example: If the timestamps are originally [&#x60;2019-05-01T00:00:00.000Z/2019-06-01T00:00:00.000Z&#x60;, &#x60;2019-04-01T00:00:00.000Z/2019-05-01T00:00:00.000Z&#x60;],  then &#x60;alignTimeAxisPeriodEnd&#x60; turns the timestamps into [&#x60;2019-05-01T00:00:00.000Z/2019-05-31T23:59:59.999Z&#x60;, &#x60;2019-04-01T00:00:00.000Z/2019-04-30T23:59:59.999Z&#x60;]. | [optional] 
**sparse_handling_mode** | **str** |  | [optional] 

## Example

```python
from visier.api.model_query.models.internal_query_execution_options_dto import InternalQueryExecutionOptionsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of InternalQueryExecutionOptionsDTO from a JSON string
internal_query_execution_options_dto_instance = InternalQueryExecutionOptionsDTO.from_json(json)
# print the JSON string representation of the object
print(InternalQueryExecutionOptionsDTO.to_json())

# convert the object into a dict
internal_query_execution_options_dto_dict = internal_query_execution_options_dto_instance.to_dict()
# create an instance of InternalQueryExecutionOptionsDTO from a dict
internal_query_execution_options_dto_from_dict = InternalQueryExecutionOptionsDTO.from_dict(internal_query_execution_options_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


