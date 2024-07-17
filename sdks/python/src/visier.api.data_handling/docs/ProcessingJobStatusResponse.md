# ProcessingJobStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The limit of processing jobs to retrieve per page. | [optional] 
**parent_job_id** | **str** | The job ID of the receiving job that spawned this job | [optional] 
**parent_tenant_code** | **str** | The tenant code of the receiving job that spawned this job. | [optional] 
**processing_jobs** | [**List[ProcessingJob]**](ProcessingJob.md) | A list of objects representing the processing jobs to retrieve. | [optional] 
**start** | **int** | The index to start retrieving results from, also known as offset. The index begins at 0. | [optional] 

## Example

```python
from visier.api.data_handling.models.processing_job_status_response import ProcessingJobStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessingJobStatusResponse from a JSON string
processing_job_status_response_instance = ProcessingJobStatusResponse.from_json(json)
# print the JSON string representation of the object
print(ProcessingJobStatusResponse.to_json())

# convert the object into a dict
processing_job_status_response_dict = processing_job_status_response_instance.to_dict()
# create an instance of ProcessingJobStatusResponse from a dict
processing_job_status_response_from_dict = ProcessingJobStatusResponse.from_dict(processing_job_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


