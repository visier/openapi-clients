# UserGroupChangeDimensionFilterDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimension_id** | **str** | The object name of the dimension. | [optional] 
**member_selections** | [**List[UserGroupChangeMemberSelectionDTO]**](UserGroupChangeMemberSelectionDTO.md) | The dimension members to select in the dynamic filter. | [optional] 
**subject_reference_path** | [**ElementIDsDTO**](ElementIDsDTO.md) | A qualifying path if the dimension is from an analytic object that references Employee.  For example, use &#x60;subjectReferencePath&#x60; to create a filter on the &#x60;Employment_Start_Type&#x60; dimension from the &#x60;Employment_Start&#x60; object, which references &#x60;Employee&#x60;: &#x60;{ \&quot;ids\&quot;: [ \&quot;Employee\&quot;, \&quot;Employment_Start\&quot; ] }&#x60;. | [optional] 

## Example

```python
from visier.api.user_management.models.user_group_change_dimension_filter_dto import UserGroupChangeDimensionFilterDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupChangeDimensionFilterDTO from a JSON string
user_group_change_dimension_filter_dto_instance = UserGroupChangeDimensionFilterDTO.from_json(json)
# print the JSON string representation of the object
print(UserGroupChangeDimensionFilterDTO.to_json())

# convert the object into a dict
user_group_change_dimension_filter_dto_dict = user_group_change_dimension_filter_dto_instance.to_dict()
# create an instance of UserGroupChangeDimensionFilterDTO from a dict
user_group_change_dimension_filter_dto_from_dict = UserGroupChangeDimensionFilterDTO.from_dict(user_group_change_dimension_filter_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


