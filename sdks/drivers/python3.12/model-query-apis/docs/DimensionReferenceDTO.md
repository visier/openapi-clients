# DimensionReferenceDTO

The name and qualifying path of a dimension to query.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The ID of the dimension. See &#x60;Dimensions&#x60; to get the ID. | [optional] 
**qualifying_path** | **str** | The qualifying path to the dimension in Visier, such as the analytic object or event the dimension is  associated with. If the path has multiple objects, each object is separated by a period. | [optional] 

## Example

```python
from visier.model_query.models.dimension_reference_dto import DimensionReferenceDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DimensionReferenceDTO from a JSON string
dimension_reference_dto_instance = DimensionReferenceDTO.from_json(json)
# print the JSON string representation of the object
print(DimensionReferenceDTO.to_json())

# convert the object into a dict
dimension_reference_dto_dict = dimension_reference_dto_instance.to_dict()
# create an instance of DimensionReferenceDTO from a dict
dimension_reference_dto_from_dict = DimensionReferenceDTO.from_dict(dimension_reference_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


