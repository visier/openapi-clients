# PerspectiveNodeDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analytic_object_filters** | [**List[AnalyticObjectFilterDTO]**](AnalyticObjectFilterDTO.md) | A list of analytic object filters indicating the analytic object and dimensions used for the selection concept. | [optional] 
**selection_concept_uuid** | **str** | The UUID of the node&#39;s selection concept. Perspective nodes are generated as selection concepts to enable filtering. | [optional] 
**symbol_name** | **str** | The symbol name of the selection concept. For example, \&quot;isExitActualSystemTermination\&quot;. | [optional] 

## Example

```python
from visier.api.object_configuration.models.perspective_node_dto import PerspectiveNodeDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PerspectiveNodeDTO from a JSON string
perspective_node_dto_instance = PerspectiveNodeDTO.from_json(json)
# print the JSON string representation of the object
print(PerspectiveNodeDTO.to_json())

# convert the object into a dict
perspective_node_dto_dict = perspective_node_dto_instance.to_dict()
# create an instance of PerspectiveNodeDTO from a dict
perspective_node_dto_from_dict = PerspectiveNodeDTO.from_dict(perspective_node_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


