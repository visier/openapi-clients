# TimeShiftDTO

The amount of time to shift the time interval by, such as backward by one year.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | **str** | The direction to extend. Default is BACKWARD. | [optional] 
**period_count** | **int** | The number of intervals. Default is 1. | [optional] 
**period_type** | **str** | The time period type for the shift. | [optional] 

## Example

```python
from visier.model_query_apis.models.time_shift_dto import TimeShiftDTO

# TODO update the JSON string below
json = "{}"
# create an instance of TimeShiftDTO from a JSON string
time_shift_dto_instance = TimeShiftDTO.from_json(json)
# print the JSON string representation of the object
print(TimeShiftDTO.to_json())

# convert the object into a dict
time_shift_dto_dict = time_shift_dto_instance.to_dict()
# create an instance of TimeShiftDTO from a dict
time_shift_dto_from_dict = TimeShiftDTO.from_dict(time_shift_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


