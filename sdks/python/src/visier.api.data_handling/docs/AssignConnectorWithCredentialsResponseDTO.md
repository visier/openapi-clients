# AssignConnectorWithCredentialsResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector** | [**ConnectorInfoResponseDTO**](ConnectorInfoResponseDTO.md) | The data connector that was assigned a connector credential. | [optional] 
**credential** | [**AssignedCredentialInfoResponseDTO**](AssignedCredentialInfoResponseDTO.md) | A connector credential that was assigned to a data connector | [optional] 

## Example

```python
from visier.api.data_handling.models.assign_connector_with_credentials_response_dto import AssignConnectorWithCredentialsResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AssignConnectorWithCredentialsResponseDTO from a JSON string
assign_connector_with_credentials_response_dto_instance = AssignConnectorWithCredentialsResponseDTO.from_json(json)
# print the JSON string representation of the object
print(AssignConnectorWithCredentialsResponseDTO.to_json())

# convert the object into a dict
assign_connector_with_credentials_response_dto_dict = assign_connector_with_credentials_response_dto_instance.to_dict()
# create an instance of AssignConnectorWithCredentialsResponseDTO from a dict
assign_connector_with_credentials_response_dto_from_dict = AssignConnectorWithCredentialsResponseDTO.from_dict(assign_connector_with_credentials_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


