# CalculationConceptListDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**concepts** | [**List[CalculationConceptDTO]**](CalculationConceptDTO.md) | A list of objects representing calculation concepts. | [optional] 

## Example

```python
from visier.api.object_configuration.models.calculation_concept_list_dto import CalculationConceptListDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CalculationConceptListDTO from a JSON string
calculation_concept_list_dto_instance = CalculationConceptListDTO.from_json(json)
# print the JSON string representation of the object
print(CalculationConceptListDTO.to_json())

# convert the object into a dict
calculation_concept_list_dto_dict = calculation_concept_list_dto_instance.to_dict()
# create an instance of CalculationConceptListDTO from a dict
calculation_concept_list_dto_from_dict = CalculationConceptListDTO.from_dict(calculation_concept_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


