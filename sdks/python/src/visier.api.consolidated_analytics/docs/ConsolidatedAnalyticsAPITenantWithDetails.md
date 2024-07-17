# ConsolidatedAnalyticsAPITenantWithDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**excluded_sources_list** | **List[str]** | A list of the CA tenant&#39;s excluded sources. | [optional] 
**source_tenants_list** | **List[str]** | A list of the CA tenant&#39;s source tenants. | [optional] 
**tenant_code** | **str** | The CA tenant&#39;s code. | [optional] 

## Example

```python
from visier.api.consolidated_analytics.models.consolidated_analytics_api_tenant_with_details import ConsolidatedAnalyticsAPITenantWithDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ConsolidatedAnalyticsAPITenantWithDetails from a JSON string
consolidated_analytics_api_tenant_with_details_instance = ConsolidatedAnalyticsAPITenantWithDetails.from_json(json)
# print the JSON string representation of the object
print(ConsolidatedAnalyticsAPITenantWithDetails.to_json())

# convert the object into a dict
consolidated_analytics_api_tenant_with_details_dict = consolidated_analytics_api_tenant_with_details_instance.to_dict()
# create an instance of ConsolidatedAnalyticsAPITenantWithDetails from a dict
consolidated_analytics_api_tenant_with_details_from_dict = ConsolidatedAnalyticsAPITenantWithDetails.from_dict(consolidated_analytics_api_tenant_with_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


