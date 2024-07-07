# TagMapElementDTO

Tag identifier and display name pair.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the tag. | [optional] 
**display_name** | **str** | The localized display name of the tag. | [optional] 

## Example

```python
from visier.model_query.models.tag_map_element_dto import TagMapElementDTO

# TODO update the JSON string below
json = "{}"
# create an instance of TagMapElementDTO from a JSON string
tag_map_element_dto_instance = TagMapElementDTO.from_json(json)
# print the JSON string representation of the object
print(TagMapElementDTO.to_json())

# convert the object into a dict
tag_map_element_dto_dict = tag_map_element_dto_instance.to_dict()
# create an instance of TagMapElementDTO from a dict
tag_map_element_dto_from_dict = TagMapElementDTO.from_dict(tag_map_element_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


