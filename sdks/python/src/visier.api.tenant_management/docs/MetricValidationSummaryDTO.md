# MetricValidationSummaryDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | An identifiable name that is displayed within Visier. For example, \&quot;Headcount\&quot;. | [optional] 
**symbol_name** | **str** | The symbol name of the metric. For example, \&quot;employeeCount\&quot;. | [optional] 
**value** | **float** | The current value of the metric expressed as an integer. | [optional] 

## Example

```python
from visier.api.tenant_management.models.metric_validation_summary_dto import MetricValidationSummaryDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MetricValidationSummaryDTO from a JSON string
metric_validation_summary_dto_instance = MetricValidationSummaryDTO.from_json(json)
# print the JSON string representation of the object
print(MetricValidationSummaryDTO.to_json())

# convert the object into a dict
metric_validation_summary_dto_dict = metric_validation_summary_dto_instance.to_dict()
# create an instance of MetricValidationSummaryDTO from a dict
metric_validation_summary_dto_from_dict = MetricValidationSummaryDTO.from_dict(metric_validation_summary_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


