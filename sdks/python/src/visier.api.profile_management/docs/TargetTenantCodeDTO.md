# TargetTenantCodeDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**for_all_children** | **bool** | If true, the assignment is for all the analytic tenants of the specified tenant. | [optional] 
**tenant_code** | **str** | The tenant code. | [optional] 

## Example

```python
from visier.api.profile_management.models.target_tenant_code_dto import TargetTenantCodeDTO

# TODO update the JSON string below
json = "{}"
# create an instance of TargetTenantCodeDTO from a JSON string
target_tenant_code_dto_instance = TargetTenantCodeDTO.from_json(json)
# print the JSON string representation of the object
print(TargetTenantCodeDTO.to_json())

# convert the object into a dict
target_tenant_code_dto_dict = target_tenant_code_dto_instance.to_dict()
# create an instance of TargetTenantCodeDTO from a dict
target_tenant_code_dto_from_dict = TargetTenantCodeDTO.from_dict(target_tenant_code_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


