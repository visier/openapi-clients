# AggregationQueryExecutionDTO

An AggregationQueryExecution provides instructions to perform your aggregation query.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | [**QueryExecutionOptionsDTO**](QueryExecutionOptionsDTO.md) | Additional instructions for your query, such as a calendar type or conversion information. | [optional] 
**query** | [**AggregationQueryDTO**](AggregationQueryDTO.md) | The data to perform an aggregation on, such as a metric or formula. The query must include a time interval,  and may optionally include filters and axes. | [optional] 

## Example

```python
from visier.model_query_apis.models.aggregation_query_execution_dto import AggregationQueryExecutionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AggregationQueryExecutionDTO from a JSON string
aggregation_query_execution_dto_instance = AggregationQueryExecutionDTO.from_json(json)
# print the JSON string representation of the object
print(AggregationQueryExecutionDTO.to_json())

# convert the object into a dict
aggregation_query_execution_dto_dict = aggregation_query_execution_dto_instance.to_dict()
# create an instance of AggregationQueryExecutionDTO from a dict
aggregation_query_execution_dto_from_dict = AggregationQueryExecutionDTO.from_dict(aggregation_query_execution_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


