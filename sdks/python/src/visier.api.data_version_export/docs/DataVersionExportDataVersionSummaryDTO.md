# DataVersionExportDataVersionSummaryDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **str** | The date that the data version was generated, in milliseconds since 1970-01-01T00:00:00Z. | [optional] 
**data_category** | **str** | The data category that the data version belongs to. If empty, the data version belongs to the default data category. | [optional] 
**data_version** | **str** | The data version number. | [optional] 

## Example

```python
from visier.api.data_version_export.models.data_version_export_data_version_summary_dto import DataVersionExportDataVersionSummaryDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DataVersionExportDataVersionSummaryDTO from a JSON string
data_version_export_data_version_summary_dto_instance = DataVersionExportDataVersionSummaryDTO.from_json(json)
# print the JSON string representation of the object
print(DataVersionExportDataVersionSummaryDTO.to_json())

# convert the object into a dict
data_version_export_data_version_summary_dto_dict = data_version_export_data_version_summary_dto_instance.to_dict()
# create an instance of DataVersionExportDataVersionSummaryDTO from a dict
data_version_export_data_version_summary_dto_from_dict = DataVersionExportDataVersionSummaryDTO.from_dict(data_version_export_data_version_summary_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


