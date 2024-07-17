# ProcessingJobAndStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The number of processing jobs to return. The maximum number of jobs to return is 1000. | [optional] 
**parent_job_id** | **str** | The ID of the dispatching job that generated the extraction jobs. | [optional] 
**parent_tenant_code** | **str** | The tenant that owns the dispatching job. This is usually the administrating tenant. | [optional] 
**processing_jobs** | [**List[ProcessingJob]**](ProcessingJob.md) | A list of processing job information. | [optional] 
**start** | **int** | The index to start retrieving results from, also known as offset. The index begins at 0. | [optional] 

## Example

```python
from visier.api.data_handling.models.processing_job_and_status_response import ProcessingJobAndStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessingJobAndStatusResponse from a JSON string
processing_job_and_status_response_instance = ProcessingJobAndStatusResponse.from_json(json)
# print the JSON string representation of the object
print(ProcessingJobAndStatusResponse.to_json())

# convert the object into a dict
processing_job_and_status_response_dict = processing_job_and_status_response_instance.to_dict()
# create an instance of ProcessingJobAndStatusResponse from a dict
processing_job_and_status_response_from_dict = ProcessingJobAndStatusResponse.from_dict(processing_job_and_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


