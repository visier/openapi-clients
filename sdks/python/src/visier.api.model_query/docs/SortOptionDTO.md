# SortOptionDTO

Sort option for a column of a list query.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_index** | **int** | The index of the column of the list query, staring from 0. | [optional] 
**sort_direction** | **str** | The sort direction. | [optional] 

## Example

```python
from visier.api.model_query.models.sort_option_dto import SortOptionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SortOptionDTO from a JSON string
sort_option_dto_instance = SortOptionDTO.from_json(json)
# print the JSON string representation of the object
print(SortOptionDTO.to_json())

# convert the object into a dict
sort_option_dto_dict = sort_option_dto_instance.to_dict()
# create an instance of SortOptionDTO from a dict
sort_option_dto_from_dict = SortOptionDTO.from_dict(sort_option_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


