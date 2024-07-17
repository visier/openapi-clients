# ProfileGetAPIResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_capabilities** | **List[str]** | A list of the additional capabilities that are assigned to this profile. | [optional] 
**capabilities** | [**List[CapabilitiesDTO]**](CapabilitiesDTO.md) | A list of objects representing the access that this profile has for the capabilities of this profile. | [optional] 
**display_name** | **str** | An identifiable profile name to display in Visier. For example, \&quot;Partner Service Manager\&quot;. | [optional] 
**profile_id** | **str** | The unique identifier associated with the profile. | [optional] 

## Example

```python
from visier.api.profile_management.models.profile_get_api_response_dto import ProfileGetAPIResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileGetAPIResponseDTO from a JSON string
profile_get_api_response_dto_instance = ProfileGetAPIResponseDTO.from_json(json)
# print the JSON string representation of the object
print(ProfileGetAPIResponseDTO.to_json())

# convert the object into a dict
profile_get_api_response_dto_dict = profile_get_api_response_dto_instance.to_dict()
# create an instance of ProfileGetAPIResponseDTO from a dict
profile_get_api_response_dto_from_dict = ProfileGetAPIResponseDTO.from_dict(profile_get_api_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


