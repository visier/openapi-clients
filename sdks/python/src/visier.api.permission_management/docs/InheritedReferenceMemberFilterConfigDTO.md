# InheritedReferenceMemberFilterConfigDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_analytic_object_id** | **str** | * The unique ID of the analytic object that the source analytic object should inherit filters from. The target analytic object must have a binding (strong) reference from the source analytic object. | [optional] 

## Example

```python
from visier.api.permission_management.models.inherited_reference_member_filter_config_dto import InheritedReferenceMemberFilterConfigDTO

# TODO update the JSON string below
json = "{}"
# create an instance of InheritedReferenceMemberFilterConfigDTO from a JSON string
inherited_reference_member_filter_config_dto_instance = InheritedReferenceMemberFilterConfigDTO.from_json(json)
# print the JSON string representation of the object
print(InheritedReferenceMemberFilterConfigDTO.to_json())

# convert the object into a dict
inherited_reference_member_filter_config_dto_dict = inherited_reference_member_filter_config_dto_instance.to_dict()
# create an instance of InheritedReferenceMemberFilterConfigDTO from a dict
inherited_reference_member_filter_config_dto_from_dict = InheritedReferenceMemberFilterConfigDTO.from_dict(inherited_reference_member_filter_config_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


