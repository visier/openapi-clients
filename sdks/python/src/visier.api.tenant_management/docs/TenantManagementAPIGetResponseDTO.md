# TenantManagementAPIGetResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_administer_other_tenants** | **bool** | If true, the tenant is an administrating tenant. | [optional] 
**click_through_link** | **str** | The custom URL to redirect users into your portal to see the relevant content. This URL is used for links that are shared by and with your users through the sharing capability or email content. | [optional] 
**click_through_link_enabled** | **str** | Whether the click-through link is enabled or disabled. | [optional] 
**current_data_version** | **str** | The data version ID that the tenant is using. | [optional] 
**custom_properties** | [**List[CustomPropertyDTO]**](CustomPropertyDTO.md) | A set of key-value pairs that represent different customizable properties for the analytic tenant. | [optional] 
**data_version_date** | **str** | The date that the data version was published to production. | [optional] 
**default_currency** | **str** | The default currency to show in the application for the tenant. | [optional] 
**embeddable_domains** | **List[str]** | A comma-separated list of strings that represent the URLs, or domains, in which Visier can be embedded. | [optional] 
**home_analysis_by_user_group** | [**List[HomeAnalysisByUserGroupDTO]**](HomeAnalysisByUserGroupDTO.md) | A list of objects representing the analysis displayed to specific user groups when users log in. | [optional] 
**home_analysis_id** | **str** | The unique ID of the analysis that&#39;s displayed for this tenant when a user logs in. | [optional] 
**industry_code** | **int** | The 6-digit NAICS code for the industry to which the analytic tenant belongs. | [optional] 
**primary_business_location** | [**BusinessLocationDTO**](BusinessLocationDTO.md) | The primary location of operations or where business is performed. If undefined, it is omitted from the response. | [optional] 
**provision_date** | **str** | The date that the tenant was created. | [optional] 
**purchased_modules** | **List[str]** | The modules assigned to the analytic tenant. | [optional] 
**sso_instance_issuers** | **List[str]** | A comma-separated list of strings that represent the issuers for the SSO providers that can authenticate this tenant. | [optional] 
**status** | **str** | Whether the tenant is enabled or disabled. | [optional] 
**tenant_code** | **str** | The tenant code of the analytic tenant. For example, \&quot;WFF_j1r~i1o\&quot; | [optional] 
**tenant_display_name** | **str** | An identifiable tenant name that is displayed within Visier. For example, \&quot;Callisto\&quot;. | [optional] 
**vanity_url_name** | **str** | The name of the administrating tenant used in Visier URLs. | [optional] 

## Example

```python
from visier.api.tenant_management.models.tenant_management_api_get_response_dto import TenantManagementAPIGetResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of TenantManagementAPIGetResponseDTO from a JSON string
tenant_management_api_get_response_dto_instance = TenantManagementAPIGetResponseDTO.from_json(json)
# print the JSON string representation of the object
print(TenantManagementAPIGetResponseDTO.to_json())

# convert the object into a dict
tenant_management_api_get_response_dto_dict = tenant_management_api_get_response_dto_instance.to_dict()
# create an instance of TenantManagementAPIGetResponseDTO from a dict
tenant_management_api_get_response_dto_from_dict = TenantManagementAPIGetResponseDTO.from_dict(tenant_management_api_get_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


