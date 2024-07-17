# MemberParameterDefinitionDTO

The definition of a filter parameter. These elements are returned as part of the definition for metrics that include parameters in their definition.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | [**MemberValuesDTO**](MemberValuesDTO.md) | The default value if the end user does not select a member at run time. | [optional] 
**description** | **str** | The localized description of the member parameter. | [optional] 
**dimension_id** | **str** | The unique ID of the dimension on which the member parameter is based. | [optional] 
**display_name** | **str** | The localized display name of the member parameter. | [optional] 
**id** | **str** | The unique ID of the member parameter. | [optional] 
**reference_path** | **List[str]** | The analytic object reference path from the metric to the dimension. | [optional] 

## Example

```python
from visier.api.model_query.models.member_parameter_definition_dto import MemberParameterDefinitionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MemberParameterDefinitionDTO from a JSON string
member_parameter_definition_dto_instance = MemberParameterDefinitionDTO.from_json(json)
# print the JSON string representation of the object
print(MemberParameterDefinitionDTO.to_json())

# convert the object into a dict
member_parameter_definition_dto_dict = member_parameter_definition_dto_instance.to_dict()
# create an instance of MemberParameterDefinitionDTO from a dict
member_parameter_definition_dto_from_dict = MemberParameterDefinitionDTO.from_dict(member_parameter_definition_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


