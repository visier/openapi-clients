# ProcessingJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_version** | **str** | The data version associated with the processing job. | [optional] 
**job_id** | **str** | The job ID of the processing job for the analytic tenant. | [optional] 
**message** | **str** | A meaningful message about the processing job. | [optional] 
**status** | **str** | The status of the receiving job for the analytic tenant. | [optional] 
**tenant_code** | **str** | The analytic tenant code. | [optional] 

## Example

```python
from visier.api.data_handling.models.processing_job import ProcessingJob

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessingJob from a JSON string
processing_job_instance = ProcessingJob.from_json(json)
# print the JSON string representation of the object
print(ProcessingJob.to_json())

# convert the object into a dict
processing_job_dict = processing_job_instance.to_dict()
# create an instance of ProcessingJob from a dict
processing_job_from_dict = ProcessingJob.from_dict(processing_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


