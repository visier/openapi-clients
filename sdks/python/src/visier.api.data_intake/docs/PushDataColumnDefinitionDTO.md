# PushDataColumnDefinitionDTO

Definition of the source column.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_empty** | **bool** | If true, the column allows an empty value for the record. | [optional] 
**column_name** | **str** | The name of the column. | [optional] 
**data_formats** | **List[str]** | The expected format for datetime data types. | [optional] 
**data_type** | **str** | The data type associated with the column. | [optional] 
**default_value** | **str** | The default value of the column. | [optional] 
**is_mandatory** | **bool** | If true, the column value is required. If a column is mandatory, and the file is missing this column, the request will fail. | [optional] 

## Example

```python
from visier.api.data_intake.models.push_data_column_definition_dto import PushDataColumnDefinitionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PushDataColumnDefinitionDTO from a JSON string
push_data_column_definition_dto_instance = PushDataColumnDefinitionDTO.from_json(json)
# print the JSON string representation of the object
print(PushDataColumnDefinitionDTO.to_json())

# convert the object into a dict
push_data_column_definition_dto_dict = push_data_column_definition_dto_instance.to_dict()
# create an instance of PushDataColumnDefinitionDTO from a dict
push_data_column_definition_dto_from_dict = PushDataColumnDefinitionDTO.from_dict(push_data_column_definition_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


