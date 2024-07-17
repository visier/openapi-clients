# DataVersionExportDataVersionsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_versions** | [**List[DataVersionExportDataVersionSummaryDTO]**](DataVersionExportDataVersionSummaryDTO.md) | All the available data versions for the tenant&#39;s primary data category. | [optional] 

## Example

```python
from visier.api.data_version_export.models.data_version_export_data_versions_dto import DataVersionExportDataVersionsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DataVersionExportDataVersionsDTO from a JSON string
data_version_export_data_versions_dto_instance = DataVersionExportDataVersionsDTO.from_json(json)
# print the JSON string representation of the object
print(DataVersionExportDataVersionsDTO.to_json())

# convert the object into a dict
data_version_export_data_versions_dto_dict = data_version_export_data_versions_dto_instance.to_dict()
# create an instance of DataVersionExportDataVersionsDTO from a dict
data_version_export_data_versions_dto_from_dict = DataVersionExportDataVersionsDTO.from_dict(data_version_export_data_versions_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


