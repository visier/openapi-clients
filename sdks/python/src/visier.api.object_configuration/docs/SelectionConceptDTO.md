# SelectionConceptDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | [**SelectionConceptConfigurationDTO**](SelectionConceptConfigurationDTO.md) | A list of objects representing the configuration for the selection concept. | [optional] 
**name** | **str** | The display name of the selection concept. | [optional] 
**uuid** | **str** | The unique identifier associated with the selection concept. | [optional] 

## Example

```python
from visier.api.object_configuration.models.selection_concept_dto import SelectionConceptDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SelectionConceptDTO from a JSON string
selection_concept_dto_instance = SelectionConceptDTO.from_json(json)
# print the JSON string representation of the object
print(SelectionConceptDTO.to_json())

# convert the object into a dict
selection_concept_dto_dict = selection_concept_dto_instance.to_dict()
# create an instance of SelectionConceptDTO from a dict
selection_concept_dto_from_dict = SelectionConceptDTO.from_dict(selection_concept_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


