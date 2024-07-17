# TenantPreviewEntriesSummaryListDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The number of analytic tenants to retrieve. The maximum number to retrieve is 1000. | [optional] 
**start** | **int** | The index to start retrieving results from, also known as offset. The index begins at 0. | [optional] 
**tenants** | [**List[TenantPreviewEntriesSummaryDTO]**](TenantPreviewEntriesSummaryDTO.md) | A list of objects representing all the analytic tenants. | [optional] 

## Example

```python
from visier.api.tenant_management.models.tenant_preview_entries_summary_list_dto import TenantPreviewEntriesSummaryListDTO

# TODO update the JSON string below
json = "{}"
# create an instance of TenantPreviewEntriesSummaryListDTO from a JSON string
tenant_preview_entries_summary_list_dto_instance = TenantPreviewEntriesSummaryListDTO.from_json(json)
# print the JSON string representation of the object
print(TenantPreviewEntriesSummaryListDTO.to_json())

# convert the object into a dict
tenant_preview_entries_summary_list_dto_dict = tenant_preview_entries_summary_list_dto_instance.to_dict()
# create an instance of TenantPreviewEntriesSummaryListDTO from a dict
tenant_preview_entries_summary_list_dto_from_dict = TenantPreviewEntriesSummaryListDTO.from_dict(tenant_preview_entries_summary_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


