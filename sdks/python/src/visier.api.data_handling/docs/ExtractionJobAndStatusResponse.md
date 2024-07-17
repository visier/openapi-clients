# ExtractionJobAndStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extraction_jobs** | [**List[ExtractionJob]**](ExtractionJob.md) | A list of extraction job information. | [optional] 
**limit** | **int** | The number of extraction jobs to return. The maximum number of jobs to return is 1000. | [optional] 
**parent_job_id** | **str** | The ID of the dispatching job that generated the extraction jobs. | [optional] 
**parent_tenant_code** | **str** | The tenant that owns the dispatching job. This is usually the administrating tenant. | [optional] 
**start** | **int** | The index to start retrieving results from, also known as offset. The index begins at 0. | [optional] 

## Example

```python
from visier.api.data_handling.models.extraction_job_and_status_response import ExtractionJobAndStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExtractionJobAndStatusResponse from a JSON string
extraction_job_and_status_response_instance = ExtractionJobAndStatusResponse.from_json(json)
# print the JSON string representation of the object
print(ExtractionJobAndStatusResponse.to_json())

# convert the object into a dict
extraction_job_and_status_response_dict = extraction_job_and_status_response_instance.to_dict()
# create an instance of ExtractionJobAndStatusResponse from a dict
extraction_job_and_status_response_from_dict = ExtractionJobAndStatusResponse.from_dict(extraction_job_and_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


