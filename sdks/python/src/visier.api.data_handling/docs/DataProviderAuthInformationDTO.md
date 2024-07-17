# DataProviderAuthInformationDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_provider_auth_params** | [**DataProviderAuthParamsDTO**](DataProviderAuthParamsDTO.md) | The authentication information for the credential. | [optional] 
**data_provider_basic_information** | [**DataProviderBasicInformationDTO**](DataProviderBasicInformationDTO.md) | The display name and description for the credential. | [optional] 
**data_provider_metadata** | [**DataProviderBasicMetadataDTO**](DataProviderBasicMetadataDTO.md) |  | [optional] 

## Example

```python
from visier.api.data_handling.models.data_provider_auth_information_dto import DataProviderAuthInformationDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DataProviderAuthInformationDTO from a JSON string
data_provider_auth_information_dto_instance = DataProviderAuthInformationDTO.from_json(json)
# print the JSON string representation of the object
print(DataProviderAuthInformationDTO.to_json())

# convert the object into a dict
data_provider_auth_information_dto_dict = data_provider_auth_information_dto_instance.to_dict()
# create an instance of DataProviderAuthInformationDTO from a dict
data_provider_auth_information_dto_from_dict = DataProviderAuthInformationDTO.from_dict(data_provider_auth_information_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


