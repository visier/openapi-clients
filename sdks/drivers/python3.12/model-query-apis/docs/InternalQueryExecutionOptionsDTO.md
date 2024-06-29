# InternalQueryExecutionOptionsDTO

Internal options - not to be documented or used by external parties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sparse_handling_mode** | **int** |  | [optional] 

## Example

```python
from visier.model_query.models.internal_query_execution_options_dto import InternalQueryExecutionOptionsDTO

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


