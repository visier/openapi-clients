# MembersDTO

A collection of members.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members** | [**List[MemberDTO]**](MemberDTO.md) |  | [optional] 

## Example

```python
from visier.model_query.models.members_dto import MembersDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MembersDTO from a JSON string
members_dto_instance = MembersDTO.from_json(json)
# print the JSON string representation of the object
print(MembersDTO.to_json())

# convert the object into a dict
members_dto_dict = members_dto_instance.to_dict()
# create an instance of MembersDTO from a dict
members_dto_from_dict = MembersDTO.from_dict(members_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


