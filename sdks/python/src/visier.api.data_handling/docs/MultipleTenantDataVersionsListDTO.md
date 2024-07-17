# MultipleTenantDataVersionsListDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The number of analytic tenants to retrieve. The maximum number to retrieve is 1000. | [optional] 
**start** | **int** | The index to start retrieving results from, also known as offset. The index begins at 0. | [optional] 
**tenants** | [**List[MultipleTenantDataVersionsDetailsDTO]**](MultipleTenantDataVersionsDetailsDTO.md) | A list of analytic tenants and their latest enabled data versions. | [optional] 

## Example

```python
from visier.api.data_handling.models.multiple_tenant_data_versions_list_dto import MultipleTenantDataVersionsListDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MultipleTenantDataVersionsListDTO from a JSON string
multiple_tenant_data_versions_list_dto_instance = MultipleTenantDataVersionsListDTO.from_json(json)
# print the JSON string representation of the object
print(MultipleTenantDataVersionsListDTO.to_json())

# convert the object into a dict
multiple_tenant_data_versions_list_dto_dict = multiple_tenant_data_versions_list_dto_instance.to_dict()
# create an instance of MultipleTenantDataVersionsListDTO from a dict
multiple_tenant_data_versions_list_dto_from_dict = MultipleTenantDataVersionsListDTO.from_dict(multiple_tenant_data_versions_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


