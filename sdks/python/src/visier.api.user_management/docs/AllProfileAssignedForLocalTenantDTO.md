# AllProfileAssignedForLocalTenantDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigned_profiles** | [**List[ProfileAssignedForLocalTenantDTO]**](ProfileAssignedForLocalTenantDTO.md) | A list of objects representing the user profiles assigned to the user and their validity range. | [optional] 

## Example

```python
from visier.api.user_management.models.all_profile_assigned_for_local_tenant_dto import AllProfileAssignedForLocalTenantDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AllProfileAssignedForLocalTenantDTO from a JSON string
all_profile_assigned_for_local_tenant_dto_instance = AllProfileAssignedForLocalTenantDTO.from_json(json)
# print the JSON string representation of the object
print(AllProfileAssignedForLocalTenantDTO.to_json())

# convert the object into a dict
all_profile_assigned_for_local_tenant_dto_dict = all_profile_assigned_for_local_tenant_dto_instance.to_dict()
# create an instance of AllProfileAssignedForLocalTenantDTO from a dict
all_profile_assigned_for_local_tenant_dto_from_dict = AllProfileAssignedForLocalTenantDTO.from_dict(all_profile_assigned_for_local_tenant_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


