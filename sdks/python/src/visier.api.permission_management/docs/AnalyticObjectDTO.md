# AnalyticObjectDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analytic_object_id** | **str** | The unique ID of the analytic object. | [optional] 
**display_name** | **str** | An identifiable name to display in Visier, such as \&quot;Employee\&quot;. | [optional] 
**object_type** | **str** | The analytic object type. | [optional] 
**related_objects** | [**List[RelatedAnalyticObjectDTO]**](RelatedAnalyticObjectDTO.md) | The analytic objects related to the data security object. | [optional] 
**securable_dimensions** | [**List[SecurableDimensionDTO]**](SecurableDimensionDTO.md) | A list of dimensions that are available to define population access filters in the permission. | [optional] 
**securable_properties** | [**List[SecurablePropertyDTO]**](SecurablePropertyDTO.md) | All available properties from the data security object and its related analytic objects that you can configure data access for. | [optional] 

## Example

```python
from visier.api.permission_management.models.analytic_object_dto import AnalyticObjectDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticObjectDTO from a JSON string
analytic_object_dto_instance = AnalyticObjectDTO.from_json(json)
# print the JSON string representation of the object
print(AnalyticObjectDTO.to_json())

# convert the object into a dict
analytic_object_dto_dict = analytic_object_dto_instance.to_dict()
# create an instance of AnalyticObjectDTO from a dict
analytic_object_dto_from_dict = AnalyticObjectDTO.from_dict(analytic_object_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


