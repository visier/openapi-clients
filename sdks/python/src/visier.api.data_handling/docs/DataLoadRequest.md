# DataLoadRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | [**DataLoadRequestModel**](DataLoadRequestModel.md) | A form body key that contains a collection of key-value pairs. | [optional] 

## Example

```python
from visier.api.data_handling.models.data_load_request import DataLoadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DataLoadRequest from a JSON string
data_load_request_instance = DataLoadRequest.from_json(json)
# print the JSON string representation of the object
print(DataLoadRequest.to_json())

# convert the object into a dict
data_load_request_dict = data_load_request_instance.to_dict()
# create an instance of DataLoadRequest from a dict
data_load_request_from_dict = DataLoadRequest.from_dict(data_load_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


