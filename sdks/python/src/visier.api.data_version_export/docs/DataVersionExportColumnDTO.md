# DataVersionExportColumnDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allows_null** | **bool** | If &#x60;true&#x60;, the column allows null values. | [optional] 
**data_type** | **str** | The column&#39;s data type. Possible data types are string, integer, number, date, Boolean. | [optional] 
**is_primary_key_component** | **bool** | If &#x60;true&#x60;, the column is part of the primary key. | [optional] 
**name** | **str** | The column&#39;s name. | [optional] 

## Example

```python
from visier.api.data_version_export.models.data_version_export_column_dto import DataVersionExportColumnDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DataVersionExportColumnDTO from a JSON string
data_version_export_column_dto_instance = DataVersionExportColumnDTO.from_json(json)
# print the JSON string representation of the object
print(DataVersionExportColumnDTO.to_json())

# convert the object into a dict
data_version_export_column_dto_dict = data_version_export_column_dto_instance.to_dict()
# create an instance of DataVersionExportColumnDTO from a dict
data_version_export_column_dto_from_dict = DataVersionExportColumnDTO.from_dict(data_version_export_column_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


