# ConsolidatedAnalyticsAPITenantWithDetailsListResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenants** | [**List[ConsolidatedAnalyticsAPITenantWithDetails]**](ConsolidatedAnalyticsAPITenantWithDetails.md) | A list of CA tenants and their details. | [optional] 

## Example

```python
from visier.api.consolidated_analytics.models.consolidated_analytics_api_tenant_with_details_list_response_dto import ConsolidatedAnalyticsAPITenantWithDetailsListResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ConsolidatedAnalyticsAPITenantWithDetailsListResponseDTO from a JSON string
consolidated_analytics_api_tenant_with_details_list_response_dto_instance = ConsolidatedAnalyticsAPITenantWithDetailsListResponseDTO.from_json(json)
# print the JSON string representation of the object
print(ConsolidatedAnalyticsAPITenantWithDetailsListResponseDTO.to_json())

# convert the object into a dict
consolidated_analytics_api_tenant_with_details_list_response_dto_dict = consolidated_analytics_api_tenant_with_details_list_response_dto_instance.to_dict()
# create an instance of ConsolidatedAnalyticsAPITenantWithDetailsListResponseDTO from a dict
consolidated_analytics_api_tenant_with_details_list_response_dto_from_dict = ConsolidatedAnalyticsAPITenantWithDetailsListResponseDTO.from_dict(consolidated_analytics_api_tenant_with_details_list_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


