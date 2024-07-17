# TenantManagementAPIUpdateRequestDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**click_through_link** | **str** | A custom URL to redirect users into your portal to see the relevant content. This URL is used for links that are shared by and with your users through the sharing capability or email content. This is optional. Causes the API request to take longer because it must publish a project to production. | [optional] 
**custom_properties** | [**List[CustomPropertyDTO]**](CustomPropertyDTO.md) | A list of objects that represent different customizable properties for the analytic tenant. This is optional. | [optional] 
**default_currency** | **str** | The default currency to show in the application for the tenant. | [optional] 
**embeddable_domains** | **List[str]** | A comma-separated list of strings that represent the URLs, or domains, in which Visier can be embedded. If domains at the administrating tenant level match the domains at the analytic tenant level, you do not need to include a domain for each analytic tenant. This is optional. | [optional] 
**enabled** | **bool** | If true, the tenant is enabled. Enabled tenants have access to Visier visualizations. | [optional] 
**home_analysis_by_user_group** | [**List[HomeAnalysisByUserGroupDTO]**](HomeAnalysisByUserGroupDTO.md) | A list of objects representing the analysis to display to specific user groups when users log in. This is optional. Causes the API request to take longer because it must publish a project to production. | [optional] 
**home_analysis_id** | **str** | The unique ID of the analysis to display for this tenant when a user logs in. This is optional. Causes the API request to take longer because it must publish a project to production.   Retrieve the ID by opening an analysis in the production version of a tenant and copying the string after the last forward slash (/) in the URL. For example: https://jupiter.visier.com/hr/prod/appcontainer?previewId&#x3D;-eZPm8xvo3SUMpD4Q5pdE-6mCj9CQ9K699XgqRGwtOxagH5x2IzDFawlWn3hYqFEfU7nP0YK9ASEzmrNfAihGg..&amp;previewType&#x3D;Production#/analytics/myanalyses/8a4c1d4f-eb61-4da0-9e5b-55bef757c30e   The &#x60;homeAnalysisID&#x60; is 8a4c1d4f-eb61-4da0-9e5b-55bef757c30e. Alternatively, retrieve the ID by copying the &#x60;contentId&#x60; found by following the &#x60;Embed a visualization&#x60; documentation. | [optional] 
**industry_code** | **int** | The 6-digit NAICS code for the industry to which the analytic tenant belongs. If the code is unknown, type 000000.  For 2-digit codes, add trailing zeros at the end to reach 6 digits, such as 620000. Required if creating new tenants. | [optional] 
**primary_business_location** | [**BusinessLocationDTO**](BusinessLocationDTO.md) | The primary location of operations or where business is performed. This field is optional. | [optional] 
**purchased_modules** | **List[str]** | A comma-separated collection of strings that represent the Visier modules assigned to the new analytic tenant. Required if creating new tenants. | [optional] 
**sso_instance_issuers** | **List[str]** | A comma-separated list of strings that represent the issuers for the SSO providers that can authenticate this tenant. This is optional. | [optional] 
**tenant_code** | **str** | A unique identifier for the newly created analytic tenant. Required if creating new tenants. | [optional] 
**tenant_display_name** | **str** | A new display name to assign to the analytic tenant. Required if creating new tenants. | [optional] 
**tenant_short_name** | **str** | A new short name to assign to the tenant. Required for analytic tenants. | [optional] 
**update_action** | **str** | Specifies the way you want to update values. Default is MERGE.  Valid values:  - &#x60;MERGE&#x60;: Combine the existing values with the new values.  - &#x60;REPLACE&#x60;: Remove existing values and let the new values take their place. | [optional] 
**vanity_url_name** | **str** | A new vanity name to assign to the tenant. Required for analytic tenants. | [optional] 

## Example

```python
from visier.api.tenant_management.models.tenant_management_api_update_request_dto import TenantManagementAPIUpdateRequestDTO

# TODO update the JSON string below
json = "{}"
# create an instance of TenantManagementAPIUpdateRequestDTO from a JSON string
tenant_management_api_update_request_dto_instance = TenantManagementAPIUpdateRequestDTO.from_json(json)
# print the JSON string representation of the object
print(TenantManagementAPIUpdateRequestDTO.to_json())

# convert the object into a dict
tenant_management_api_update_request_dto_dict = tenant_management_api_update_request_dto_instance.to_dict()
# create an instance of TenantManagementAPIUpdateRequestDTO from a dict
tenant_management_api_update_request_dto_from_dict = TenantManagementAPIUpdateRequestDTO.from_dict(tenant_management_api_update_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


