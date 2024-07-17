# InheritedAccessConfigDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analytic_object_id** | **str** | The analytic object ID associated with the inherited access configuration. | [optional] 
**member_filter_configs** | [**List[MemberFilterConfigDTO]**](MemberFilterConfigDTO.md) | Custom filters that define population access for an inherited analytic object in the permission. | [optional] 
**remove_access** | **bool** | The flag for removing access to the inherited analytic object. | [optional] 

## Example

```python
from visier.api.permission_management.models.inherited_access_config_dto import InheritedAccessConfigDTO

# TODO update the JSON string below
json = "{}"
# create an instance of InheritedAccessConfigDTO from a JSON string
inherited_access_config_dto_instance = InheritedAccessConfigDTO.from_json(json)
# print the JSON string representation of the object
print(InheritedAccessConfigDTO.to_json())

# convert the object into a dict
inherited_access_config_dto_dict = inherited_access_config_dto_instance.to_dict()
# create an instance of InheritedAccessConfigDTO from a dict
inherited_access_config_dto_from_dict = InheritedAccessConfigDTO.from_dict(inherited_access_config_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


