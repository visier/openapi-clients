# DataVersionExportScheduleJobResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_uuid** | **str** | The unique identifier of the scheduled data version export job. | [optional] 

## Example

```python
from visier.api.data_version_export.models.data_version_export_schedule_job_response_dto import DataVersionExportScheduleJobResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DataVersionExportScheduleJobResponseDTO from a JSON string
data_version_export_schedule_job_response_dto_instance = DataVersionExportScheduleJobResponseDTO.from_json(json)
# print the JSON string representation of the object
print(DataVersionExportScheduleJobResponseDTO.to_json())

# convert the object into a dict
data_version_export_schedule_job_response_dto_dict = data_version_export_schedule_job_response_dto_instance.to_dict()
# create an instance of DataVersionExportScheduleJobResponseDTO from a dict
data_version_export_schedule_job_response_dto_from_dict = DataVersionExportScheduleJobResponseDTO.from_dict(data_version_export_schedule_job_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


