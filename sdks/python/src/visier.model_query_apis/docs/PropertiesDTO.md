# PropertiesDTO

A collection of properties.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**List[PropertyDTO]**](PropertyDTO.md) |  | [optional] 

## Example

```python
from visier.model_query_apis.models.properties_dto import PropertiesDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PropertiesDTO from a JSON string
properties_dto_instance = PropertiesDTO.from_json(json)
# print the JSON string representation of the object
print(PropertiesDTO.to_json())

# convert the object into a dict
properties_dto_dict = properties_dto_instance.to_dict()
# create an instance of PropertiesDTO from a dict
properties_dto_from_dict = PropertiesDTO.from_dict(properties_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


