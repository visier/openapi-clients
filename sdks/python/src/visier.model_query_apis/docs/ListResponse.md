# ListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header** | [**GoogleProtobufAny**](GoogleProtobufAny.md) |  | [optional] 
**rows** | [**List[GoogleProtobufAny]**](GoogleProtobufAny.md) |  | [optional] 

## Example

```python
from visier.model_query_apis.models.list_response import ListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListResponse from a JSON string
list_response_instance = ListResponse.from_json(json)
# print the JSON string representation of the object
print(ListResponse.to_json())

# convert the object into a dict
list_response_dict = list_response_instance.to_dict()
# create an instance of ListResponse from a dict
list_response_from_dict = ListResponse.from_dict(list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


