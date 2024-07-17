# TenantAssignmentsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignments** | [**List[UserSecurityAssignmentsDTO]**](UserSecurityAssignmentsDTO.md) | A list of objects representing the user group and user assignments. | [optional] 
**message** | **str** | A detailed description of the request outcome, if available. | [optional] 
**status** | **str** | The state of the user group assignment. Valid values are Succeed or Failed. | [optional] 
**tenant_code** | **str** | The unique identifier associated with the tenant. | [optional] 

## Example

```python
from visier.api.user_management.models.tenant_assignments_dto import TenantAssignmentsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of TenantAssignmentsDTO from a JSON string
tenant_assignments_dto_instance = TenantAssignmentsDTO.from_json(json)
# print the JSON string representation of the object
print(TenantAssignmentsDTO.to_json())

# convert the object into a dict
tenant_assignments_dto_dict = tenant_assignments_dto_instance.to_dict()
# create an instance of TenantAssignmentsDTO from a dict
tenant_assignments_dto_from_dict = TenantAssignmentsDTO.from_dict(tenant_assignments_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


