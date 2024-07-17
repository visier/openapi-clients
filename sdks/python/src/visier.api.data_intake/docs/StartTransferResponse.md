# StartTransferResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transfer_session_id** | **str** | The unique identifier associated with the transfer session. | [optional] 

## Example

```python
from visier.api.data_intake.models.start_transfer_response import StartTransferResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StartTransferResponse from a JSON string
start_transfer_response_instance = StartTransferResponse.from_json(json)
# print the JSON string representation of the object
print(StartTransferResponse.to_json())

# convert the object into a dict
start_transfer_response_dict = start_transfer_response_instance.to_dict()
# create an instance of StartTransferResponse from a dict
start_transfer_response_from_dict = StartTransferResponse.from_dict(start_transfer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


