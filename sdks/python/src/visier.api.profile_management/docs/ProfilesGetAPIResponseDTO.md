# ProfilesGetAPIResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profiles** | [**List[ProfileGetAPIResponseDTO]**](ProfileGetAPIResponseDTO.md) | A list of objects representing the available profiles. | [optional] 

## Example

```python
from visier.api.profile_management.models.profiles_get_api_response_dto import ProfilesGetAPIResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ProfilesGetAPIResponseDTO from a JSON string
profiles_get_api_response_dto_instance = ProfilesGetAPIResponseDTO.from_json(json)
# print the JSON string representation of the object
print(ProfilesGetAPIResponseDTO.to_json())

# convert the object into a dict
profiles_get_api_response_dto_dict = profiles_get_api_response_dto_instance.to_dict()
# create an instance of ProfilesGetAPIResponseDTO from a dict
profiles_get_api_response_dto_from_dict = ProfilesGetAPIResponseDTO.from_dict(profiles_get_api_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


