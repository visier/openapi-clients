# AssignConnectorCredentialsResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenants** | [**List[AssignConnectorCredentialsByTenantResponseDTO]**](AssignConnectorCredentialsByTenantResponseDTO.md) | A list of objects representing the tenants and data connectors that were assigned connector credentials. | [optional] 

## Example

```python
from visier.api.data_handling.models.assign_connector_credentials_response_dto import AssignConnectorCredentialsResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AssignConnectorCredentialsResponseDTO from a JSON string
assign_connector_credentials_response_dto_instance = AssignConnectorCredentialsResponseDTO.from_json(json)
# print the JSON string representation of the object
print(AssignConnectorCredentialsResponseDTO.to_json())

# convert the object into a dict
assign_connector_credentials_response_dto_dict = assign_connector_credentials_response_dto_instance.to_dict()
# create an instance of AssignConnectorCredentialsResponseDTO from a dict
assign_connector_credentials_response_dto_from_dict = AssignConnectorCredentialsResponseDTO.from_dict(assign_connector_credentials_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


