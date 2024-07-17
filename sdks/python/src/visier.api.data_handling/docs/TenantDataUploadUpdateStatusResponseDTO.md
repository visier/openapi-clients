# TenantDataUploadUpdateStatusResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | If applicable, the message explains why errors were encountered during the exclusion operation. | [optional] 
**status** | **str** | The outcome of the exclusion operation. | [optional] 
**tenant_code** | **str** | The analytic tenant that the exclusion operation was conducted for. | [optional] 
**upload_time** | **str** | The upload time of the data upload | [optional] 

## Example

```python
from visier.api.data_handling.models.tenant_data_upload_update_status_response_dto import TenantDataUploadUpdateStatusResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of TenantDataUploadUpdateStatusResponseDTO from a JSON string
tenant_data_upload_update_status_response_dto_instance = TenantDataUploadUpdateStatusResponseDTO.from_json(json)
# print the JSON string representation of the object
print(TenantDataUploadUpdateStatusResponseDTO.to_json())

# convert the object into a dict
tenant_data_upload_update_status_response_dto_dict = tenant_data_upload_update_status_response_dto_instance.to_dict()
# create an instance of TenantDataUploadUpdateStatusResponseDTO from a dict
tenant_data_upload_update_status_response_dto_from_dict = TenantDataUploadUpdateStatusResponseDTO.from_dict(tenant_data_upload_update_status_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


