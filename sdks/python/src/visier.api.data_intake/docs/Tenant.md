# Tenant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sources** | [**List[Source]**](Source.md) | A list of objects representing the sources that data was pushed to and their data transfer results. | [optional] 
**status** | **str** | The status of the data transfer for this tenant. | [optional] 
**tenant_code** | **str** | The code of the tenant that data was transferred to. For example, WFF_j1r or WFF_j1r~c7o. | [optional] 

## Example

```python
from visier.api.data_intake.models.tenant import Tenant

# TODO update the JSON string below
json = "{}"
# create an instance of Tenant from a JSON string
tenant_instance = Tenant.from_json(json)
# print the JSON string representation of the object
print(Tenant.to_json())

# convert the object into a dict
tenant_dict = tenant_instance.to_dict()
# create an instance of Tenant from a dict
tenant_from_dict = Tenant.from_dict(tenant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


