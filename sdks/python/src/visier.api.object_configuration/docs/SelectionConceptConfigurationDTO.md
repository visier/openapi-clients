# SelectionConceptConfigurationDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analytic_object_filters** | [**List[AnalyticObjectFilterDTO]**](AnalyticObjectFilterDTO.md) | A list of analytic object filters indicating the analytic object and dimension used for this selection concept. | [optional] 

## Example

```python
from visier.api.object_configuration.models.selection_concept_configuration_dto import SelectionConceptConfigurationDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SelectionConceptConfigurationDTO from a JSON string
selection_concept_configuration_dto_instance = SelectionConceptConfigurationDTO.from_json(json)
# print the JSON string representation of the object
print(SelectionConceptConfigurationDTO.to_json())

# convert the object into a dict
selection_concept_configuration_dto_dict = selection_concept_configuration_dto_instance.to_dict()
# create an instance of SelectionConceptConfigurationDTO from a dict
selection_concept_configuration_dto_from_dict = SelectionConceptConfigurationDTO.from_dict(selection_concept_configuration_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


