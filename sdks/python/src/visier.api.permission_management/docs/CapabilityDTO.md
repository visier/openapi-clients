# CapabilityDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A description of the capability. | [optional] 
**display_name** | **str** | An identifiable capability name to display in Visier, such as \&quot;Schedule Analysis\&quot;. | [optional] 
**name** | **str** | The unique name of the capability. | [optional] 

## Example

```python
from visier.api.permission_management.models.capability_dto import CapabilityDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CapabilityDTO from a JSON string
capability_dto_instance = CapabilityDTO.from_json(json)
# print the JSON string representation of the object
print(CapabilityDTO.to_json())

# convert the object into a dict
capability_dto_dict = capability_dto_instance.to_dict()
# create an instance of CapabilityDTO from a dict
capability_dto_from_dict = CapabilityDTO.from_dict(capability_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


