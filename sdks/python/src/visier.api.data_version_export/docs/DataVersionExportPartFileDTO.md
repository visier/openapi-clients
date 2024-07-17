# DataVersionExportPartFileDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **int** | The unique integer identifier of the file in the data version export. | [optional] 
**filename** | **str** | The file&#39;s name. | [optional] 

## Example

```python
from visier.api.data_version_export.models.data_version_export_part_file_dto import DataVersionExportPartFileDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DataVersionExportPartFileDTO from a JSON string
data_version_export_part_file_dto_instance = DataVersionExportPartFileDTO.from_json(json)
# print the JSON string representation of the object
print(DataVersionExportPartFileDTO.to_json())

# convert the object into a dict
data_version_export_part_file_dto_dict = data_version_export_part_file_dto_instance.to_dict()
# create an instance of DataVersionExportPartFileDTO from a dict
data_version_export_part_file_dto_from_dict = DataVersionExportPartFileDTO.from_dict(data_version_export_part_file_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


