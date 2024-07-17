# DataProviderBasicMetadataDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_children_inherit** | **bool** |  | [optional] 

## Example

```python
from visier.api.data_handling.models.data_provider_basic_metadata_dto import DataProviderBasicMetadataDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DataProviderBasicMetadataDTO from a JSON string
data_provider_basic_metadata_dto_instance = DataProviderBasicMetadataDTO.from_json(json)
# print the JSON string representation of the object
print(DataProviderBasicMetadataDTO.to_json())

# convert the object into a dict
data_provider_basic_metadata_dto_dict = data_provider_basic_metadata_dto_instance.to_dict()
# create an instance of DataProviderBasicMetadataDTO from a dict
data_provider_basic_metadata_dto_from_dict = DataProviderBasicMetadataDTO.from_dict(data_provider_basic_metadata_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


