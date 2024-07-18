# DimensionMappingValidationExecutionDTO

Instruction to execute a mapping validation query

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analytic_object** | **str** | the analytic object associated with the dimension map | [optional] 
**member_map_id** | **str** | memberMapId &#x3D;&#x3D; dimensionMapId | [optional] 

## Example

```python
from visier.api.model_query.models.dimension_mapping_validation_execution_dto import DimensionMappingValidationExecutionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DimensionMappingValidationExecutionDTO from a JSON string
dimension_mapping_validation_execution_dto_instance = DimensionMappingValidationExecutionDTO.from_json(json)
# print the JSON string representation of the object
print(DimensionMappingValidationExecutionDTO.to_json())

# convert the object into a dict
dimension_mapping_validation_execution_dto_dict = dimension_mapping_validation_execution_dto_instance.to_dict()
# create an instance of DimensionMappingValidationExecutionDTO from a dict
dimension_mapping_validation_execution_dto_from_dict = DimensionMappingValidationExecutionDTO.from_dict(dimension_mapping_validation_execution_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


