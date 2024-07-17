# TenantDataUploadsResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_code** | **str** | The tenant code of the analytic tenant owning the data uploads. | [optional] 
**uploads** | [**List[TenantDataUploadStatusResponseDTO]**](TenantDataUploadStatusResponseDTO.md) | The data uploads completed for the specified analytic tenant. The list is empty if no previous data uploads are found for the analytic tenant. | [optional] 

## Example

```python
from visier.api.data_handling.models.tenant_data_uploads_response_dto import TenantDataUploadsResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of TenantDataUploadsResponseDTO from a JSON string
tenant_data_uploads_response_dto_instance = TenantDataUploadsResponseDTO.from_json(json)
# print the JSON string representation of the object
print(TenantDataUploadsResponseDTO.to_json())

# convert the object into a dict
tenant_data_uploads_response_dto_dict = tenant_data_uploads_response_dto_instance.to_dict()
# create an instance of TenantDataUploadsResponseDTO from a dict
tenant_data_uploads_response_dto_from_dict = TenantDataUploadsResponseDTO.from_dict(tenant_data_uploads_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


