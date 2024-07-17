# ReceivingJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**receiving_job_id** | **str** | The job ID of the receiving job for the analytic tenant. | [optional] 
**status** | **str** | The status of the receiving job for the analytic tenant. | [optional] 
**tenant_code** | **str** | The analytic tenant code. | [optional] 

## Example

```python
from visier.api.data_handling.models.receiving_job import ReceivingJob

# TODO update the JSON string below
json = "{}"
# create an instance of ReceivingJob from a JSON string
receiving_job_instance = ReceivingJob.from_json(json)
# print the JSON string representation of the object
print(ReceivingJob.to_json())

# convert the object into a dict
receiving_job_dict = receiving_job_instance.to_dict()
# create an instance of ReceivingJob from a dict
receiving_job_from_dict = ReceivingJob.from_dict(receiving_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


