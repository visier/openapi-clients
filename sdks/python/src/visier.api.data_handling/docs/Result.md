# Result


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_version** | **str** | If applicable, the data version that was disabled. | [optional] 
**job_id** | **str** | If applicable, the job ID associated with the data version. | [optional] 
**message** | **str** | If applicable, the message explains what errors occurred while disabling data versions. | [optional] 
**status** | **str** | The outcome of the disabling operation. | [optional] 
**tenant_code** | **str** | The analytic tenant that the disable operation was conducted for. | [optional] 

## Example

```python
from visier.api.data_handling.models.result import Result

# TODO update the JSON string below
json = "{}"
# create an instance of Result from a JSON string
result_instance = Result.from_json(json)
# print the JSON string representation of the object
print(Result.to_json())

# convert the object into a dict
result_dict = result_instance.to_dict()
# create an instance of Result from a dict
result_from_dict = Result.from_dict(result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


