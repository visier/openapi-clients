# CustomPropertyDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from visier.api.tenant_management.models.custom_property_dto import CustomPropertyDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CustomPropertyDTO from a JSON string
custom_property_dto_instance = CustomPropertyDTO.from_json(json)
# print the JSON string representation of the object
print(CustomPropertyDTO.to_json())

# convert the object into a dict
custom_property_dto_dict = custom_property_dto_instance.to_dict()
# create an instance of CustomPropertyDTO from a dict
custom_property_dto_from_dict = CustomPropertyDTO.from_dict(custom_property_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


