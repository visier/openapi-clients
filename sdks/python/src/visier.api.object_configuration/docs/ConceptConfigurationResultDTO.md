# ConceptConfigurationResultDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**concept_id** | **str** | The unique identifier of the configured concept. | [optional] 
**message** | **str** | A meaningful message about the API result. | [optional] 
**project_id** | **str** | The unique identifier of the system-generated project. | [optional] 

## Example

```python
from visier.api.object_configuration.models.concept_configuration_result_dto import ConceptConfigurationResultDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ConceptConfigurationResultDTO from a JSON string
concept_configuration_result_dto_instance = ConceptConfigurationResultDTO.from_json(json)
# print the JSON string representation of the object
print(ConceptConfigurationResultDTO.to_json())

# convert the object into a dict
concept_configuration_result_dto_dict = concept_configuration_result_dto_instance.to_dict()
# create an instance of ConceptConfigurationResultDTO from a dict
concept_configuration_result_dto_from_dict = ConceptConfigurationResultDTO.from_dict(concept_configuration_result_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


