# ReceivingJobStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | The unique identifier associated with the receiving job. | [optional] 
**parent_job_id** | **str** | The job ID of the receiving job that spawned this job. | [optional] 
**parent_tenant_code** | **str** | The tenant code of the receiving job that spawned this job. | [optional] 
**receiving_jobs** | [**List[ReceivingJob]**](ReceivingJob.md) | A list of objects representing the receiving jobs to retrieve. | [optional] 
**status** | **str** | The status of the receiving job. | [optional] 

## Example

```python
from visier.api.data_handling.models.receiving_job_status_response import ReceivingJobStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReceivingJobStatusResponse from a JSON string
receiving_job_status_response_instance = ReceivingJobStatusResponse.from_json(json)
# print the JSON string representation of the object
print(ReceivingJobStatusResponse.to_json())

# convert the object into a dict
receiving_job_status_response_dict = receiving_job_status_response_instance.to_dict()
# create an instance of ReceivingJobStatusResponse from a dict
receiving_job_status_response_from_dict = ReceivingJobStatusResponse.from_dict(receiving_job_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


