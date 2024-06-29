# ObjectReferenceDTO

A link between one analytic object and another. An ObjectReference allows you to discover the relationships between  analytic objects. In some queries, you may need to provide a qualifyingPath, which is built from ObjectReference information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the object reference. | [optional] 
**display_name** | **str** | The localized display name of the object reference. | [optional] 
**description** | **str** | The localized description of the object reference. | [optional] 
**from_object** | **str** | The ID of the referencing analytic object. | [optional] 
**to_object** | **str** | The ID of the referenced analytic object. | [optional] 
**type** | **int** | The type of object reference. | [optional] 
**is_strong_reference** | **bool** | True if this is a strong reference. | [optional] 

## Example

```python
from visier.model_query.models.object_reference_dto import ObjectReferenceDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectReferenceDTO from a JSON string
object_reference_dto_instance = ObjectReferenceDTO.from_json(json)
# print the JSON string representation of the object
print(ObjectReferenceDTO.to_json())

# convert the object into a dict
object_reference_dto_dict = object_reference_dto_instance.to_dict()
# create an instance of ObjectReferenceDTO from a dict
object_reference_dto_from_dict = ObjectReferenceDTO.from_dict(object_reference_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


