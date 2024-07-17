# DataVersionExportDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_data_version_number** | **str** | The baseline data version number for which the export was generated. If specified, the export is a delta of the differences between &#x60;dateVersionNumber&#x60; and &#x60;baseDataVersionNumber&#x60;. If empty, a full export is generated for &#x60;dataVersionNumber&#x60;. | [optional] 
**data_version_number** | **str** | The data version number for which the export was generated. | [optional] 
**deleted_tables** | **List[str]** | Tables that do not exist in &#x60;dataVersionNumber&#x60; but did exist in &#x60;baseDataVersionNumber&#x60;. | [optional] 
**new_tables** | **List[str]** | Tables that exist in &#x60;dataVersionNumber&#x60; but did not exist in &#x60;baseDataVersionNumber&#x60;. | [optional] 
**tables** | [**List[DataVersionExportTableDTO]**](DataVersionExportTableDTO.md) | Information about the tables in the export. | [optional] 
**timestamp** | **str** | The date that the data version export was generated, in milliseconds since 1970-01-01T00:00:00Z. | [optional] 
**uuid** | **str** | The unique identifier of the data version export. Must be a valid UUID. | [optional] 

## Example

```python
from visier.api.data_version_export.models.data_version_export_dto import DataVersionExportDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DataVersionExportDTO from a JSON string
data_version_export_dto_instance = DataVersionExportDTO.from_json(json)
# print the JSON string representation of the object
print(DataVersionExportDTO.to_json())

# convert the object into a dict
data_version_export_dto_dict = data_version_export_dto_instance.to_dict()
# create an instance of DataVersionExportDTO from a dict
data_version_export_dto_from_dict = DataVersionExportDTO.from_dict(data_version_export_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


