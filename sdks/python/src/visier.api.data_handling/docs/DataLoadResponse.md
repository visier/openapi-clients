# DataLoadResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | The unique identifier associated with the receiving job. | [optional] 

## Example

```python
from visier.api.data_handling.models.data_load_response import DataLoadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DataLoadResponse from a JSON string
data_load_response_instance = DataLoadResponse.from_json(json)
# print the JSON string representation of the object
print(DataLoadResponse.to_json())

# convert the object into a dict
data_load_response_dict = data_load_response_instance.to_dict()
# create an instance of DataLoadResponse from a dict
data_load_response_from_dict = DataLoadResponse.from_dict(data_load_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


