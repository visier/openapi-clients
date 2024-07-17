# TenantAndCredential


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential_id** | **str** | The unique identifier associated with the credential. | [optional] 
**tenant_code** | **str** | The unique identifier associated with the tenant. | [optional] 

## Example

```python
from visier.api.data_handling.models.tenant_and_credential import TenantAndCredential

# TODO update the JSON string below
json = "{}"
# create an instance of TenantAndCredential from a JSON string
tenant_and_credential_instance = TenantAndCredential.from_json(json)
# print the JSON string representation of the object
print(TenantAndCredential.to_json())

# convert the object into a dict
tenant_and_credential_dict = tenant_and_credential_instance.to_dict()
# create an instance of TenantAndCredential from a dict
tenant_and_credential_from_dict = TenantAndCredential.from_dict(tenant_and_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


