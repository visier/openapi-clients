# PropertyDTO

Properties are qualities of an analytic object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the property.  **Note:** See &#x60;Properties&#x60; to get the ID. | [optional] 
**display_name** | **str** | The localized display name of the property. | [optional] 
**description** | **str** | The localized description of the property. | [optional] 
**data_type** | **str** | The data type of the property, such as Categorical, HourDuration, or Ratio. | [optional] 
**primitive_data_type** | **str** | The primitive data type of the property, such as Number, String, or Boolean. | [optional] 
**parameters** | [**List[ParameterDefinitionDTO]**](ParameterDefinitionDTO.md) | The collection of parameters defined for the property. | [optional] 

## Example

```python
from visier.model_query.models.property_dto import PropertyDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyDTO from a JSON string
property_dto_instance = PropertyDTO.from_json(json)
# print the JSON string representation of the object
print(PropertyDTO.to_json())

# convert the object into a dict
property_dto_dict = property_dto_instance.to_dict()
# create an instance of PropertyDTO from a dict
property_dto_from_dict = PropertyDTO.from_dict(property_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


