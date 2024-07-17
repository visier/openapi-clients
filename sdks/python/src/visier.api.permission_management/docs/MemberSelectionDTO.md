# MemberSelectionDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimension_member_status** | **str** | The dimension member&#39;s validity status. Valid values: Valid, NotFound.  * **Valid**: The object exists and has loaded data.  * **NotFound**: The object doesn&#39;t exist. | [optional] 
**excluded** | **bool** | If &#x60;true&#x60;, population access is granted for all members except this member. | [optional] 
**name_path** | **List[str]** | The member name path. | [optional] 

## Example

```python
from visier.api.permission_management.models.member_selection_dto import MemberSelectionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MemberSelectionDTO from a JSON string
member_selection_dto_instance = MemberSelectionDTO.from_json(json)
# print the JSON string representation of the object
print(MemberSelectionDTO.to_json())

# convert the object into a dict
member_selection_dto_dict = member_selection_dto_instance.to_dict()
# create an instance of MemberSelectionDTO from a dict
member_selection_dto_from_dict = MemberSelectionDTO.from_dict(member_selection_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


