# CapabilitiesDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_level** | **str** | The access level of the profile for the given capability. | [optional] 
**capability** | **str** | The name of the capability. | [optional] 
**view_level** | **str** | The view level of the profile for the given capability. | [optional] 

## Example

```python
from visier.api.user_management.models.capabilities_dto import CapabilitiesDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CapabilitiesDTO from a JSON string
capabilities_dto_instance = CapabilitiesDTO.from_json(json)
# print the JSON string representation of the object
print(CapabilitiesDTO.to_json())

# convert the object into a dict
capabilities_dto_dict = capabilities_dto_instance.to_dict()
# create an instance of CapabilitiesDTO from a dict
capabilities_dto_from_dict = CapabilitiesDTO.from_dict(capabilities_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


