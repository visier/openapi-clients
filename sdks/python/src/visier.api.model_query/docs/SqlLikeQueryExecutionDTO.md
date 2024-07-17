# SqlLikeQueryExecutionDTO

*  Request body for SQL-like query executions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | [**QueryExecutionOptionsDTO**](QueryExecutionOptionsDTO.md) | Optional options that currently that cannot be expressed in SQL-like | [optional] 
**query** | **str** | The SQL-like query string | [optional] 

## Example

```python
from visier.api.model_query.models.sql_like_query_execution_dto import SqlLikeQueryExecutionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SqlLikeQueryExecutionDTO from a JSON string
sql_like_query_execution_dto_instance = SqlLikeQueryExecutionDTO.from_json(json)
# print the JSON string representation of the object
print(SqlLikeQueryExecutionDTO.to_json())

# convert the object into a dict
sql_like_query_execution_dto_dict = sql_like_query_execution_dto_instance.to_dict()
# create an instance of SqlLikeQueryExecutionDTO from a dict
sql_like_query_execution_dto_from_dict = SqlLikeQueryExecutionDTO.from_dict(sql_like_query_execution_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


