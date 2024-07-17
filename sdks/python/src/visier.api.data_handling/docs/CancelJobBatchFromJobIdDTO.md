# CancelJobBatchFromJobIdDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_ids** | **List[str]** | A list of jobs to cancel. The maximum number of jobs that can be cancelled is 500. | [optional] 

## Example

```python
from visier.api.data_handling.models.cancel_job_batch_from_job_id_dto import CancelJobBatchFromJobIdDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CancelJobBatchFromJobIdDTO from a JSON string
cancel_job_batch_from_job_id_dto_instance = CancelJobBatchFromJobIdDTO.from_json(json)
# print the JSON string representation of the object
print(CancelJobBatchFromJobIdDTO.to_json())

# convert the object into a dict
cancel_job_batch_from_job_id_dto_dict = cancel_job_batch_from_job_id_dto_instance.to_dict()
# create an instance of CancelJobBatchFromJobIdDTO from a dict
cancel_job_batch_from_job_id_dto_from_dict = CancelJobBatchFromJobIdDTO.from_dict(cancel_job_batch_from_job_id_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


