# ConsolidatedAnalyticsAPITenantCreateRequestDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_code** | **str** | The ID of the tenant. For example, WFF_{XXX}~CA{YYY} where {XXX} is the administrating tenant code and {YYY}  is the consolidated analytic tenant code. | [optional] 

## Example

```python
from visier.api.consolidated_analytics.models.consolidated_analytics_api_tenant_create_request_dto import ConsolidatedAnalyticsAPITenantCreateRequestDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ConsolidatedAnalyticsAPITenantCreateRequestDTO from a JSON string
consolidated_analytics_api_tenant_create_request_dto_instance = ConsolidatedAnalyticsAPITenantCreateRequestDTO.from_json(json)
# print the JSON string representation of the object
print(ConsolidatedAnalyticsAPITenantCreateRequestDTO.to_json())

# convert the object into a dict
consolidated_analytics_api_tenant_create_request_dto_dict = consolidated_analytics_api_tenant_create_request_dto_instance.to_dict()
# create an instance of ConsolidatedAnalyticsAPITenantCreateRequestDTO from a dict
consolidated_analytics_api_tenant_create_request_dto_from_dict = ConsolidatedAnalyticsAPITenantCreateRequestDTO.from_dict(consolidated_analytics_api_tenant_create_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


