# PropertyColumnDTO

A named, result column of a list query.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_definition** | [**QueryPropertyDTO**](QueryPropertyDTO.md) | The definition of the property to query on. | [optional] 
**column_name** | **str** | The name of the column. This is optional.  If not specified, the name of the property is used, or a generic column name if the property is unnamed. | [optional] 

## Example

```python
from visier.api.model_query.models.property_column_dto import PropertyColumnDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyColumnDTO from a JSON string
property_column_dto_instance = PropertyColumnDTO.from_json(json)
# print the JSON string representation of the object
print(PropertyColumnDTO.to_json())

# convert the object into a dict
property_column_dto_dict = property_column_dto_instance.to_dict()
# create an instance of PropertyColumnDTO from a dict
property_column_dto_from_dict = PropertyColumnDTO.from_dict(property_column_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


