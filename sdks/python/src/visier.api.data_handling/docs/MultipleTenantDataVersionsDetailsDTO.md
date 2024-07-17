# MultipleTenantDataVersionsDetailsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_versions** | [**List[DataVersionAndDateDTO]**](DataVersionAndDateDTO.md) | The latest enabled data versions for the given analytic tenant. If the analytic tenant  has no enabled data versions, an empty string \&quot;\&quot; is returned. | [optional] 
**tenant_code** | **str** | The owner of the data versions. | [optional] 

## Example

```python
from visier.api.data_handling.models.multiple_tenant_data_versions_details_dto import MultipleTenantDataVersionsDetailsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MultipleTenantDataVersionsDetailsDTO from a JSON string
multiple_tenant_data_versions_details_dto_instance = MultipleTenantDataVersionsDetailsDTO.from_json(json)
# print the JSON string representation of the object
print(MultipleTenantDataVersionsDetailsDTO.to_json())

# convert the object into a dict
multiple_tenant_data_versions_details_dto_dict = multiple_tenant_data_versions_details_dto_instance.to_dict()
# create an instance of MultipleTenantDataVersionsDetailsDTO from a dict
multiple_tenant_data_versions_details_dto_from_dict = MultipleTenantDataVersionsDetailsDTO.from_dict(multiple_tenant_data_versions_details_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


