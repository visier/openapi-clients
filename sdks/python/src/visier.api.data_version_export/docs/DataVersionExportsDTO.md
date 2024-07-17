# DataVersionExportsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_version_exports** | [**List[DataVersionExportDTO]**](DataVersionExportDTO.md) | Information about data version exports. | [optional] 

## Example

```python
from visier.api.data_version_export.models.data_version_exports_dto import DataVersionExportsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DataVersionExportsDTO from a JSON string
data_version_exports_dto_instance = DataVersionExportsDTO.from_json(json)
# print the JSON string representation of the object
print(DataVersionExportsDTO.to_json())

# convert the object into a dict
data_version_exports_dto_dict = data_version_exports_dto_instance.to_dict()
# create an instance of DataVersionExportsDTO from a dict
data_version_exports_dto_from_dict = DataVersionExportsDTO.from_dict(data_version_exports_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


