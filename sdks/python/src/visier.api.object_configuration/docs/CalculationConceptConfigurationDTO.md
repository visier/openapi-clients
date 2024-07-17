# CalculationConceptConfigurationDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**perspectives** | [**List[PerspectiveConfigurationDTO]**](PerspectiveConfigurationDTO.md) | A list of objects representing the perspectives in the calculation concept. | [optional] 

## Example

```python
from visier.api.object_configuration.models.calculation_concept_configuration_dto import CalculationConceptConfigurationDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CalculationConceptConfigurationDTO from a JSON string
calculation_concept_configuration_dto_instance = CalculationConceptConfigurationDTO.from_json(json)
# print the JSON string representation of the object
print(CalculationConceptConfigurationDTO.to_json())

# convert the object into a dict
calculation_concept_configuration_dto_dict = calculation_concept_configuration_dto_instance.to_dict()
# create an instance of CalculationConceptConfigurationDTO from a dict
calculation_concept_configuration_dto_from_dict = CalculationConceptConfigurationDTO.from_dict(calculation_concept_configuration_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


