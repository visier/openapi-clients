# UpdateTenantModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_properties** | **Dict[str, str]** | A set of key-value pairs that represent different customizable properties for the analytic tenant. | [optional] 
**embeddable_domains** | **List[str]** | A comma-separated list of strings that represent the URLs, or domains, in which Visier can be embedded. If  domains at the administrating tenant level match the domains at the analytic tenant level, you do not need  to include a domain for each analytic tenant. | [optional] 
**industry_code** | **int** | The 6-digit NAICS code for the industry to which the analytic tenant belongs. If the code is unknown, type 000000.   For 2-digit codes, add trailing zeros at the end to reach 6 digits, such as 620000. | [optional] 
**purchased_modules** | **List[str]** | A comma-separated collection of strings that represent the Visier modules assigned to the new analytic tenant. | [optional] 
**sso_instance_issuers** | **List[str]** | A comma-separated list of strings that represent the issuers for the SSO providers that can authenticate this tenant. | [optional] 
**tenant_display_name** | **str** | A display name that is assigned to the new analytic tenant. | [optional] 

## Example

```python
from visier.api.tenant_management.models.update_tenant_model import UpdateTenantModel

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTenantModel from a JSON string
update_tenant_model_instance = UpdateTenantModel.from_json(json)
# print the JSON string representation of the object
print(UpdateTenantModel.to_json())

# convert the object into a dict
update_tenant_model_dict = update_tenant_model_instance.to_dict()
# create an instance of UpdateTenantModel from a dict
update_tenant_model_from_dict = UpdateTenantModel.from_dict(update_tenant_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


