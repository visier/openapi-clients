# TenantManagementAPIListResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The limit of analytic tenants to return. The maximum value is 1000. The default is 150. | [optional] 
**start** | **int** | The index to start retrieving values from, also known as offset. The index begins at 0. | [optional] 
**tenants** | [**List[TenantManagementAPIGetResponseDTO]**](TenantManagementAPIGetResponseDTO.md) | A list of objects representing all the analytic tenants. | [optional] 

## Example

```python
from visier.api.tenant_management.models.tenant_management_api_list_response_dto import TenantManagementAPIListResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of TenantManagementAPIListResponseDTO from a JSON string
tenant_management_api_list_response_dto_instance = TenantManagementAPIListResponseDTO.from_json(json)
# print the JSON string representation of the object
print(TenantManagementAPIListResponseDTO.to_json())

# convert the object into a dict
tenant_management_api_list_response_dto_dict = tenant_management_api_list_response_dto_instance.to_dict()
# create an instance of TenantManagementAPIListResponseDTO from a dict
tenant_management_api_list_response_dto_from_dict = TenantManagementAPIListResponseDTO.from_dict(tenant_management_api_list_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


