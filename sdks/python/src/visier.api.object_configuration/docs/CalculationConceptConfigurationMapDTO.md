# CalculationConceptConfigurationMapDTO

The configuration to apply to the concept.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**perspectives_to_map** | [**List[PerspectiveConfigurationDTO]**](PerspectiveConfigurationDTO.md) | A list of objects representing the list of perspectives in the calculation concept. | [optional] 

## Example

```python
from visier.api.object_configuration.models.calculation_concept_configuration_map_dto import CalculationConceptConfigurationMapDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CalculationConceptConfigurationMapDTO from a JSON string
calculation_concept_configuration_map_dto_instance = CalculationConceptConfigurationMapDTO.from_json(json)
# print the JSON string representation of the object
print(CalculationConceptConfigurationMapDTO.to_json())

# convert the object into a dict
calculation_concept_configuration_map_dto_dict = calculation_concept_configuration_map_dto_instance.to_dict()
# create an instance of CalculationConceptConfigurationMapDTO from a dict
calculation_concept_configuration_map_dto_from_dict = CalculationConceptConfigurationMapDTO.from_dict(calculation_concept_configuration_map_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


