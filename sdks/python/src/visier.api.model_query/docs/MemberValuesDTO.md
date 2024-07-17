# MemberValuesDTO

Member filter values are discrete member references in a dimension filter. You can define  included and excluded members simultaneously. This is typically done with filtering applied on  dimensions with multiple levels. For example, a Location parameter may include “South  America” and exclude “Brazil” which results in the metric being evaluated for all South American  countries except Brazil.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**excluded** | [**List[DimensionMemberReferenceDTO]**](DimensionMemberReferenceDTO.md) | The unique IDs of members to exclude when evaluating the metric. | [optional] 
**included** | [**List[DimensionMemberReferenceDTO]**](DimensionMemberReferenceDTO.md) | The unique IDs of members to include when evaluating the metric. | [optional] 

## Example

```python
from visier.api.model_query.models.member_values_dto import MemberValuesDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MemberValuesDTO from a JSON string
member_values_dto_instance = MemberValuesDTO.from_json(json)
# print the JSON string representation of the object
print(MemberValuesDTO.to_json())

# convert the object into a dict
member_values_dto_dict = member_values_dto_instance.to_dict()
# create an instance of MemberValuesDTO from a dict
member_values_dto_from_dict = MemberValuesDTO.from_dict(member_values_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


