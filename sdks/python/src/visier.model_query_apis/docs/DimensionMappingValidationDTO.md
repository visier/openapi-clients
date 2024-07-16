# DimensionMappingValidationDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimension_id** | **str** |  | [optional] 
**dimension_map_id** | **str** |  | [optional] 
**failures** | **List[str]** |  | [optional] 
**unmapped_members** | [**List[DimensionMemberReferenceDTO]**](DimensionMemberReferenceDTO.md) |  | [optional] 

## Example

```python
from visier.model_query_apis.models.dimension_mapping_validation_dto import DimensionMappingValidationDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DimensionMappingValidationDTO from a JSON string
dimension_mapping_validation_dto_instance = DimensionMappingValidationDTO.from_json(json)
# print the JSON string representation of the object
print(DimensionMappingValidationDTO.to_json())

# convert the object into a dict
dimension_mapping_validation_dto_dict = dimension_mapping_validation_dto_instance.to_dict()
# create an instance of DimensionMappingValidationDTO from a dict
dimension_mapping_validation_dto_from_dict = DimensionMappingValidationDTO.from_dict(dimension_mapping_validation_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


