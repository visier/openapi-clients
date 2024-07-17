# PushDataCompleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**processing_data** | **bool** | If true, a processing job will be triggered after the receiving job successfully completes. This generates a new data version. | [optional] 
**transfer_session_id** | **str** | The unique identifier associated with the transfer session. | [optional] 

## Example

```python
from visier.api.data_intake.models.push_data_complete_request import PushDataCompleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PushDataCompleteRequest from a JSON string
push_data_complete_request_instance = PushDataCompleteRequest.from_json(json)
# print the JSON string representation of the object
print(PushDataCompleteRequest.to_json())

# convert the object into a dict
push_data_complete_request_dict = push_data_complete_request_instance.to_dict()
# create an instance of PushDataCompleteRequest from a dict
push_data_complete_request_from_dict = PushDataCompleteRequest.from_dict(push_data_complete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


