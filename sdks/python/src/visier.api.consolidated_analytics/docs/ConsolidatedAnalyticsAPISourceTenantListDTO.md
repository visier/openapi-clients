# ConsolidatedAnalyticsAPISourceTenantListDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_codes** | **List[str]** | A list of the CA tenant&#39;s source tenants. | [optional] 

## Example

```python
from visier.api.consolidated_analytics.models.consolidated_analytics_api_source_tenant_list_dto import ConsolidatedAnalyticsAPISourceTenantListDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ConsolidatedAnalyticsAPISourceTenantListDTO from a JSON string
consolidated_analytics_api_source_tenant_list_dto_instance = ConsolidatedAnalyticsAPISourceTenantListDTO.from_json(json)
# print the JSON string representation of the object
print(ConsolidatedAnalyticsAPISourceTenantListDTO.to_json())

# convert the object into a dict
consolidated_analytics_api_source_tenant_list_dto_dict = consolidated_analytics_api_source_tenant_list_dto_instance.to_dict()
# create an instance of ConsolidatedAnalyticsAPISourceTenantListDTO from a dict
consolidated_analytics_api_source_tenant_list_dto_from_dict = ConsolidatedAnalyticsAPISourceTenantListDTO.from_dict(consolidated_analytics_api_source_tenant_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


