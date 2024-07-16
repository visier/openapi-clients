# PopulationConfigurationDTO

A set of property and dimension references configured by Visier or an administrator to tell the platform what  properties and dimensions to use when doing population insight calculations. These are the distinguishing properties,  change history properties, and grouping dimensions to use in AI insights.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_history_properties** | [**List[PropertyReferenceDTO]**](PropertyReferenceDTO.md) | Properties that are used by default to compare subject members over time. | [optional] 
**distinguishing_properties** | [**List[PropertyReferenceDTO]**](PropertyReferenceDTO.md) | Properties that are used by default to compare subject members. | [optional] 
**grouping_dimensions** | [**List[DimensionReferenceDTO]**](DimensionReferenceDTO.md) | Dimensions to use for grouping and clustering the population. | [optional] 

## Example

```python
from visier.model_query_apis.models.population_configuration_dto import PopulationConfigurationDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PopulationConfigurationDTO from a JSON string
population_configuration_dto_instance = PopulationConfigurationDTO.from_json(json)
# print the JSON string representation of the object
print(PopulationConfigurationDTO.to_json())

# convert the object into a dict
population_configuration_dto_dict = population_configuration_dto_instance.to_dict()
# create an instance of PopulationConfigurationDTO from a dict
population_configuration_dto_from_dict = PopulationConfigurationDTO.from_dict(population_configuration_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


