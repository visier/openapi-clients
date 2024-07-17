# DimensionMemberDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimension_member** | **List[str]** | A list of strings representing the dimension members. Dimension members in a hierarchical dimension  will have an array with multiple strings. | [optional] 

## Example

```python
from visier.api.object_configuration.models.dimension_member_dto import DimensionMemberDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DimensionMemberDTO from a JSON string
dimension_member_dto_instance = DimensionMemberDTO.from_json(json)
# print the JSON string representation of the object
print(DimensionMemberDTO.to_json())

# convert the object into a dict
dimension_member_dto_dict = dimension_member_dto_instance.to_dict()
# create an instance of DimensionMemberDTO from a dict
dimension_member_dto_from_dict = DimensionMemberDTO.from_dict(dimension_member_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


