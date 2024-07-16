# SnapshotQueryExecutionDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | [**List[PropertyColumnDTO]**](PropertyColumnDTO.md) | The columns to include in the result. This must contain at least one column. | [optional] 
**filters** | [**List[QueryFilterDTO]**](QueryFilterDTO.md) | The filters of this query. Omit &#x60;filters&#x60; if no filtering is required. | [optional] 
**options** | [**SnapshotQueryExecutionOptionsDTO**](SnapshotQueryExecutionOptionsDTO.md) | Additional instructions for your query, such as a calendar type or conversion information. | [optional] 
**parameter_values** | [**List[QueryParameterValueDTO]**](QueryParameterValueDTO.md) | The parameter values for either member or numeric parameters. | [optional] 
**sort_options** | [**List[SortOptionDTO]**](SortOptionDTO.md) | The index and direction to sort a column in the &#x60;columns&#x60; array. | [optional] 
**source** | [**ListQuerySourceDTO**](ListQuerySourceDTO.md) | The source data that you want to query. | [optional] 
**time_intervals** | [**QueryTimeIntervalsDTO**](QueryTimeIntervalsDTO.md) | The time intervals to query. | [optional] 

## Example

```python
from visier.model_query_apis.models.snapshot_query_execution_dto import SnapshotQueryExecutionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotQueryExecutionDTO from a JSON string
snapshot_query_execution_dto_instance = SnapshotQueryExecutionDTO.from_json(json)
# print the JSON string representation of the object
print(SnapshotQueryExecutionDTO.to_json())

# convert the object into a dict
snapshot_query_execution_dto_dict = snapshot_query_execution_dto_instance.to_dict()
# create an instance of SnapshotQueryExecutionDTO from a dict
snapshot_query_execution_dto_from_dict = SnapshotQueryExecutionDTO.from_dict(snapshot_query_execution_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


