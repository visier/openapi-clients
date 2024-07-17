# AccessibleTenantProfileRevokeResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bad_tenant_codes** | [**List[ReducedTenantCodeErrorDTO]**](ReducedTenantCodeErrorDTO.md) | A list of objects representing any tenants that returned errors. | [optional] 
**bad_user_ids** | [**List[ReducedUserIdErrorDTO]**](ReducedUserIdErrorDTO.md) | A list of objects representing the user IDs that may not be valid. | [optional] 
**succeeded** | [**List[SuccessfulLocalTenantProfileAssignmentDTO]**](SuccessfulLocalTenantProfileAssignmentDTO.md) | A list of objects representing the valid user IDs that succeeded. | [optional] 
**unaffected_users** | [**List[SuccessfulLocalTenantProfileAssignmentDTO]**](SuccessfulLocalTenantProfileAssignmentDTO.md) | A list of objects representing the valid user IDs that were not affected. | [optional] 

## Example

```python
from visier.api.profile_management.models.accessible_tenant_profile_revoke_response_dto import AccessibleTenantProfileRevokeResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AccessibleTenantProfileRevokeResponseDTO from a JSON string
accessible_tenant_profile_revoke_response_dto_instance = AccessibleTenantProfileRevokeResponseDTO.from_json(json)
# print the JSON string representation of the object
print(AccessibleTenantProfileRevokeResponseDTO.to_json())

# convert the object into a dict
accessible_tenant_profile_revoke_response_dto_dict = accessible_tenant_profile_revoke_response_dto_instance.to_dict()
# create an instance of AccessibleTenantProfileRevokeResponseDTO from a dict
accessible_tenant_profile_revoke_response_dto_from_dict = AccessibleTenantProfileRevokeResponseDTO.from_dict(accessible_tenant_profile_revoke_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


