# PushDataCompleteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_receiving_job_id** | **str** | The unique identifier associated with the receiving job. | [optional] 
**data_transfer_result_details** | [**List[DataTransferResultDetail]**](DataTransferResultDetail.md) | A list of objects representing the results of the transfer session. | [optional] 
**message** | **str** | A meaningful message about the transfer session. | [optional] 
**status** | **str** | The status of the transfer session. A completed session returns the status SUCCEED. | [optional] 
**transfer_session_id** | **str** | The unique identifier associated with the transfer session. | [optional] 

## Example

```python
from visier.api.data_intake.models.push_data_complete_response import PushDataCompleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PushDataCompleteResponse from a JSON string
push_data_complete_response_instance = PushDataCompleteResponse.from_json(json)
# print the JSON string representation of the object
print(PushDataCompleteResponse.to_json())

# convert the object into a dict
push_data_complete_response_dict = push_data_complete_response_instance.to_dict()
# create an instance of PushDataCompleteResponse from a dict
push_data_complete_response_from_dict = PushDataCompleteResponse.from_dict(push_data_complete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


