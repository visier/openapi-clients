# NumericParameterDefinitionDTO

The definition of a numeric parameter. These elements are returned as part of the query definition for metric parameter values.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **float** | The default value if the end user does not select a member at run time. | [optional] 
**description** | **str** | The localized description of the numeric parameter. | [optional] 
**display_name** | **str** | The localized display name of the numeric parameter. | [optional] 
**id** | **str** | The unique ID of the numeric parameter. | [optional] 
**lower_bound** | **float** | The lowest value for the numeric parameter. | [optional] 
**upper_bound** | **float** | The highest value for the numeric parameter. | [optional] 

## Example

```python
from visier.model_query_apis.models.numeric_parameter_definition_dto import NumericParameterDefinitionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of NumericParameterDefinitionDTO from a JSON string
numeric_parameter_definition_dto_instance = NumericParameterDefinitionDTO.from_json(json)
# print the JSON string representation of the object
print(NumericParameterDefinitionDTO.to_json())

# convert the object into a dict
numeric_parameter_definition_dto_dict = numeric_parameter_definition_dto_instance.to_dict()
# create an instance of NumericParameterDefinitionDTO from a dict
numeric_parameter_definition_dto_from_dict = NumericParameterDefinitionDTO.from_dict(numeric_parameter_definition_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


