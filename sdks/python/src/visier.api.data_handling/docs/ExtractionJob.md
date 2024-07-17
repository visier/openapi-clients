# ExtractionJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_stage** | **str** | The current stage of the job. This is not returned if the stage is \&quot;Completed\&quot;.  - Valid values: Initialize, Retrieve Main Subject, Retrieve Secondary Subjects, Retrieve Custom Subjects, Process Records, Publish Artifacts, Publish Records, Completed. | [optional] 
**extraction_job_id** | **str** | The ID of the extraction job. | [optional] 
**status** | **str** | The current state of the job.  - Valid values: Pending, Running, Succeeded, Failed, Error, Cancelling, Cancelled, RolledBack, Rescheduling, Rescheduled. | [optional] 
**tenant_code** | **str** | The tenant code of the analytic tenant for the extraction job. | [optional] 

## Example

```python
from visier.api.data_handling.models.extraction_job import ExtractionJob

# TODO update the JSON string below
json = "{}"
# create an instance of ExtractionJob from a JSON string
extraction_job_instance = ExtractionJob.from_json(json)
# print the JSON string representation of the object
print(ExtractionJob.to_json())

# convert the object into a dict
extraction_job_dict = extraction_job_instance.to_dict()
# create an instance of ExtractionJob from a dict
extraction_job_from_dict = ExtractionJob.from_dict(extraction_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


