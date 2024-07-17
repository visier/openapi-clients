# TenantDataUploadStatusResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**included** | **bool** | If \&quot;true\&quot;, the data upload is included. | [optional] 
**upload_time** | **str** | The upload time of the data upload. | [optional] 

## Example

```python
from visier.api.data_handling.models.tenant_data_upload_status_response_dto import TenantDataUploadStatusResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of TenantDataUploadStatusResponseDTO from a JSON string
tenant_data_upload_status_response_dto_instance = TenantDataUploadStatusResponseDTO.from_json(json)
# print the JSON string representation of the object
print(TenantDataUploadStatusResponseDTO.to_json())

# convert the object into a dict
tenant_data_upload_status_response_dto_dict = tenant_data_upload_status_response_dto_instance.to_dict()
# create an instance of TenantDataUploadStatusResponseDTO from a dict
tenant_data_upload_status_response_dto_from_dict = TenantDataUploadStatusResponseDTO.from_dict(tenant_data_upload_status_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


