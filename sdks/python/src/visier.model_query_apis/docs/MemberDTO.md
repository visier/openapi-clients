# MemberDTO

A member is an element of a dimension. Dimension members are organized hierarchically. For example, Argentina is  a member of the Location dimension at the Country level of the hierarchy Region > Country > Province > City.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The localized display name of the member. | [optional] 
**display_name_path** | **List[str]** | The display names for each level in the member&#39;s ancestral path. | [optional] 
**full_name** | **str** | The fully qualified name of the member. This is the dimension&#39;s object name and the member&#39;s display name, separated by a period. | [optional] 
**level** | **int** | The numeric level of the hierarchy the member belongs to. | [optional] 
**path** | **List[str]** | A comma-separated list of identifiers that reference members on the query axis as part of dimensionMemberSelection. | [optional] 
**validity_ranges** | [**List[ValidityRangeDTO]**](ValidityRangeDTO.md) | The validity ranges that exist for this member. | [optional] 

## Example

```python
from visier.model_query_apis.models.member_dto import MemberDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MemberDTO from a JSON string
member_dto_instance = MemberDTO.from_json(json)
# print the JSON string representation of the object
print(MemberDTO.to_json())

# convert the object into a dict
member_dto_dict = member_dto_instance.to_dict()
# create an instance of MemberDTO from a dict
member_dto_from_dict = MemberDTO.from_dict(member_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


