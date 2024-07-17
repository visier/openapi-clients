# TenantStatusAPIDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_administer_other_tenants** | **bool** | If true, the tenant is an administrating tenant. | [optional] 
**status** | **str** | Whether the tenant is enabled or disabled. | [optional] 
**tenant_code** | **str** | The unique identifier for the analytic tenant. | [optional] 
**tenant_display_name** | **str** | The identifiable tenant name that is displayed within Visier. For example, \&quot;Callisto\&quot;. | [optional] 

## Example

```python
from visier.api.tenant_management.models.tenant_status_apidto import TenantStatusAPIDTO

# TODO update the JSON string below
json = "{}"
# create an instance of TenantStatusAPIDTO from a JSON string
tenant_status_apidto_instance = TenantStatusAPIDTO.from_json(json)
# print the JSON string representation of the object
print(TenantStatusAPIDTO.to_json())

# convert the object into a dict
tenant_status_apidto_dict = tenant_status_apidto_instance.to_dict()
# create an instance of TenantStatusAPIDTO from a dict
tenant_status_apidto_from_dict = TenantStatusAPIDTO.from_dict(tenant_status_apidto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


