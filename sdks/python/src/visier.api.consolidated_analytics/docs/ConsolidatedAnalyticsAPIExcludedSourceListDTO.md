# ConsolidatedAnalyticsAPIExcludedSourceListDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**excluded_sources** | **List[str]** | A list of the CA tenant&#39;s excluded sources. | [optional] 

## Example

```python
from visier.api.consolidated_analytics.models.consolidated_analytics_api_excluded_source_list_dto import ConsolidatedAnalyticsAPIExcludedSourceListDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ConsolidatedAnalyticsAPIExcludedSourceListDTO from a JSON string
consolidated_analytics_api_excluded_source_list_dto_instance = ConsolidatedAnalyticsAPIExcludedSourceListDTO.from_json(json)
# print the JSON string representation of the object
print(ConsolidatedAnalyticsAPIExcludedSourceListDTO.to_json())

# convert the object into a dict
consolidated_analytics_api_excluded_source_list_dto_dict = consolidated_analytics_api_excluded_source_list_dto_instance.to_dict()
# create an instance of ConsolidatedAnalyticsAPIExcludedSourceListDTO from a dict
consolidated_analytics_api_excluded_source_list_dto_from_dict = ConsolidatedAnalyticsAPIExcludedSourceListDTO.from_dict(consolidated_analytics_api_excluded_source_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


