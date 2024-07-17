# TenantCodeErrorDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**ErrorDTO**](ErrorDTO.md) | The details about the error. | [optional] 
**for_all_children** | **bool** | If true, the target assignment is for all analytic tenants. | [optional] 
**tenant_code** | **str** | The bad tenant code. | [optional] 

## Example

```python
from visier.api.profile_management.models.tenant_code_error_dto import TenantCodeErrorDTO

# TODO update the JSON string below
json = "{}"
# create an instance of TenantCodeErrorDTO from a JSON string
tenant_code_error_dto_instance = TenantCodeErrorDTO.from_json(json)
# print the JSON string representation of the object
print(TenantCodeErrorDTO.to_json())

# convert the object into a dict
tenant_code_error_dto_dict = tenant_code_error_dto_instance.to_dict()
# create an instance of TenantCodeErrorDTO from a dict
tenant_code_error_dto_from_dict = TenantCodeErrorDTO.from_dict(tenant_code_error_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


