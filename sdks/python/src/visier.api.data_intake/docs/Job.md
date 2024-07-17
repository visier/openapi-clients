# Job


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**receiving_job_id** | **str** | The job ID of the receiving job for the analytic tenant. | [optional] 
**status** | **str** | The status of the receiving job for the analytic tenant. | [optional] 
**tenant_code** | **str** | The analytic tenant code. | [optional] 

## Example

```python
from visier.api.data_intake.models.job import Job

# TODO update the JSON string below
json = "{}"
# create an instance of Job from a JSON string
job_instance = Job.from_json(json)
# print the JSON string representation of the object
print(Job.to_json())

# convert the object into a dict
job_dict = job_instance.to_dict()
# create an instance of Job from a dict
job_from_dict = Job.from_dict(job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


