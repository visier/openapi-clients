# TenantDataUploadsUpdateResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_failures** | **int** | The number of data uploads that failed during the exclusion operation. | [optional] 
**total_success** | **int** | The number of data uploads that were excluded successfully. | [optional] 
**uploads** | [**List[TenantDataUploadUpdateStatusResponseDTO]**](TenantDataUploadUpdateStatusResponseDTO.md) | A list of objects representing the results of the data upload exclusion. | [optional] 

## Example

```python
from visier.api.data_handling.models.tenant_data_uploads_update_response_dto import TenantDataUploadsUpdateResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of TenantDataUploadsUpdateResponseDTO from a JSON string
tenant_data_uploads_update_response_dto_instance = TenantDataUploadsUpdateResponseDTO.from_json(json)
# print the JSON string representation of the object
print(TenantDataUploadsUpdateResponseDTO.to_json())

# convert the object into a dict
tenant_data_uploads_update_response_dto_dict = tenant_data_uploads_update_response_dto_instance.to_dict()
# create an instance of TenantDataUploadsUpdateResponseDTO from a dict
tenant_data_uploads_update_response_dto_from_dict = TenantDataUploadsUpdateResponseDTO.from_dict(tenant_data_uploads_update_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


