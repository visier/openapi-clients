# ProfileAssignedForAccessibleTenantDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | An identifiable profile name to display in Visier such as \&quot;Partner Service Manager\&quot;. | [optional] 
**for_all_children** | **bool** | If true, the profile is assigned for all the analytic tenants of the administrating tenant. | [optional] 
**profile_id** | **str** | The unique identifier associated with the profile. | [optional] 
**tenant_code** | **str** | The tenant code of the analytic tenant on which this profile is assigned. | [optional] 
**validity_end_time** | **str** | An exclusive date-time when this profile is no longer active.   Note: Long.Max_Value means that endTime is undefined and is equivalent to permanent access. | [optional] 
**validity_start_time** | **str** | An inclusive date-time when this profile is active.   Note: Long.Min_Value means that startTime is undefined. | [optional] 

## Example

```python
from visier.api.profile_management.models.profile_assigned_for_accessible_tenant_dto import ProfileAssignedForAccessibleTenantDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileAssignedForAccessibleTenantDTO from a JSON string
profile_assigned_for_accessible_tenant_dto_instance = ProfileAssignedForAccessibleTenantDTO.from_json(json)
# print the JSON string representation of the object
print(ProfileAssignedForAccessibleTenantDTO.to_json())

# convert the object into a dict
profile_assigned_for_accessible_tenant_dto_dict = profile_assigned_for_accessible_tenant_dto_instance.to_dict()
# create an instance of ProfileAssignedForAccessibleTenantDTO from a dict
profile_assigned_for_accessible_tenant_dto_from_dict = ProfileAssignedForAccessibleTenantDTO.from_dict(profile_assigned_for_accessible_tenant_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


