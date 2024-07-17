# AccessibleTenantProfileAssignmentRequestDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_tenant_codes** | [**List[TargetTenantCodeDTO]**](TargetTenantCodeDTO.md) | A list of objects representing the  analytic tenants for profiles assigned to the users. | [optional] 
**target_user_ids** | **List[str]** | A list of users to assign this profile. | [optional] 
**validity_end_time** | **str** | An exclusive date-time when this profile is no longer active. | [optional] 
**validity_start_time** | **str** | An inclusive date-time when this profile is active. | [optional] 

## Example

```python
from visier.api.profile_management.models.accessible_tenant_profile_assignment_request_dto import AccessibleTenantProfileAssignmentRequestDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AccessibleTenantProfileAssignmentRequestDTO from a JSON string
accessible_tenant_profile_assignment_request_dto_instance = AccessibleTenantProfileAssignmentRequestDTO.from_json(json)
# print the JSON string representation of the object
print(AccessibleTenantProfileAssignmentRequestDTO.to_json())

# convert the object into a dict
accessible_tenant_profile_assignment_request_dto_dict = accessible_tenant_profile_assignment_request_dto_instance.to_dict()
# create an instance of AccessibleTenantProfileAssignmentRequestDTO from a dict
accessible_tenant_profile_assignment_request_dto_from_dict = AccessibleTenantProfileAssignmentRequestDTO.from_dict(accessible_tenant_profile_assignment_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


