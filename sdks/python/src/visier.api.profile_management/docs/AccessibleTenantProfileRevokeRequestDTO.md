# AccessibleTenantProfileRevokeRequestDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_tenant_codes** | [**List[TargetTenantCodeDTO]**](TargetTenantCodeDTO.md) | A list of objects representing the  analytic tenants for removing profiles from each target user ID. | [optional] 
**target_user_ids** | **List[str]** | A list of users to remove this profile from. | [optional] 

## Example

```python
from visier.api.profile_management.models.accessible_tenant_profile_revoke_request_dto import AccessibleTenantProfileRevokeRequestDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AccessibleTenantProfileRevokeRequestDTO from a JSON string
accessible_tenant_profile_revoke_request_dto_instance = AccessibleTenantProfileRevokeRequestDTO.from_json(json)
# print the JSON string representation of the object
print(AccessibleTenantProfileRevokeRequestDTO.to_json())

# convert the object into a dict
accessible_tenant_profile_revoke_request_dto_dict = accessible_tenant_profile_revoke_request_dto_instance.to_dict()
# create an instance of AccessibleTenantProfileRevokeRequestDTO from a dict
accessible_tenant_profile_revoke_request_dto_from_dict = AccessibleTenantProfileRevokeRequestDTO.from_dict(accessible_tenant_profile_revoke_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


