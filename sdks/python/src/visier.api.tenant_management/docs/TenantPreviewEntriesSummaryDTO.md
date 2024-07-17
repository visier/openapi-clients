# TenantPreviewEntriesSummaryDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_version** | **str** | The data version ID. | [optional] 
**data_version_date** | **str** | The date that the data version was created. | [optional] 
**metrics** | [**List[MetricValidationSummaryDTO]**](MetricValidationSummaryDTO.md) | A list of metrics and their values. | [optional] 
**tenant_code** | **str** | The tenant code of the analytic tenant. For example, \&quot;WFF_j1r~i1o\&quot;. | [optional] 

## Example

```python
from visier.api.tenant_management.models.tenant_preview_entries_summary_dto import TenantPreviewEntriesSummaryDTO

# TODO update the JSON string below
json = "{}"
# create an instance of TenantPreviewEntriesSummaryDTO from a JSON string
tenant_preview_entries_summary_dto_instance = TenantPreviewEntriesSummaryDTO.from_json(json)
# print the JSON string representation of the object
print(TenantPreviewEntriesSummaryDTO.to_json())

# convert the object into a dict
tenant_preview_entries_summary_dto_dict = tenant_preview_entries_summary_dto_instance.to_dict()
# create an instance of TenantPreviewEntriesSummaryDTO from a dict
tenant_preview_entries_summary_dto_from_dict = TenantPreviewEntriesSummaryDTO.from_dict(tenant_preview_entries_summary_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


