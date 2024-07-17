# UserGroupChangeMemberSelectionDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_excluded** | **bool** | If &#x60;true&#x60;, the specified member must not be defined for members of the user group. | [optional] 
**name_path** | **List[str]** | The name path for dimension members; for example, &#x60;[ \&quot;North America\&quot;, \&quot;US\&quot;, \&quot;CA\&quot; ]&#x60;. | [optional] 

## Example

```python
from visier.api.user_management.models.user_group_change_member_selection_dto import UserGroupChangeMemberSelectionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupChangeMemberSelectionDTO from a JSON string
user_group_change_member_selection_dto_instance = UserGroupChangeMemberSelectionDTO.from_json(json)
# print the JSON string representation of the object
print(UserGroupChangeMemberSelectionDTO.to_json())

# convert the object into a dict
user_group_change_member_selection_dto_dict = user_group_change_member_selection_dto_instance.to_dict()
# create an instance of UserGroupChangeMemberSelectionDTO from a dict
user_group_change_member_selection_dto_from_dict = UserGroupChangeMemberSelectionDTO.from_dict(user_group_change_member_selection_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


