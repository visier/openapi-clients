# DirectDataJobStatusResponseDTO

The job status information for a committed transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | The unique identifier of the processing job. | [optional] 
**message** | **str** | If the processing job fails, this field contains details specific to the failure. | [optional] 
**status** | **str** | The status of the processing job. | [optional] 
**tenant_code** | **str** | The tenant for the data load. | [optional] 
**transaction_id** | **str** | The unique identifier of the committed transaction. | [optional] 

## Example

```python
from visier.api.direct_data_intake.models.direct_data_job_status_response_dto import DirectDataJobStatusResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DirectDataJobStatusResponseDTO from a JSON string
direct_data_job_status_response_dto_instance = DirectDataJobStatusResponseDTO.from_json(json)
# print the JSON string representation of the object
print(DirectDataJobStatusResponseDTO.to_json())

# convert the object into a dict
direct_data_job_status_response_dto_dict = direct_data_job_status_response_dto_instance.to_dict()
# create an instance of DirectDataJobStatusResponseDTO from a dict
direct_data_job_status_response_dto_from_dict = DirectDataJobStatusResponseDTO.from_dict(direct_data_job_status_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


