# PlanningHierarchyFilterContextDTO

A plan context defined using hierarchy members

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hierarchy_name** | **str** | The object name of the hierarchy. | [optional] 
**included_members** | **List[str]** | The unique IDs of the included dimension members. | [optional] 
**excluded_members** | **List[str]** | The unique IDs of excluded dimension members. | [optional] 

## Example

```python
from visier.model_query.models.planning_hierarchy_filter_context_dto import PlanningHierarchyFilterContextDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PlanningHierarchyFilterContextDTO from a JSON string
planning_hierarchy_filter_context_dto_instance = PlanningHierarchyFilterContextDTO.from_json(json)
# print the JSON string representation of the object
print(PlanningHierarchyFilterContextDTO.to_json())

# convert the object into a dict
planning_hierarchy_filter_context_dto_dict = planning_hierarchy_filter_context_dto_instance.to_dict()
# create an instance of PlanningHierarchyFilterContextDTO from a dict
planning_hierarchy_filter_context_dto_from_dict = PlanningHierarchyFilterContextDTO.from_dict(planning_hierarchy_filter_context_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


