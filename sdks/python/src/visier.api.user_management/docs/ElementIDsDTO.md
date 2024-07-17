# ElementIDsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** | The unique identifiers. | [optional] 

## Example

```python
from visier.api.user_management.models.element_ids_dto import ElementIDsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ElementIDsDTO from a JSON string
element_ids_dto_instance = ElementIDsDTO.from_json(json)
# print the JSON string representation of the object
print(ElementIDsDTO.to_json())

# convert the object into a dict
element_ids_dto_dict = element_ids_dto_instance.to_dict()
# create an instance of ElementIDsDTO from a dict
element_ids_dto_from_dict = ElementIDsDTO.from_dict(element_ids_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


