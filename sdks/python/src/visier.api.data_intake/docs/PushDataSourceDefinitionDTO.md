# PushDataSourceDefinitionDTO

Details of each existing source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | [**List[PushDataColumnDefinitionDTO]**](PushDataColumnDefinitionDTO.md) | A list of objects representing the source columns. | [optional] 
**is_inherited** | **bool** | If true, the source is inherited by all analytic tenants. | [optional] 
**name** | **str** | The object name of the source. | [optional] 
**source_id** | **str** | The unique identifier associated with the source. | [optional] 

## Example

```python
from visier.api.data_intake.models.push_data_source_definition_dto import PushDataSourceDefinitionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PushDataSourceDefinitionDTO from a JSON string
push_data_source_definition_dto_instance = PushDataSourceDefinitionDTO.from_json(json)
# print the JSON string representation of the object
print(PushDataSourceDefinitionDTO.to_json())

# convert the object into a dict
push_data_source_definition_dto_dict = push_data_source_definition_dto_instance.to_dict()
# create an instance of PushDataSourceDefinitionDTO from a dict
push_data_source_definition_dto_from_dict = PushDataSourceDefinitionDTO.from_dict(push_data_source_definition_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


