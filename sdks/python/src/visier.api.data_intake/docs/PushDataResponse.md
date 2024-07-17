# PushDataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Any additional information about the data transfer. | [optional] 
**sequence** | **int** | The unique sequence number associated with a batch of records. | [optional] 
**status** | **str** | The status of the data transfer. | [optional] 
**tenants** | [**List[Tenant]**](Tenant.md) | A list of strings representing the tenants that data was pushed to and their data transfer results. | [optional] 
**transfer_session_id** | **str** | The unique identifier associated with the transfer session. | [optional] 

## Example

```python
from visier.api.data_intake.models.push_data_response import PushDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PushDataResponse from a JSON string
push_data_response_instance = PushDataResponse.from_json(json)
# print the JSON string representation of the object
print(PushDataResponse.to_json())

# convert the object into a dict
push_data_response_dict = push_data_response_instance.to_dict()
# create an instance of PushDataResponse from a dict
push_data_response_from_dict = PushDataResponse.from_dict(push_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


