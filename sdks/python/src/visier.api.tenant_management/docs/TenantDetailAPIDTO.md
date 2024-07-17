# TenantDetailAPIDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_administer_other_tenants** | **bool** | If true, the tenant is an administrating tenant. | [optional] 
**current_data_version** | **str** | The data version ID that the tenant is using. | [optional] 
**custom_properties** | [**List[CustomTenantPropertyDTO]**](CustomTenantPropertyDTO.md) | A set of key-value pairs that represent different customizable properties for the analytic tenant. | [optional] 
**data_version_date** | **str** | The date that the data version was published to production. | [optional] 
**embeddable_domains** | **List[str]** | A comma-separated list of strings that represent the URLs, or domains, in which Visier can be embedded. | [optional] 
**industry_code** | **int** | The 6-digit NAICS code for the industry to which the analytic tenant belongs. | [optional] 
**modules** | [**List[TenantModuleDTO]**](TenantModuleDTO.md) | The modules assigned to the analytic tenant. | [optional] 
**provision_date** | **str** | The date that the tenant was created. | [optional] 
**sso_instance_issuers** | **List[str]** | A comma-separated list of strings that represent the issuers for the SSO providers that can authenticate this tenant. | [optional] 
**status** | **str** | Whether the tenant is enabled or disabled. | [optional] 
**tenant_code** | **str** | The tenant code of the analytic tenant. For example, \&quot;WFF_j1r~i1o\&quot;. | [optional] 
**tenant_display_name** | **str** | An identifiable tenant name that is displayed within Visier. For example, \&quot;Callisto\&quot;. | [optional] 
**vanity_url_name** | **str** | The name of the administrating tenant used in Visier URLs. | [optional] 

## Example

```python
from visier.api.tenant_management.models.tenant_detail_apidto import TenantDetailAPIDTO

# TODO update the JSON string below
json = "{}"
# create an instance of TenantDetailAPIDTO from a JSON string
tenant_detail_apidto_instance = TenantDetailAPIDTO.from_json(json)
# print the JSON string representation of the object
print(TenantDetailAPIDTO.to_json())

# convert the object into a dict
tenant_detail_apidto_dict = tenant_detail_apidto_instance.to_dict()
# create an instance of TenantDetailAPIDTO from a dict
tenant_detail_apidto_from_dict = TenantDetailAPIDTO.from_dict(tenant_detail_apidto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


