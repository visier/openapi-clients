# SnapshotQueryExecutionOptionsDTO

A SnapshotQueryExecutionOptions provides additional instructions to perform a snapshot query.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calendar_type** | **str** | The calendar type to use. This will be used for all time calculations unless explicitly overridden in  the calculation itself. Default is TENANT_CALENDAR. | [optional] 
**currency_conversion_code** | **str** | The optional target currency for all currency conversions.  If not specified, the tenant default currency will be used. | [optional] 
**currency_conversion_date** | **str** | The currency conversion date to use. If defined, the currency conversion will use the exchange rates as of this date. | [optional] 
**date_time_display_mode** | **str** | Control how date-time values are displayed in the result set.  Supported values:  * &#x60;EPOCH&#x60;: The number of elapsed milliseconds since January 1, 1970 in UTC timezone. This is the default.  * &#x60;DATETIME&#x60;: The date-time value displayed in &#x60;yyyy-MM-dd HH:mm:ssZZ&#x60; format. | [optional] 
**limit** | **int** | The maximum number of entries to return. Default is to return all entries. If &#x60;page&#x60; is defined but  limit is not defined, limit will be set to a default value of 1000. | [optional] 
**multiple_tables** | **bool** | Option to return multiple table files as zipped archive for derived metrics.  Default is false. If false, one table is returned for the drill-through metric. | [optional] 
**omit_header** | **bool** | Option to omit the header from the result.  If true, queryMode must be either FILL or FAIL.  Default is false. | [optional] 
**page** | **int** | A page defines a subset of the overall result set. The number of rows per page is equal to limit  with the exception of the last page in the result set which may contain fewer rows. &#x60;Page&#x60; is an index  that begins at 0. The index to start retrieving results is calculated by multiplying &#x60;page&#x60; by &#x60;limit&#x60;. | [optional] 
**query_mode** | **str** | Determines how the query should handle column definitions that the query is unable to resolve. Default is DEFAULT. | [optional] 

## Example

```python
from visier.api.model_query.models.snapshot_query_execution_options_dto import SnapshotQueryExecutionOptionsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotQueryExecutionOptionsDTO from a JSON string
snapshot_query_execution_options_dto_instance = SnapshotQueryExecutionOptionsDTO.from_json(json)
# print the JSON string representation of the object
print(SnapshotQueryExecutionOptionsDTO.to_json())

# convert the object into a dict
snapshot_query_execution_options_dto_dict = snapshot_query_execution_options_dto_instance.to_dict()
# create an instance of SnapshotQueryExecutionOptionsDTO from a dict
snapshot_query_execution_options_dto_from_dict = SnapshotQueryExecutionOptionsDTO.from_dict(snapshot_query_execution_options_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


