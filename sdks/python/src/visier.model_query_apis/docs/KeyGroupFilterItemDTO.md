# KeyGroupFilterItemDTO

An individual filter in a key group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**formula** | **str** | A filter expressed as a formula. | [optional] 
**member_set** | [**MemberFilterDTO**](MemberFilterDTO.md) | A filter that includes or excludes dimension members. | [optional] 
**selection_concept** | [**SelectionConceptReferenceDTO**](SelectionConceptReferenceDTO.md) | A filter that uses an existing selection concept in Visier. | [optional] 

## Example

```python
from visier.model_query_apis.models.key_group_filter_item_dto import KeyGroupFilterItemDTO

# TODO update the JSON string below
json = "{}"
# create an instance of KeyGroupFilterItemDTO from a JSON string
key_group_filter_item_dto_instance = KeyGroupFilterItemDTO.from_json(json)
# print the JSON string representation of the object
print(KeyGroupFilterItemDTO.to_json())

# convert the object into a dict
key_group_filter_item_dto_dict = key_group_filter_item_dto_instance.to_dict()
# create an instance of KeyGroupFilterItemDTO from a dict
key_group_filter_item_dto_from_dict = KeyGroupFilterItemDTO.from_dict(key_group_filter_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


