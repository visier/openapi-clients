# UserGroupChangeUsersDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dynamic_filter_definition** | [**UserGroupFiltersDTO**](UserGroupFiltersDTO.md) | The filters that dynamically define a population through dimensions or dimensions accessible through references from the analytic object.  * Omit if &#x60;includeAllUsers&#x60; is &#x60;true&#x60;.  * You can combine dynamic filters with manually-assigned users. | [optional] 
**include_all_users** | **bool** | If &#x60;true&#x60;, all users are included in the user group. If &#x60;true&#x60;:  * You can manually exclude users with &#x60;manuallyExcludedIds&#x60;.  * Cannot be combined with &#x60;manuallyIncludedIds&#x60; or &#x60;dynamicFilterDefinition&#x60;. | [optional] 
**manually_excluded_ids** | [**ElementIDsDTO**](ElementIDsDTO.md) | Excludes specified user IDs from the user group.  * You can manually exclude users if &#x60;includeAllUsers&#x60; is &#x60;true&#x60; or if &#x60;dynamicFilterDefinition&#x60; is defined.  * Excluded IDs must not overlap with user IDs in &#x60;manuallyIncludedIds&#x60;. | [optional] 
**manually_included_ids** | [**ElementIDsDTO**](ElementIDsDTO.md) | Includes specified user IDs in the user group.  * May be combined with &#x60;dynamicFilterDefinition&#x60;.  * Omit if &#x60;includeAllUsers&#x60; is &#x60;true&#x60;. | [optional] 

## Example

```python
from visier.api.user_management.models.user_group_change_users_dto import UserGroupChangeUsersDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupChangeUsersDTO from a JSON string
user_group_change_users_dto_instance = UserGroupChangeUsersDTO.from_json(json)
# print the JSON string representation of the object
print(UserGroupChangeUsersDTO.to_json())

# convert the object into a dict
user_group_change_users_dto_dict = user_group_change_users_dto_instance.to_dict()
# create an instance of UserGroupChangeUsersDTO from a dict
user_group_change_users_dto_from_dict = UserGroupChangeUsersDTO.from_dict(user_group_change_users_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


