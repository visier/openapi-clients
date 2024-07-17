# TenantCodeBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_codes** | **List[str]** | A list of a CA tenant&#39;s source tenants codes. The maximum length is 1000. | [optional] 

## Example

```python
from visier.api.consolidated_analytics.models.tenant_code_body import TenantCodeBody

# TODO update the JSON string below
json = "{}"
# create an instance of TenantCodeBody from a JSON string
tenant_code_body_instance = TenantCodeBody.from_json(json)
# print the JSON string representation of the object
print(TenantCodeBody.to_json())

# convert the object into a dict
tenant_code_body_dict = tenant_code_body_instance.to_dict()
# create an instance of TenantCodeBody from a dict
tenant_code_body_from_dict = TenantCodeBody.from_dict(tenant_code_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


