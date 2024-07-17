# CalculationConceptDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | [**CalculationConceptConfigurationDTO**](CalculationConceptConfigurationDTO.md) | A list of objects representing the configuration for the calculation concept. | [optional] 
**name** | **str** | The display name of the calculation concept. | [optional] 
**uuid** | **str** | The unique identifier associated with the calculation concept. | [optional] 

## Example

```python
from visier.api.object_configuration.models.calculation_concept_dto import CalculationConceptDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CalculationConceptDTO from a JSON string
calculation_concept_dto_instance = CalculationConceptDTO.from_json(json)
# print the JSON string representation of the object
print(CalculationConceptDTO.to_json())

# convert the object into a dict
calculation_concept_dto_dict = calculation_concept_dto_instance.to_dict()
# create an instance of CalculationConceptDTO from a dict
calculation_concept_dto_from_dict = CalculationConceptDTO.from_dict(calculation_concept_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


