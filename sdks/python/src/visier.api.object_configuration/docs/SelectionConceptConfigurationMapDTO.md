# SelectionConceptConfigurationMapDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analytic_object_filters_to_map** | [**List[AnalyticObjectFilterDTO]**](AnalyticObjectFilterDTO.md) | A list of analytic object filters indicating the analytic object and dimension members used  for the selection concept.   Note: If this array is empty, all filters will be removed for the concept. | [optional] 

## Example

```python
from visier.api.object_configuration.models.selection_concept_configuration_map_dto import SelectionConceptConfigurationMapDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SelectionConceptConfigurationMapDTO from a JSON string
selection_concept_configuration_map_dto_instance = SelectionConceptConfigurationMapDTO.from_json(json)
# print the JSON string representation of the object
print(SelectionConceptConfigurationMapDTO.to_json())

# convert the object into a dict
selection_concept_configuration_map_dto_dict = selection_concept_configuration_map_dto_instance.to_dict()
# create an instance of SelectionConceptConfigurationMapDTO from a dict
selection_concept_configuration_map_dto_from_dict = SelectionConceptConfigurationMapDTO.from_dict(selection_concept_configuration_map_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


