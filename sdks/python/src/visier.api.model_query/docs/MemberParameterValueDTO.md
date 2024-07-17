# MemberParameterValueDTO

The member value of a parameter, including the parameter ID, dimension that the parameter is based on,  and the included and excluded members for the parameter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimension_id** | **str** | The unique ID of the dimension on which the parameter is based. | [optional] 
**parameter_id** | **str** | The unique ID of the member parameter qualified by the object. | [optional] 
**reference_path** | **List[str]** | The analytic object reference path from the metric to the dimension. | [optional] 
**values** | [**MemberValuesDTO**](MemberValuesDTO.md) | The included and excluded member references in a dimension filter. | [optional] 

## Example

```python
from visier.api.model_query.models.member_parameter_value_dto import MemberParameterValueDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MemberParameterValueDTO from a JSON string
member_parameter_value_dto_instance = MemberParameterValueDTO.from_json(json)
# print the JSON string representation of the object
print(MemberParameterValueDTO.to_json())

# convert the object into a dict
member_parameter_value_dto_dict = member_parameter_value_dto_instance.to_dict()
# create an instance of MemberParameterValueDTO from a dict
member_parameter_value_dto_from_dict = MemberParameterValueDTO.from_dict(member_parameter_value_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


