# PushDataSourceDefinitionsDTO

The existing sources.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sources** | [**List[PushDataSourceDefinitionDTO]**](PushDataSourceDefinitionDTO.md) | A list of objects representing the target sources for the request. | [optional] 

## Example

```python
from visier.api.data_intake.models.push_data_source_definitions_dto import PushDataSourceDefinitionsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PushDataSourceDefinitionsDTO from a JSON string
push_data_source_definitions_dto_instance = PushDataSourceDefinitionsDTO.from_json(json)
# print the JSON string representation of the object
print(PushDataSourceDefinitionsDTO.to_json())

# convert the object into a dict
push_data_source_definitions_dto_dict = push_data_source_definitions_dto_instance.to_dict()
# create an instance of PushDataSourceDefinitionsDTO from a dict
push_data_source_definitions_dto_from_dict = PushDataSourceDefinitionsDTO.from_dict(push_data_source_definitions_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


