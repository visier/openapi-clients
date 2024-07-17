# MemberFilterConfigDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimension_filters** | [**List[DimensionFilterDTO]**](DimensionFilterDTO.md) | A list of objects representing the custom filters that define population access for the item.   A custom filter can be a \&quot;member filter\&quot; (&#x60;staticDimensionFilter&#x60;) or a \&quot;dynamic filter\&quot; (&#x60;dynamicDimensionFilter&#x60;). | [optional] 

## Example

```python
from visier.api.permission_management.models.member_filter_config_dto import MemberFilterConfigDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MemberFilterConfigDTO from a JSON string
member_filter_config_dto_instance = MemberFilterConfigDTO.from_json(json)
# print the JSON string representation of the object
print(MemberFilterConfigDTO.to_json())

# convert the object into a dict
member_filter_config_dto_dict = member_filter_config_dto_instance.to_dict()
# create an instance of MemberFilterConfigDTO from a dict
member_filter_config_dto_from_dict = MemberFilterConfigDTO.from_dict(member_filter_config_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


