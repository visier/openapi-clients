# DisableDVResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Result]**](Result.md) | A list of objects representing the disabling process. | [optional] 
**total_failures** | **int** | The number of data versions that failed during the disabling process. | [optional] 
**total_success** | **int** | The number of data versions that were disabled successfully. | [optional] 

## Example

```python
from visier.api.data_handling.models.disable_dv_response import DisableDVResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DisableDVResponse from a JSON string
disable_dv_response_instance = DisableDVResponse.from_json(json)
# print the JSON string representation of the object
print(DisableDVResponse.to_json())

# convert the object into a dict
disable_dv_response_dict = disable_dv_response_instance.to_dict()
# create an instance of DisableDVResponse from a dict
disable_dv_response_from_dict = DisableDVResponse.from_dict(disable_dv_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


