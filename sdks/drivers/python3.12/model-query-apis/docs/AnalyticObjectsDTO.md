# AnalyticObjectsDTO

A collection of analytic objects

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analytic_objects** | [**List[AnalyticObjectDTO]**](AnalyticObjectDTO.md) |  | [optional] 

## Example

```python
from visier.model_query.models.analytic_objects_dto import AnalyticObjectsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticObjectsDTO from a JSON string
analytic_objects_dto_instance = AnalyticObjectsDTO.from_json(json)
# print the JSON string representation of the object
print(AnalyticObjectsDTO.to_json())

# convert the object into a dict
analytic_objects_dto_dict = analytic_objects_dto_instance.to_dict()
# create an instance of AnalyticObjectsDTO from a dict
analytic_objects_dto_from_dict = AnalyticObjectsDTO.from_dict(analytic_objects_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


