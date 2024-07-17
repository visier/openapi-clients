# TenantDataUploadsListResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The number of analytic tenants to retrieve. The maximum number of analytic tenants to retrieve is 1000. | [optional] 
**start** | **int** | The index to start retrieving results from, also known as offset. The index begins at 0. | [optional] 
**tenants** | [**List[TenantDataUploadsResponseDTO]**](TenantDataUploadsResponseDTO.md) | A list of objects representing analytic tenants and their data uploads. | [optional] 

## Example

```python
from visier.api.data_handling.models.tenant_data_uploads_list_response_dto import TenantDataUploadsListResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of TenantDataUploadsListResponseDTO from a JSON string
tenant_data_uploads_list_response_dto_instance = TenantDataUploadsListResponseDTO.from_json(json)
# print the JSON string representation of the object
print(TenantDataUploadsListResponseDTO.to_json())

# convert the object into a dict
tenant_data_uploads_list_response_dto_dict = tenant_data_uploads_list_response_dto_instance.to_dict()
# create an instance of TenantDataUploadsListResponseDTO from a dict
tenant_data_uploads_list_response_dto_from_dict = TenantDataUploadsListResponseDTO.from_dict(tenant_data_uploads_list_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


