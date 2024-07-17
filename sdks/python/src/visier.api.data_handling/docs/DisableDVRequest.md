# DisableDVRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | [**DisableDVModel**](DisableDVModel.md) | A form body key that contains a collection of key-value pairs. | [optional] 

## Example

```python
from visier.api.data_handling.models.disable_dv_request import DisableDVRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DisableDVRequest from a JSON string
disable_dv_request_instance = DisableDVRequest.from_json(json)
# print the JSON string representation of the object
print(DisableDVRequest.to_json())

# convert the object into a dict
disable_dv_request_dict = disable_dv_request_instance.to_dict()
# create an instance of DisableDVRequest from a dict
disable_dv_request_from_dict = DisableDVRequest.from_dict(disable_dv_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


