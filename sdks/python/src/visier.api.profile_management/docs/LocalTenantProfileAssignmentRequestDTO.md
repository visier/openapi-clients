# LocalTenantProfileAssignmentRequestDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_user_ids** | **List[str]** | A list of users to assign this profile. | [optional] 
**validity_end_time** | **str** | An exclusive date-time when this profile is no longer active. | [optional] 
**validity_start_time** | **str** | An inclusive date-time when this profile is active. | [optional] 

## Example

```python
from visier.api.profile_management.models.local_tenant_profile_assignment_request_dto import LocalTenantProfileAssignmentRequestDTO

# TODO update the JSON string below
json = "{}"
# create an instance of LocalTenantProfileAssignmentRequestDTO from a JSON string
local_tenant_profile_assignment_request_dto_instance = LocalTenantProfileAssignmentRequestDTO.from_json(json)
# print the JSON string representation of the object
print(LocalTenantProfileAssignmentRequestDTO.to_json())

# convert the object into a dict
local_tenant_profile_assignment_request_dto_dict = local_tenant_profile_assignment_request_dto_instance.to_dict()
# create an instance of LocalTenantProfileAssignmentRequestDTO from a dict
local_tenant_profile_assignment_request_dto_from_dict = LocalTenantProfileAssignmentRequestDTO.from_dict(local_tenant_profile_assignment_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


