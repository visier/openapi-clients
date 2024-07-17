# PermissionsToUserGroupForTenantDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A detailed description of the request outcome, if available. | [optional] 
**status** | **str** | The state of the permission assignment or removal. Valid values are Succeed or Failed. | [optional] 
**tenant_code** | **str** | The unique identifier associated with the tenant. | [optional] 
**user_groups** | [**List[UserGroupGetAPIResponseDTO]**](UserGroupGetAPIResponseDTO.md) | A list of objects representing user groups and the permissions to assign to or remove from them. | [optional] 

## Example

```python
from visier.api.user_management.models.permissions_to_user_group_for_tenant_dto import PermissionsToUserGroupForTenantDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionsToUserGroupForTenantDTO from a JSON string
permissions_to_user_group_for_tenant_dto_instance = PermissionsToUserGroupForTenantDTO.from_json(json)
# print the JSON string representation of the object
print(PermissionsToUserGroupForTenantDTO.to_json())

# convert the object into a dict
permissions_to_user_group_for_tenant_dto_dict = permissions_to_user_group_for_tenant_dto_instance.to_dict()
# create an instance of PermissionsToUserGroupForTenantDTO from a dict
permissions_to_user_group_for_tenant_dto_from_dict = PermissionsToUserGroupForTenantDTO.from_dict(permissions_to_user_group_for_tenant_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


