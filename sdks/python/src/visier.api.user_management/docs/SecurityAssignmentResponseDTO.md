# SecurityAssignmentResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenants** | [**List[TenantAssignmentsDTO]**](TenantAssignmentsDTO.md) | A list of objects representing the tenants and users that were assigned to or removed from user groups. | [optional] 

## Example

```python
from visier.api.user_management.models.security_assignment_response_dto import SecurityAssignmentResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityAssignmentResponseDTO from a JSON string
security_assignment_response_dto_instance = SecurityAssignmentResponseDTO.from_json(json)
# print the JSON string representation of the object
print(SecurityAssignmentResponseDTO.to_json())

# convert the object into a dict
security_assignment_response_dto_dict = security_assignment_response_dto_instance.to_dict()
# create an instance of SecurityAssignmentResponseDTO from a dict
security_assignment_response_dto_from_dict = SecurityAssignmentResponseDTO.from_dict(security_assignment_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


