# HomeAnalysisByUserGroupDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**home_analysis_id** | **str** | The unique ID of the analysis to show for this user group when a user logs in. | [optional] 
**user_group_id** | **str** | The user group ID. | [optional] 

## Example

```python
from visier.api.tenant_management.models.home_analysis_by_user_group_dto import HomeAnalysisByUserGroupDTO

# TODO update the JSON string below
json = "{}"
# create an instance of HomeAnalysisByUserGroupDTO from a JSON string
home_analysis_by_user_group_dto_instance = HomeAnalysisByUserGroupDTO.from_json(json)
# print the JSON string representation of the object
print(HomeAnalysisByUserGroupDTO.to_json())

# convert the object into a dict
home_analysis_by_user_group_dto_dict = home_analysis_by_user_group_dto_instance.to_dict()
# create an instance of HomeAnalysisByUserGroupDTO from a dict
home_analysis_by_user_group_dto_from_dict = HomeAnalysisByUserGroupDTO.from_dict(home_analysis_by_user_group_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


