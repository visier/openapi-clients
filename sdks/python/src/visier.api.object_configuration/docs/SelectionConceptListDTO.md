# SelectionConceptListDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**concepts** | [**List[SelectionConceptDTO]**](SelectionConceptDTO.md) | A list of objects representing selection concepts. | [optional] 

## Example

```python
from visier.api.object_configuration.models.selection_concept_list_dto import SelectionConceptListDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SelectionConceptListDTO from a JSON string
selection_concept_list_dto_instance = SelectionConceptListDTO.from_json(json)
# print the JSON string representation of the object
print(SelectionConceptListDTO.to_json())

# convert the object into a dict
selection_concept_list_dto_dict = selection_concept_list_dto_instance.to_dict()
# create an instance of SelectionConceptListDTO from a dict
selection_concept_list_dto_from_dict = SelectionConceptListDTO.from_dict(selection_concept_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


