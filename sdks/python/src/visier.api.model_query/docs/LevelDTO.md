# LevelDTO

Levels are the hierarchical structure of members within a dimension.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**depth** | **int** | The level depth of the dimension. | [optional] 
**display_name** | **str** | The localized display name of the dimension. | [optional] 
**id** | **str** | The unique ID of a level within a dimension. | [optional] 

## Example

```python
from visier.api.model_query.models.level_dto import LevelDTO

# TODO update the JSON string below
json = "{}"
# create an instance of LevelDTO from a JSON string
level_dto_instance = LevelDTO.from_json(json)
# print the JSON string representation of the object
print(LevelDTO.to_json())

# convert the object into a dict
level_dto_dict = level_dto_instance.to_dict()
# create an instance of LevelDTO from a dict
level_dto_from_dict = LevelDTO.from_dict(level_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


