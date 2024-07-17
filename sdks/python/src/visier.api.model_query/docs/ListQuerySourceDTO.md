# ListQuerySourceDTO

A ListQuerySource defines the source data to query in a list query.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analytic_object** | **str** | The ID of an existing analytic object in your Visier solution.  An analytic object source cannot have filters or time handling. | [optional] 
**formula** | **str** | An ad-hoc metric formula. The response returns the individual data points that make up the aggregate. | [optional] 
**metric** | **str** | The ID of an existing metric in your Visier solution. | [optional] 

## Example

```python
from visier.api.model_query.models.list_query_source_dto import ListQuerySourceDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ListQuerySourceDTO from a JSON string
list_query_source_dto_instance = ListQuerySourceDTO.from_json(json)
# print the JSON string representation of the object
print(ListQuerySourceDTO.to_json())

# convert the object into a dict
list_query_source_dto_dict = list_query_source_dto_instance.to_dict()
# create an instance of ListQuerySourceDTO from a dict
list_query_source_dto_from_dict = ListQuerySourceDTO.from_dict(list_query_source_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


