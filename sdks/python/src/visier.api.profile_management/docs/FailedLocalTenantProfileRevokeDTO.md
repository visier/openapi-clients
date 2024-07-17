# FailedLocalTenantProfileRevokeDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The details about the error. | [optional] 
**user_id** | **str** | The impacted user ID. | [optional] 

## Example

```python
from visier.api.profile_management.models.failed_local_tenant_profile_revoke_dto import FailedLocalTenantProfileRevokeDTO

# TODO update the JSON string below
json = "{}"
# create an instance of FailedLocalTenantProfileRevokeDTO from a JSON string
failed_local_tenant_profile_revoke_dto_instance = FailedLocalTenantProfileRevokeDTO.from_json(json)
# print the JSON string representation of the object
print(FailedLocalTenantProfileRevokeDTO.to_json())

# convert the object into a dict
failed_local_tenant_profile_revoke_dto_dict = failed_local_tenant_profile_revoke_dto_instance.to_dict()
# create an instance of FailedLocalTenantProfileRevokeDTO from a dict
failed_local_tenant_profile_revoke_dto_from_dict = FailedLocalTenantProfileRevokeDTO.from_dict(failed_local_tenant_profile_revoke_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


