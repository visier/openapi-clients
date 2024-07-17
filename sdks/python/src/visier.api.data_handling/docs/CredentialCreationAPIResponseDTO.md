# CredentialCreationAPIResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**missing_connection_properties** | [**List[SubjectMissingAccessDTO]**](SubjectMissingAccessDTO.md) | The properties that the credential cannot access despite successful authentication.  This is only returned for authentications that do not grant access to all data. | [optional] 
**object_name** | **str** | The object name of the newly created credential. | [optional] 
**symbol_name** | **str** | The symbol name of the newly created credential. | [optional] 
**uuid** | **str** | The unique ID of the newly created credential. | [optional] 

## Example

```python
from visier.api.data_handling.models.credential_creation_api_response_dto import CredentialCreationAPIResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialCreationAPIResponseDTO from a JSON string
credential_creation_api_response_dto_instance = CredentialCreationAPIResponseDTO.from_json(json)
# print the JSON string representation of the object
print(CredentialCreationAPIResponseDTO.to_json())

# convert the object into a dict
credential_creation_api_response_dto_dict = credential_creation_api_response_dto_instance.to_dict()
# create an instance of CredentialCreationAPIResponseDTO from a dict
credential_creation_api_response_dto_from_dict = CredentialCreationAPIResponseDTO.from_dict(credential_creation_api_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


