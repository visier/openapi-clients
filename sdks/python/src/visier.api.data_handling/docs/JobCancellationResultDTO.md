# JobCancellationResultDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancel_status** | **str** | The status of the cancellation. | [optional] 
**job_id** | **str** | The job ID of the job that the cancel operation was conducted for. | [optional] 
**job_status** | **str** | The job status after the cancel operation. If successful, the status is either Cancelled or Cancelling. | [optional] 
**job_type** | **str** | The job type associated with the job ID. | [optional] 
**message** | **str** | If applicable, the message explains what errors occurred while cancelling the jobs. | [optional] 
**parent_job_id** | **str** | If applicable, the job ID of the job that spawned the given job. | [optional] 
**tenant_code** | **str** | The analytic tenant whose job the cancel operation was conducted for. | [optional] 

## Example

```python
from visier.api.data_handling.models.job_cancellation_result_dto import JobCancellationResultDTO

# TODO update the JSON string below
json = "{}"
# create an instance of JobCancellationResultDTO from a JSON string
job_cancellation_result_dto_instance = JobCancellationResultDTO.from_json(json)
# print the JSON string representation of the object
print(JobCancellationResultDTO.to_json())

# convert the object into a dict
job_cancellation_result_dto_dict = job_cancellation_result_dto_instance.to_dict()
# create an instance of JobCancellationResultDTO from a dict
job_cancellation_result_dto_from_dict = JobCancellationResultDTO.from_dict(job_cancellation_result_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


