# DataVersionExportFileDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | [**List[DataVersionExportColumnDTO]**](DataVersionExportColumnDTO.md) | Information about a table&#39;s columns. | [optional] 
**files** | [**List[DataVersionExportPartFileDTO]**](DataVersionExportPartFileDTO.md) | Information about a table&#39;s files in the export. | [optional] 

## Example

```python
from visier.api.data_version_export.models.data_version_export_file_dto import DataVersionExportFileDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DataVersionExportFileDTO from a JSON string
data_version_export_file_dto_instance = DataVersionExportFileDTO.from_json(json)
# print the JSON string representation of the object
print(DataVersionExportFileDTO.to_json())

# convert the object into a dict
data_version_export_file_dto_dict = data_version_export_file_dto_instance.to_dict()
# create an instance of DataVersionExportFileDTO from a dict
data_version_export_file_dto_from_dict = DataVersionExportFileDTO.from_dict(data_version_export_file_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


