# ListQueryExecutionDTO

A ListQueryExecution provides instructions to perform a list query.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | [**List[PropertyColumnDTO]**](PropertyColumnDTO.md) | The columns to include in the result. This must contain at least one column. | [optional] 
**filters** | [**List[QueryFilterDTO]**](QueryFilterDTO.md) | The filters of this query. Omit &#x60;filters&#x60; if no filtering is required. | [optional] 
**options** | [**ListQueryExecutionOptionsDTO**](ListQueryExecutionOptionsDTO.md) | Additional instructions for your query, such as a calendar type or conversion information. | [optional] 
**parameter_values** | [**List[QueryParameterValueDTO]**](QueryParameterValueDTO.md) | The parameter values for either member or numeric parameters. | [optional] 
**sort_options** | [**List[SortOptionDTO]**](SortOptionDTO.md) | The index and direction to sort a column in the &#x60;columns&#x60; array. | [optional] 
**source** | [**ListQuerySourceDTO**](ListQuerySourceDTO.md) | The source data that you want to query. | [optional] 
**time_interval** | [**QueryTimeIntervalDTO**](QueryTimeIntervalDTO.md) | The time that the data is valid, such as a specific day or period of months. | [optional] 

## Example

```python
from visier.model_query_apis.models.list_query_execution_dto import ListQueryExecutionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ListQueryExecutionDTO from a JSON string
list_query_execution_dto_instance = ListQueryExecutionDTO.from_json(json)
# print the JSON string representation of the object
print(ListQueryExecutionDTO.to_json())

# convert the object into a dict
list_query_execution_dto_dict = list_query_execution_dto_instance.to_dict()
# create an instance of ListQueryExecutionDTO from a dict
list_query_execution_dto_from_dict = ListQueryExecutionDTO.from_dict(list_query_execution_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


