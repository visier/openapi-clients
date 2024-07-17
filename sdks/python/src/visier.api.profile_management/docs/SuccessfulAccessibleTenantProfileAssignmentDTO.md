# SuccessfulAccessibleTenantProfileAssignmentDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**for_all_children** | **bool** | If true, the target assignment is for all analytic tenants. | [optional] 
**tenant_code** | **str** | The tenant code. | [optional] 
**user_id** | **str** | The user ID. | [optional] 

## Example

```python
from visier.api.profile_management.models.successful_accessible_tenant_profile_assignment_dto import SuccessfulAccessibleTenantProfileAssignmentDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessfulAccessibleTenantProfileAssignmentDTO from a JSON string
successful_accessible_tenant_profile_assignment_dto_instance = SuccessfulAccessibleTenantProfileAssignmentDTO.from_json(json)
# print the JSON string representation of the object
print(SuccessfulAccessibleTenantProfileAssignmentDTO.to_json())

# convert the object into a dict
successful_accessible_tenant_profile_assignment_dto_dict = successful_accessible_tenant_profile_assignment_dto_instance.to_dict()
# create an instance of SuccessfulAccessibleTenantProfileAssignmentDTO from a dict
successful_accessible_tenant_profile_assignment_dto_from_dict = SuccessfulAccessibleTenantProfileAssignmentDTO.from_dict(successful_accessible_tenant_profile_assignment_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


