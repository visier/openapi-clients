# Status

The response structure for errors.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | The status code, which should be an enum value of [google.rpc.Code][google.rpc.Code]. | [optional] 
**message** | **str** | The error message returned by the server. | [optional] 
**details** | [**List[GoogleProtobufAny]**](GoogleProtobufAny.md) | A list of messages that carry the error details.  There is a common set of message types for APIs to use. | [optional] 

## Example

```python
from visier.authentication.models.status import Status

# TODO update the JSON string below
json = "{}"
# create an instance of Status from a JSON string
status_instance = Status.from_json(json)
# print the JSON string representation of the object
print(Status.to_json())

# convert the object into a dict
status_dict = status_instance.to_dict()
# create an instance of Status from a dict
status_from_dict = Status.from_dict(status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


