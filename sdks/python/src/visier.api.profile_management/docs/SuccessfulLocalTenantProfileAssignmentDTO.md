# SuccessfulLocalTenantProfileAssignmentDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The user ID. | [optional] 

## Example

```python
from visier.api.profile_management.models.successful_local_tenant_profile_assignment_dto import SuccessfulLocalTenantProfileAssignmentDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessfulLocalTenantProfileAssignmentDTO from a JSON string
successful_local_tenant_profile_assignment_dto_instance = SuccessfulLocalTenantProfileAssignmentDTO.from_json(json)
# print the JSON string representation of the object
print(SuccessfulLocalTenantProfileAssignmentDTO.to_json())

# convert the object into a dict
successful_local_tenant_profile_assignment_dto_dict = successful_local_tenant_profile_assignment_dto_instance.to_dict()
# create an instance of SuccessfulLocalTenantProfileAssignmentDTO from a dict
successful_local_tenant_profile_assignment_dto_from_dict = SuccessfulLocalTenantProfileAssignmentDTO.from_dict(successful_local_tenant_profile_assignment_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


