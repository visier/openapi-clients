# ReceivingJobAndStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The number of receiving jobs to return. The maximum number of jobs to return is 1000. | [optional] 
**parent_job_id** | **str** | The ID of the dispatching job that generated the extraction jobs. | [optional] 
**parent_tenant_code** | **str** | The tenant that owns the dispatching job. This is usually the administrating tenant. | [optional] 
**receiving_jobs** | [**List[ReceivingJob]**](ReceivingJob.md) | A list of receiving job information. | [optional] 
**start** | **int** | The index to start retrieving results from, also known as offset. The index begins at 0. | [optional] 

## Example

```python
from visier.api.data_handling.models.receiving_job_and_status_response import ReceivingJobAndStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReceivingJobAndStatusResponse from a JSON string
receiving_job_and_status_response_instance = ReceivingJobAndStatusResponse.from_json(json)
# print the JSON string representation of the object
print(ReceivingJobAndStatusResponse.to_json())

# convert the object into a dict
receiving_job_and_status_response_dict = receiving_job_and_status_response_instance.to_dict()
# create an instance of ReceivingJobAndStatusResponse from a dict
receiving_job_and_status_response_from_dict = ReceivingJobAndStatusResponse.from_dict(receiving_job_and_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


