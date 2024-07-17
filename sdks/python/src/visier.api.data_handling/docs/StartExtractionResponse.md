# StartExtractionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | The ID of the dispatching job that generated the extraction jobs. | [optional] 

## Example

```python
from visier.api.data_handling.models.start_extraction_response import StartExtractionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StartExtractionResponse from a JSON string
start_extraction_response_instance = StartExtractionResponse.from_json(json)
# print the JSON string representation of the object
print(StartExtractionResponse.to_json())

# convert the object into a dict
start_extraction_response_dict = start_extraction_response_instance.to_dict()
# create an instance of StartExtractionResponse from a dict
start_extraction_response_from_dict = StartExtractionResponse.from_dict(start_extraction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


