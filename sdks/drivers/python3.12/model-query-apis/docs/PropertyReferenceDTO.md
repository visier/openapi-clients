# PropertyReferenceDTO

The name and qualifying path of a property to query.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The ID of the property. See &#x60;Properties&#x60; to get the ID. | [optional] 
**qualifying_path** | **str** | The qualifying path to the property in Visier, such as the analytic object or event the property is associated with.  If the path has multiple objects, each object is separated by a period. | [optional] 

## Example

```python
from visier.model_query.models.property_reference_dto import PropertyReferenceDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyReferenceDTO from a JSON string
property_reference_dto_instance = PropertyReferenceDTO.from_json(json)
# print the JSON string representation of the object
print(PropertyReferenceDTO.to_json())

# convert the object into a dict
property_reference_dto_dict = property_reference_dto_instance.to_dict()
# create an instance of PropertyReferenceDTO from a dict
property_reference_dto_from_dict = PropertyReferenceDTO.from_dict(property_reference_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


