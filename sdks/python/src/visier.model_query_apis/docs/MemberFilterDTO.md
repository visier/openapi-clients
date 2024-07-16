# MemberFilterDTO

Member filters are dimension member values to filter by in your query. The member filters are  defined within the filters section of a query definition. You can filter by dimension members in  aggregate and list queries.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimension** | [**DimensionReferenceDTO**](DimensionReferenceDTO.md) | The dimension in which the members belong. | [optional] 
**values** | [**MemberValuesDTO**](MemberValuesDTO.md) | The dimension members to filter by. | [optional] 

## Example

```python
from visier.model_query_apis.models.member_filter_dto import MemberFilterDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MemberFilterDTO from a JSON string
member_filter_dto_instance = MemberFilterDTO.from_json(json)
# print the JSON string representation of the object
print(MemberFilterDTO.to_json())

# convert the object into a dict
member_filter_dto_dict = member_filter_dto_instance.to_dict()
# create an instance of MemberFilterDTO from a dict
member_filter_dto_from_dict = MemberFilterDTO.from_dict(member_filter_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


