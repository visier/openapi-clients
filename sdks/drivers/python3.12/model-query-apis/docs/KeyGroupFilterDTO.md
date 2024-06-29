# KeyGroupFilterDTO

A collection of related filters that define a key group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**List[KeyGroupFilterItemDTO]**](KeyGroupFilterItemDTO.md) |  | [optional] 

## Example

```python
from visier.model_query.models.key_group_filter_dto import KeyGroupFilterDTO

# TODO update the JSON string below
json = "{}"
# create an instance of KeyGroupFilterDTO from a JSON string
key_group_filter_dto_instance = KeyGroupFilterDTO.from_json(json)
# print the JSON string representation of the object
print(KeyGroupFilterDTO.to_json())

# convert the object into a dict
key_group_filter_dto_dict = key_group_filter_dto_instance.to_dict()
# create an instance of KeyGroupFilterDTO from a dict
key_group_filter_dto_from_dict = KeyGroupFilterDTO.from_dict(key_group_filter_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


