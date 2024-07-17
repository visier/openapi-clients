# AllTenantsStatusAPIDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The limit of analytic tenants to return. The maximum value is 1000. | [optional] 
**start** | **int** | The index to start retrieving values from, also known as offset. The index begins at 0. | [optional] 
**tenants** | [**List[TenantDetailAPIDTO]**](TenantDetailAPIDTO.md) | A list of objects representing all the analytic tenants. | [optional] 

## Example

```python
from visier.api.tenant_management.models.all_tenants_status_apidto import AllTenantsStatusAPIDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AllTenantsStatusAPIDTO from a JSON string
all_tenants_status_apidto_instance = AllTenantsStatusAPIDTO.from_json(json)
# print the JSON string representation of the object
print(AllTenantsStatusAPIDTO.to_json())

# convert the object into a dict
all_tenants_status_apidto_dict = all_tenants_status_apidto_instance.to_dict()
# create an instance of AllTenantsStatusAPIDTO from a dict
all_tenants_status_apidto_from_dict = AllTenantsStatusAPIDTO.from_dict(all_tenants_status_apidto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


