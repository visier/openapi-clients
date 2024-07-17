# FailedAccessibleTenantProfileAssignmentDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**ErrorDTO**](ErrorDTO.md) | The details about the error. | [optional] 
**for_all_children** | **bool** | If true, the target assignment is for all analytic tenants. | [optional] 
**tenant_code** | **str** | The tenant code. | [optional] 
**user_id** | **str** | The impacted user ID. | [optional] 

## Example

```python
from visier.api.profile_management.models.failed_accessible_tenant_profile_assignment_dto import FailedAccessibleTenantProfileAssignmentDTO

# TODO update the JSON string below
json = "{}"
# create an instance of FailedAccessibleTenantProfileAssignmentDTO from a JSON string
failed_accessible_tenant_profile_assignment_dto_instance = FailedAccessibleTenantProfileAssignmentDTO.from_json(json)
# print the JSON string representation of the object
print(FailedAccessibleTenantProfileAssignmentDTO.to_json())

# convert the object into a dict
failed_accessible_tenant_profile_assignment_dto_dict = failed_accessible_tenant_profile_assignment_dto_instance.to_dict()
# create an instance of FailedAccessibleTenantProfileAssignmentDTO from a dict
failed_accessible_tenant_profile_assignment_dto_from_dict = FailedAccessibleTenantProfileAssignmentDTO.from_dict(failed_accessible_tenant_profile_assignment_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


