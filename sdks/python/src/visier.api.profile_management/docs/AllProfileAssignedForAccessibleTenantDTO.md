# AllProfileAssignedForAccessibleTenantDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigned_profiles_for_accessible_tenant** | [**List[ProfileAssignedForAccessibleTenantDTO]**](ProfileAssignedForAccessibleTenantDTO.md) | A list of objects representing the user profiles assigned to the user and their validity range. | [optional] 

## Example

```python
from visier.api.profile_management.models.all_profile_assigned_for_accessible_tenant_dto import AllProfileAssignedForAccessibleTenantDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AllProfileAssignedForAccessibleTenantDTO from a JSON string
all_profile_assigned_for_accessible_tenant_dto_instance = AllProfileAssignedForAccessibleTenantDTO.from_json(json)
# print the JSON string representation of the object
print(AllProfileAssignedForAccessibleTenantDTO.to_json())

# convert the object into a dict
all_profile_assigned_for_accessible_tenant_dto_dict = all_profile_assigned_for_accessible_tenant_dto_instance.to_dict()
# create an instance of AllProfileAssignedForAccessibleTenantDTO from a dict
all_profile_assigned_for_accessible_tenant_dto_from_dict = AllProfileAssignedForAccessibleTenantDTO.from_dict(all_profile_assigned_for_accessible_tenant_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


