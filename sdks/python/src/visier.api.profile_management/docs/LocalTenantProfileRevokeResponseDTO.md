# LocalTenantProfileRevokeResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failed** | [**List[FailedLocalTenantProfileRevokeDTO]**](FailedLocalTenantProfileRevokeDTO.md) | A list of objects representing any errors that occurred during the assignment operation. | [optional] 
**succeeded** | [**List[SuccessfulLocalTenantProfileAssignmentDTO]**](SuccessfulLocalTenantProfileAssignmentDTO.md) | A list of the user IDs that successfully had a profile removed. | [optional] 

## Example

```python
from visier.api.profile_management.models.local_tenant_profile_revoke_response_dto import LocalTenantProfileRevokeResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of LocalTenantProfileRevokeResponseDTO from a JSON string
local_tenant_profile_revoke_response_dto_instance = LocalTenantProfileRevokeResponseDTO.from_json(json)
# print the JSON string representation of the object
print(LocalTenantProfileRevokeResponseDTO.to_json())

# convert the object into a dict
local_tenant_profile_revoke_response_dto_dict = local_tenant_profile_revoke_response_dto_instance.to_dict()
# create an instance of LocalTenantProfileRevokeResponseDTO from a dict
local_tenant_profile_revoke_response_dto_from_dict = LocalTenantProfileRevokeResponseDTO.from_dict(local_tenant_profile_revoke_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


