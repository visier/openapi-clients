# ProfileAssignedForLocalTenantDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_capabilities** | [**AdditionalCapabilitiesDTO**](AdditionalCapabilitiesDTO.md) | A list of the additional capabilities that are assigned to this profile. | [optional] 
**capabilities** | [**List[CapabilitiesDTO]**](CapabilitiesDTO.md) | A list of objects representing the access that this profile has for the capabilities of this profile. | [optional] 
**display_name** | **str** | An identifiable profile name to display in Visier, such as \&quot;Partner Service Manager\&quot;. | [optional] 
**profile_id** | **str** | The unique identifier associated with the profile. | [optional] 
**validity_end_time** | **str** | An exclusive date-time when this profile is no longer active. | [optional] 
**validity_start_time** | **str** | An inclusive date-time when this profile is active. | [optional] 

## Example

```python
from visier.api.profile_management.models.profile_assigned_for_local_tenant_dto import ProfileAssignedForLocalTenantDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileAssignedForLocalTenantDTO from a JSON string
profile_assigned_for_local_tenant_dto_instance = ProfileAssignedForLocalTenantDTO.from_json(json)
# print the JSON string representation of the object
print(ProfileAssignedForLocalTenantDTO.to_json())

# convert the object into a dict
profile_assigned_for_local_tenant_dto_dict = profile_assigned_for_local_tenant_dto_instance.to_dict()
# create an instance of ProfileAssignedForLocalTenantDTO from a dict
profile_assigned_for_local_tenant_dto_from_dict = ProfileAssignedForLocalTenantDTO.from_dict(profile_assigned_for_local_tenant_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


