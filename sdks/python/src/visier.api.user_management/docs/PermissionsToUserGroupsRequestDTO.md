# PermissionsToUserGroupsRequestDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_groups** | [**List[PermissionsToUserGroupRequestDTO]**](PermissionsToUserGroupRequestDTO.md) | A list of objects representing the user groups and permissions to assign or remove. | [optional] 

## Example

```python
from visier.api.user_management.models.permissions_to_user_groups_request_dto import PermissionsToUserGroupsRequestDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionsToUserGroupsRequestDTO from a JSON string
permissions_to_user_groups_request_dto_instance = PermissionsToUserGroupsRequestDTO.from_json(json)
# print the JSON string representation of the object
print(PermissionsToUserGroupsRequestDTO.to_json())

# convert the object into a dict
permissions_to_user_groups_request_dto_dict = permissions_to_user_groups_request_dto_instance.to_dict()
# create an instance of PermissionsToUserGroupsRequestDTO from a dict
permissions_to_user_groups_request_dto_from_dict = PermissionsToUserGroupsRequestDTO.from_dict(permissions_to_user_groups_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


