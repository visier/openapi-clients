# FailedLocalTenantProfileAssignmentDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**ErrorDTO**](ErrorDTO.md) | The details about the error. | [optional] 
**user_id** | **str** | The impacted user ID. | [optional] 

## Example

```python
from visier.api.profile_management.models.failed_local_tenant_profile_assignment_dto import FailedLocalTenantProfileAssignmentDTO

# TODO update the JSON string below
json = "{}"
# create an instance of FailedLocalTenantProfileAssignmentDTO from a JSON string
failed_local_tenant_profile_assignment_dto_instance = FailedLocalTenantProfileAssignmentDTO.from_json(json)
# print the JSON string representation of the object
print(FailedLocalTenantProfileAssignmentDTO.to_json())

# convert the object into a dict
failed_local_tenant_profile_assignment_dto_dict = failed_local_tenant_profile_assignment_dto_instance.to_dict()
# create an instance of FailedLocalTenantProfileAssignmentDTO from a dict
failed_local_tenant_profile_assignment_dto_from_dict = FailedLocalTenantProfileAssignmentDTO.from_dict(failed_local_tenant_profile_assignment_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


