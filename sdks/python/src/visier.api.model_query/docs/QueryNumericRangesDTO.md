# QueryNumericRangesDTO

A QueryNumericRanges groups data into specified ranges based on a property value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_all_member** | **bool** | If &#x60;true&#x60;, a member is included that represents all members on the axis. Default is false. | [optional] 
**include_independent_zero_range** | **bool** | If &#x60;true&#x60;, 0 is an independent range. Default is false. | [optional] 
**include_negative** | **bool** | If &#x60;true&#x60;, negative ranges are included. Default is false. | [optional] 
**var_property** | [**QueryPropertyDTO**](QueryPropertyDTO.md) | The name and qualifying path of a numeric property. Non-numeric properties are not accepted. | [optional] 
**ranges** | **str** | The ranges to group data into, expressed as a space-separated string of range-bound values. | [optional] 

## Example

```python
from visier.api.model_query.models.query_numeric_ranges_dto import QueryNumericRangesDTO

# TODO update the JSON string below
json = "{}"
# create an instance of QueryNumericRangesDTO from a JSON string
query_numeric_ranges_dto_instance = QueryNumericRangesDTO.from_json(json)
# print the JSON string representation of the object
print(QueryNumericRangesDTO.to_json())

# convert the object into a dict
query_numeric_ranges_dto_dict = query_numeric_ranges_dto_instance.to_dict()
# create an instance of QueryNumericRangesDTO from a dict
query_numeric_ranges_dto_from_dict = QueryNumericRangesDTO.from_dict(query_numeric_ranges_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


