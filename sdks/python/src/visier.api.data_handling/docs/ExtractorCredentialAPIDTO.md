# ExtractorCredentialAPIDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_context** | **str** |  | [optional] 
**credential_id** | **str** | The ID associated with the connector credential. | [optional] 
**data_provider** | **str** | The data provider associated with the credential. | [optional] 
**display_name** | **str** | An identifiable connector credential name that is displayed within Visier. | [optional] 
**is_inherited** | **bool** | Whether this credential is inherited from another tenant. | [optional] 

## Example

```python
from visier.api.data_handling.models.extractor_credential_apidto import ExtractorCredentialAPIDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ExtractorCredentialAPIDTO from a JSON string
extractor_credential_apidto_instance = ExtractorCredentialAPIDTO.from_json(json)
# print the JSON string representation of the object
print(ExtractorCredentialAPIDTO.to_json())

# convert the object into a dict
extractor_credential_apidto_dict = extractor_credential_apidto_instance.to_dict()
# create an instance of ExtractorCredentialAPIDTO from a dict
extractor_credential_apidto_from_dict = ExtractorCredentialAPIDTO.from_dict(extractor_credential_apidto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


