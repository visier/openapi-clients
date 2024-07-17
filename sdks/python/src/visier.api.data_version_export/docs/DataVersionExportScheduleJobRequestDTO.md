# DataVersionExportScheduleJobRequestDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_data_version_number** | **str** | Optional. The baseline data version number to use to generate a delta export.  Delta exports contain the differences between &#x60;baseDataVersionNumber&#x60; and  &#x60;dataVersionNumber&#x60;, such as anything updated, added, or removed in &#x60;dataVersionNumber&#x60;.  If &#x60;baseDataVersionNumber&#x60; is not provided, a full export generates for &#x60;dataVersionNumber&#x60;. | [optional] 
**data_version_number** | **str** | The data version number to generate an export for. | [optional] 

## Example

```python
from visier.api.data_version_export.models.data_version_export_schedule_job_request_dto import DataVersionExportScheduleJobRequestDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DataVersionExportScheduleJobRequestDTO from a JSON string
data_version_export_schedule_job_request_dto_instance = DataVersionExportScheduleJobRequestDTO.from_json(json)
# print the JSON string representation of the object
print(DataVersionExportScheduleJobRequestDTO.to_json())

# convert the object into a dict
data_version_export_schedule_job_request_dto_dict = data_version_export_schedule_job_request_dto_instance.to_dict()
# create an instance of DataVersionExportScheduleJobRequestDTO from a dict
data_version_export_schedule_job_request_dto_from_dict = DataVersionExportScheduleJobRequestDTO.from_dict(data_version_export_schedule_job_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


