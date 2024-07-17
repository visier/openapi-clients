# ExtractorCredentialsAPIDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_credentials** | [**List[ExtractorCredentialAPIDTO]**](ExtractorCredentialAPIDTO.md) | A list of objects representing all the available connector credentials in Production. | [optional] 
**limit** | **int** | The number of connector credentials to return. The maximum number of data connector credentials to return is 1000. | [optional] 
**start** | **int** | The index to start retrieving values from, also known as offset. The index begins at 0. | [optional] 

## Example

```python
from visier.api.data_handling.models.extractor_credentials_apidto import ExtractorCredentialsAPIDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ExtractorCredentialsAPIDTO from a JSON string
extractor_credentials_apidto_instance = ExtractorCredentialsAPIDTO.from_json(json)
# print the JSON string representation of the object
print(ExtractorCredentialsAPIDTO.to_json())

# convert the object into a dict
extractor_credentials_apidto_dict = extractor_credentials_apidto_instance.to_dict()
# create an instance of ExtractorCredentialsAPIDTO from a dict
extractor_credentials_apidto_from_dict = ExtractorCredentialsAPIDTO.from_dict(extractor_credentials_apidto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


