# PushDataCancelResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_transfer_result_details** | [**List[DataTransferResultDetail]**](DataTransferResultDetail.md) | A list of objects representing the results of the transfer session. | [optional] 
**message** | **str** | A meaningful message about the transfer session. | [optional] 
**status** | **str** | The status of the transfer session. A cancelled session returns the status CANCELLED. | [optional] 
**transfer_session_id** | **str** | The unique identifier associated with the transfer session. | [optional] 

## Example

```python
from visier.api.data_intake.models.push_data_cancel_response import PushDataCancelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PushDataCancelResponse from a JSON string
push_data_cancel_response_instance = PushDataCancelResponse.from_json(json)
# print the JSON string representation of the object
print(PushDataCancelResponse.to_json())

# convert the object into a dict
push_data_cancel_response_dict = push_data_cancel_response_instance.to_dict()
# create an instance of PushDataCancelResponse from a dict
push_data_cancel_response_from_dict = PushDataCancelResponse.from_dict(push_data_cancel_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


