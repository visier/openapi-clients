# ConsolidatedAnalyticsAPITenantListResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_codes** | **List[str]** | A list of CA tenant codes. | [optional] 

## Example

```python
from visier.api.consolidated_analytics.models.consolidated_analytics_api_tenant_list_response_dto import ConsolidatedAnalyticsAPITenantListResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ConsolidatedAnalyticsAPITenantListResponseDTO from a JSON string
consolidated_analytics_api_tenant_list_response_dto_instance = ConsolidatedAnalyticsAPITenantListResponseDTO.from_json(json)
# print the JSON string representation of the object
print(ConsolidatedAnalyticsAPITenantListResponseDTO.to_json())

# convert the object into a dict
consolidated_analytics_api_tenant_list_response_dto_dict = consolidated_analytics_api_tenant_list_response_dto_instance.to_dict()
# create an instance of ConsolidatedAnalyticsAPITenantListResponseDTO from a dict
consolidated_analytics_api_tenant_list_response_dto_from_dict = ConsolidatedAnalyticsAPITenantListResponseDTO.from_dict(consolidated_analytics_api_tenant_list_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


