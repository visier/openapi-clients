# DimensionMemberReferenceDTO

The members of a dimension.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **List[str]** | A list of strings representing the members within a dimension path. For example, a dimension for Location  may have the paths \&quot;Canada, BC, Vancouver\&quot; and \&quot;US, California, San Francisco\&quot;. | [optional] 

## Example

```python
from visier.model_query_apis.models.dimension_member_reference_dto import DimensionMemberReferenceDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DimensionMemberReferenceDTO from a JSON string
dimension_member_reference_dto_instance = DimensionMemberReferenceDTO.from_json(json)
# print the JSON string representation of the object
print(DimensionMemberReferenceDTO.to_json())

# convert the object into a dict
dimension_member_reference_dto_dict = dimension_member_reference_dto_instance.to_dict()
# create an instance of DimensionMemberReferenceDTO from a dict
dimension_member_reference_dto_from_dict = DimensionMemberReferenceDTO.from_dict(dimension_member_reference_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


