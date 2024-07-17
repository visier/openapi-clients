# AssignedCredentialInfoResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential_id** | **str** | The unique identifier associated with the user. | [optional] 
**display_name** | **str** | The user&#39;s username. This is typically the user&#39;s email, such as john@visier.com. | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from visier.api.data_handling.models.assigned_credential_info_response_dto import AssignedCredentialInfoResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AssignedCredentialInfoResponseDTO from a JSON string
assigned_credential_info_response_dto_instance = AssignedCredentialInfoResponseDTO.from_json(json)
# print the JSON string representation of the object
print(AssignedCredentialInfoResponseDTO.to_json())

# convert the object into a dict
assigned_credential_info_response_dto_dict = assigned_credential_info_response_dto_instance.to_dict()
# create an instance of AssignedCredentialInfoResponseDTO from a dict
assigned_credential_info_response_dto_from_dict = AssignedCredentialInfoResponseDTO.from_dict(assigned_credential_info_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


