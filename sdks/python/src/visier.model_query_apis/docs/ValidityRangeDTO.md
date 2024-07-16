# ValidityRangeDTO

A pair of values that represent the time interval to which the data is valid.  The validity range is defined in Unix epoch format and UTC timezone.  Note: Epochs are expressed as 64-bit integers and represented as stringified longs in JSON due to JSON's inherent  limitation in representing large numbers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | **str** | The date from which data is no longer available.  Note: Format is the number of milliseconds since midnight 01 January, 1970 UTC as a string. | [optional] 
**start** | **str** | The date from which data becomes available.  Note: Format is the number of milliseconds since midnight 01 January, 1970 UTC as a string. | [optional] 

## Example

```python
from visier.model_query_apis.models.validity_range_dto import ValidityRangeDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ValidityRangeDTO from a JSON string
validity_range_dto_instance = ValidityRangeDTO.from_json(json)
# print the JSON string representation of the object
print(ValidityRangeDTO.to_json())

# convert the object into a dict
validity_range_dto_dict = validity_range_dto_instance.to_dict()
# create an instance of ValidityRangeDTO from a dict
validity_range_dto_from_dict = ValidityRangeDTO.from_dict(validity_range_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


