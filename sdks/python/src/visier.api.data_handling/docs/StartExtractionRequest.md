# StartExtractionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | [**StartExtractionModel**](StartExtractionModel.md) | A form body key that contains a collection of key-value pairs. | [optional] 

## Example

```python
from visier.api.data_handling.models.start_extraction_request import StartExtractionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StartExtractionRequest from a JSON string
start_extraction_request_instance = StartExtractionRequest.from_json(json)
# print the JSON string representation of the object
print(StartExtractionRequest.to_json())

# convert the object into a dict
start_extraction_request_dict = start_extraction_request_instance.to_dict()
# create an instance of StartExtractionRequest from a dict
start_extraction_request_from_dict = StartExtractionRequest.from_dict(start_extraction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


