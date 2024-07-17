# DirectDataSchemaFieldDTO

The definition of each field in an object's schema.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | **str** | The column&#39;s data type. | [optional] 
**empty_values_allowed** | **bool** | If true, the value may be empty. | [optional] 
**formats** | **List[str]** | The column&#39;s accepted formats, such as date formats like \&quot;yyyy-MM-dd\&quot;. | [optional] 
**is_mandatory** | **bool** | If true, the field must contain a value to successfully load data into the object. | [optional] 
**name** | **str** | The field&#39;s column name. Column names are case sensitive. | [optional] 

## Example

```python
from visier.api.direct_data_intake.models.direct_data_schema_field_dto import DirectDataSchemaFieldDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DirectDataSchemaFieldDTO from a JSON string
direct_data_schema_field_dto_instance = DirectDataSchemaFieldDTO.from_json(json)
# print the JSON string representation of the object
print(DirectDataSchemaFieldDTO.to_json())

# convert the object into a dict
direct_data_schema_field_dto_dict = direct_data_schema_field_dto_instance.to_dict()
# create an instance of DirectDataSchemaFieldDTO from a dict
direct_data_schema_field_dto_from_dict = DirectDataSchemaFieldDTO.from_dict(direct_data_schema_field_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


