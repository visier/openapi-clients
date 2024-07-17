# PermissionsToUserGroupRequestDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions_ids** | **List[str]** | A list of strings representing the unique permission IDs to assign. | [optional] 
**user_group_id** | **str** | The unique identifier associated with the user group. | [optional] 

## Example

```python
from visier.api.user_management.models.permissions_to_user_group_request_dto import PermissionsToUserGroupRequestDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionsToUserGroupRequestDTO from a JSON string
permissions_to_user_group_request_dto_instance = PermissionsToUserGroupRequestDTO.from_json(json)
# print the JSON string representation of the object
print(PermissionsToUserGroupRequestDTO.to_json())

# convert the object into a dict
permissions_to_user_group_request_dto_dict = permissions_to_user_group_request_dto_instance.to_dict()
# create an instance of PermissionsToUserGroupRequestDTO from a dict
permissions_to_user_group_request_dto_from_dict = PermissionsToUserGroupRequestDTO.from_dict(permissions_to_user_group_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


