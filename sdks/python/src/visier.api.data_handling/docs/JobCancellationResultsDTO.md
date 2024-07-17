# JobCancellationResultsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_cancellation_results** | [**List[JobCancellationResultDTO]**](JobCancellationResultDTO.md) | A list of objects representing the job cancellation results. | [optional] 

## Example

```python
from visier.api.data_handling.models.job_cancellation_results_dto import JobCancellationResultsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of JobCancellationResultsDTO from a JSON string
job_cancellation_results_dto_instance = JobCancellationResultsDTO.from_json(json)
# print the JSON string representation of the object
print(JobCancellationResultsDTO.to_json())

# convert the object into a dict
job_cancellation_results_dto_dict = job_cancellation_results_dto_instance.to_dict()
# create an instance of JobCancellationResultsDTO from a dict
job_cancellation_results_dto_from_dict = JobCancellationResultsDTO.from_dict(job_cancellation_results_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


