# AdditionalCapabilitiesDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_capabilities** | **List[str]** | The additional capabilities assigned to this profile. | [optional] 

## Example

```python
from visier.api.user_management.models.additional_capabilities_dto import AdditionalCapabilitiesDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalCapabilitiesDTO from a JSON string
additional_capabilities_dto_instance = AdditionalCapabilitiesDTO.from_json(json)
# print the JSON string representation of the object
print(AdditionalCapabilitiesDTO.to_json())

# convert the object into a dict
additional_capabilities_dto_dict = additional_capabilities_dto_instance.to_dict()
# create an instance of AdditionalCapabilitiesDTO from a dict
additional_capabilities_dto_from_dict = AdditionalCapabilitiesDTO.from_dict(additional_capabilities_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


