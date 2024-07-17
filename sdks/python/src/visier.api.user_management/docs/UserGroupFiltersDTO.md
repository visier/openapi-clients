# UserGroupFiltersDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**List[UserGroupChangeFilterDTO]**](UserGroupChangeFilterDTO.md) | The filters that define user group membership. | [optional] 

## Example

```python
from visier.api.user_management.models.user_group_filters_dto import UserGroupFiltersDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupFiltersDTO from a JSON string
user_group_filters_dto_instance = UserGroupFiltersDTO.from_json(json)
# print the JSON string representation of the object
print(UserGroupFiltersDTO.to_json())

# convert the object into a dict
user_group_filters_dto_dict = user_group_filters_dto_instance.to_dict()
# create an instance of UserGroupFiltersDTO from a dict
user_group_filters_dto_from_dict = UserGroupFiltersDTO.from_dict(user_group_filters_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


