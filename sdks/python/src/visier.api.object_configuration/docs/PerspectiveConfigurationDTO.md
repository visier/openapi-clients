# PerspectiveConfigurationDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**perspective_id** | **str** | The UUID of the perspective. | [optional] 
**perspective_name** | **str** | The display name of the perspective. | [optional] 
**perspective_nodes** | [**List[PerspectiveNodeDTO]**](PerspectiveNodeDTO.md) | A list of nodes in the perspective. | [optional] 

## Example

```python
from visier.api.object_configuration.models.perspective_configuration_dto import PerspectiveConfigurationDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PerspectiveConfigurationDTO from a JSON string
perspective_configuration_dto_instance = PerspectiveConfigurationDTO.from_json(json)
# print the JSON string representation of the object
print(PerspectiveConfigurationDTO.to_json())

# convert the object into a dict
perspective_configuration_dto_dict = perspective_configuration_dto_instance.to_dict()
# create an instance of PerspectiveConfigurationDTO from a dict
perspective_configuration_dto_from_dict = PerspectiveConfigurationDTO.from_dict(perspective_configuration_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


