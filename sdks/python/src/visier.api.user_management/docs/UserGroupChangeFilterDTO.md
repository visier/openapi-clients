# UserGroupChangeFilterDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analytic_object_id** | **str** | The analytic object the filter applies to. Currently, the only supported analytic object is &#x60;Employee&#x60;. Default is &#x60;Employee&#x60;. | [optional] 
**dimension_filters** | [**List[UserGroupChangeDimensionFilterDTO]**](UserGroupChangeDimensionFilterDTO.md) | The dimensions in the dynamic filter. | [optional] 
**filter_id** | **str** | The unique identifier of the filter. Omit if creating a new filter. | [optional] 

## Example

```python
from visier.api.user_management.models.user_group_change_filter_dto import UserGroupChangeFilterDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupChangeFilterDTO from a JSON string
user_group_change_filter_dto_instance = UserGroupChangeFilterDTO.from_json(json)
# print the JSON string representation of the object
print(UserGroupChangeFilterDTO.to_json())

# convert the object into a dict
user_group_change_filter_dto_dict = user_group_change_filter_dto_instance.to_dict()
# create an instance of UserGroupChangeFilterDTO from a dict
user_group_change_filter_dto_from_dict = UserGroupChangeFilterDTO.from_dict(user_group_change_filter_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


