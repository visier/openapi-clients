# ReducedTenantCodeErrorDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**ReducedErrorDTO**](ReducedErrorDTO.md) | The details about the error. | [optional] 
**for_all_children** | **bool** | If true, the assignment is for all the analytic tenants of the specified tenant. | [optional] 
**tenant_code** | **str** | The bad tenant code. | [optional] 

## Example

```python
from visier.api.profile_management.models.reduced_tenant_code_error_dto import ReducedTenantCodeErrorDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ReducedTenantCodeErrorDTO from a JSON string
reduced_tenant_code_error_dto_instance = ReducedTenantCodeErrorDTO.from_json(json)
# print the JSON string representation of the object
print(ReducedTenantCodeErrorDTO.to_json())

# convert the object into a dict
reduced_tenant_code_error_dto_dict = reduced_tenant_code_error_dto_instance.to_dict()
# create an instance of ReducedTenantCodeErrorDTO from a dict
reduced_tenant_code_error_dto_from_dict = ReducedTenantCodeErrorDTO.from_dict(reduced_tenant_code_error_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


