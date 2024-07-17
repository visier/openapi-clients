# DataProviderBasicInformationDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 

## Example

```python
from visier.api.data_handling.models.data_provider_basic_information_dto import DataProviderBasicInformationDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DataProviderBasicInformationDTO from a JSON string
data_provider_basic_information_dto_instance = DataProviderBasicInformationDTO.from_json(json)
# print the JSON string representation of the object
print(DataProviderBasicInformationDTO.to_json())

# convert the object into a dict
data_provider_basic_information_dto_dict = data_provider_basic_information_dto_instance.to_dict()
# create an instance of DataProviderBasicInformationDTO from a dict
data_provider_basic_information_dto_from_dict = DataProviderBasicInformationDTO.from_dict(data_provider_basic_information_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


