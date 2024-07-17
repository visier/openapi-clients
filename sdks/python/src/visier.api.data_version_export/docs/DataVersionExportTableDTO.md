# DataVersionExportTableDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_columns** | [**DataVersionExportFileDTO**](DataVersionExportFileDTO.md) | Information about the columns and files that are in both &#x60;dataVersionNumber&#x60; and &#x60;baseDataVersionNumber&#x60;. Always empty for full exports where &#x60;baseDataVersionNumber&#x60; is not specified. | [optional] 
**deleted_columns** | **List[str]** | Information about columns that do not exist in &#x60;dataVersionNumber&#x60; but did exist in &#x60;baseDataVersionNumber&#x60;. | [optional] 
**name** | **str** | The name of a table in the data version export; for example, Employee or Applicant. | [optional] 
**new_columns** | [**DataVersionExportFileDTO**](DataVersionExportFileDTO.md) | Information about new columns and files in the data version.  If full export, lists all columns. If delta export, lists columns that exist in &#x60;dataVersionNumber&#x60; but not in &#x60;baseDataVersionNumber&#x60;. | [optional] 

## Example

```python
from visier.api.data_version_export.models.data_version_export_table_dto import DataVersionExportTableDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DataVersionExportTableDTO from a JSON string
data_version_export_table_dto_instance = DataVersionExportTableDTO.from_json(json)
# print the JSON string representation of the object
print(DataVersionExportTableDTO.to_json())

# convert the object into a dict
data_version_export_table_dto_dict = data_version_export_table_dto_instance.to_dict()
# create an instance of DataVersionExportTableDTO from a dict
data_version_export_table_dto_from_dict = DataVersionExportTableDTO.from_dict(data_version_export_table_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


