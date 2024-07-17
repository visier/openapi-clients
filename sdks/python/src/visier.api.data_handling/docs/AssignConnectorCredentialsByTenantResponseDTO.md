# AssignConnectorCredentialsByTenantResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connectors** | [**List[AssignConnectorWithCredentialsResponseDTO]**](AssignConnectorWithCredentialsResponseDTO.md) | A list of objects representing the assigned credentials and connectors. | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** | The state of the credential assignment. Valid values are Succeed or Failed. | [optional] 
**tenant_code** | **str** | The unique identifier associated with the tenant. | [optional] 

## Example

```python
from visier.api.data_handling.models.assign_connector_credentials_by_tenant_response_dto import AssignConnectorCredentialsByTenantResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AssignConnectorCredentialsByTenantResponseDTO from a JSON string
assign_connector_credentials_by_tenant_response_dto_instance = AssignConnectorCredentialsByTenantResponseDTO.from_json(json)
# print the JSON string representation of the object
print(AssignConnectorCredentialsByTenantResponseDTO.to_json())

# convert the object into a dict
assign_connector_credentials_by_tenant_response_dto_dict = assign_connector_credentials_by_tenant_response_dto_instance.to_dict()
# create an instance of AssignConnectorCredentialsByTenantResponseDTO from a dict
assign_connector_credentials_by_tenant_response_dto_from_dict = AssignConnectorCredentialsByTenantResponseDTO.from_dict(assign_connector_credentials_by_tenant_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


