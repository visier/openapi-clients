# AssignConnectorCredentialRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connectors** | [**List[Connector]**](Connector.md) | A list of objects representing the data connectors to be assigned with credentials. | [optional] 

## Example

```python
from visier.api.data_handling.models.assign_connector_credential_request import AssignConnectorCredentialRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssignConnectorCredentialRequest from a JSON string
assign_connector_credential_request_instance = AssignConnectorCredentialRequest.from_json(json)
# print the JSON string representation of the object
print(AssignConnectorCredentialRequest.to_json())

# convert the object into a dict
assign_connector_credential_request_dict = assign_connector_credential_request_instance.to_dict()
# create an instance of AssignConnectorCredentialRequest from a dict
assign_connector_credential_request_from_dict = AssignConnectorCredentialRequest.from_dict(assign_connector_credential_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


