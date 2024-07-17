# LocalTenantProfileRevokeRequestDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_user_ids** | **List[str]** | A list of users to remove this profile from. | [optional] 

## Example

```python
from visier.api.profile_management.models.local_tenant_profile_revoke_request_dto import LocalTenantProfileRevokeRequestDTO

# TODO update the JSON string below
json = "{}"
# create an instance of LocalTenantProfileRevokeRequestDTO from a JSON string
local_tenant_profile_revoke_request_dto_instance = LocalTenantProfileRevokeRequestDTO.from_json(json)
# print the JSON string representation of the object
print(LocalTenantProfileRevokeRequestDTO.to_json())

# convert the object into a dict
local_tenant_profile_revoke_request_dto_dict = local_tenant_profile_revoke_request_dto_instance.to_dict()
# create an instance of LocalTenantProfileRevokeRequestDTO from a dict
local_tenant_profile_revoke_request_dto_from_dict = LocalTenantProfileRevokeRequestDTO.from_dict(local_tenant_profile_revoke_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


