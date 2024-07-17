# GetCapabilitiesAPIResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capabilities** | [**List[CapabilityDTO]**](CapabilityDTO.md) | A list of objects representing the available capabilities. | [optional] 

## Example

```python
from visier.api.permission_management.models.get_capabilities_api_response_dto import GetCapabilitiesAPIResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of GetCapabilitiesAPIResponseDTO from a JSON string
get_capabilities_api_response_dto_instance = GetCapabilitiesAPIResponseDTO.from_json(json)
# print the JSON string representation of the object
print(GetCapabilitiesAPIResponseDTO.to_json())

# convert the object into a dict
get_capabilities_api_response_dto_dict = get_capabilities_api_response_dto_instance.to_dict()
# create an instance of GetCapabilitiesAPIResponseDTO from a dict
get_capabilities_api_response_dto_from_dict = GetCapabilitiesAPIResponseDTO.from_dict(get_capabilities_api_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


