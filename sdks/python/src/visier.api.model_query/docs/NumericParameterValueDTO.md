# NumericParameterValueDTO

The value of a numeric parameter, including the parameter ID and the numeric value passed into the parameter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameter_id** | **str** | The unique ID of the numeric parameter qualified by the object. | [optional] 
**value** | **float** | The numeric value of the parameter. | [optional] 

## Example

```python
from visier.api.model_query.models.numeric_parameter_value_dto import NumericParameterValueDTO

# TODO update the JSON string below
json = "{}"
# create an instance of NumericParameterValueDTO from a JSON string
numeric_parameter_value_dto_instance = NumericParameterValueDTO.from_json(json)
# print the JSON string representation of the object
print(NumericParameterValueDTO.to_json())

# convert the object into a dict
numeric_parameter_value_dto_dict = numeric_parameter_value_dto_instance.to_dict()
# create an instance of NumericParameterValueDTO from a dict
numeric_parameter_value_dto_from_dict = NumericParameterValueDTO.from_dict(numeric_parameter_value_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


