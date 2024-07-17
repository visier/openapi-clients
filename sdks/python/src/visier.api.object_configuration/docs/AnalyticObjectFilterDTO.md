# AnalyticObjectFilterDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analytic_object_uuid** | **str** | The UUID of the analytic object used in the selection concept. | [optional] 
**dimensions** | [**List[DimensionFilterDTO]**](DimensionFilterDTO.md) | A list of dimensions included in the concept. | [optional] 
**symbol_name** | **str** | The symbol name of the analytic object. | [optional] 

## Example

```python
from visier.api.object_configuration.models.analytic_object_filter_dto import AnalyticObjectFilterDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticObjectFilterDTO from a JSON string
analytic_object_filter_dto_instance = AnalyticObjectFilterDTO.from_json(json)
# print the JSON string representation of the object
print(AnalyticObjectFilterDTO.to_json())

# convert the object into a dict
analytic_object_filter_dto_dict = analytic_object_filter_dto_instance.to_dict()
# create an instance of AnalyticObjectFilterDTO from a dict
analytic_object_filter_dto_from_dict = AnalyticObjectFilterDTO.from_dict(analytic_object_filter_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


