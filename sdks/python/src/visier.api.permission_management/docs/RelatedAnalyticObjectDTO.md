# RelatedAnalyticObjectDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analytic_object_id** | **str** | The analytic object ID. | [optional] 
**display_name** | **str** | An identifiable analytic object name to display in Visier, such as \&quot;Recognition\&quot;. | [optional] 

## Example

```python
from visier.api.permission_management.models.related_analytic_object_dto import RelatedAnalyticObjectDTO

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedAnalyticObjectDTO from a JSON string
related_analytic_object_dto_instance = RelatedAnalyticObjectDTO.from_json(json)
# print the JSON string representation of the object
print(RelatedAnalyticObjectDTO.to_json())

# convert the object into a dict
related_analytic_object_dto_dict = related_analytic_object_dto_instance.to_dict()
# create an instance of RelatedAnalyticObjectDTO from a dict
related_analytic_object_dto_from_dict = RelatedAnalyticObjectDTO.from_dict(related_analytic_object_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


