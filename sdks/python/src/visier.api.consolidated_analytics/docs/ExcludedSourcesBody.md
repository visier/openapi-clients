# ExcludedSourcesBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**excluded_sources** | **List[str]** | A list of a CA tenant&#39;s excluded sources. | [optional] 

## Example

```python
from visier.api.consolidated_analytics.models.excluded_sources_body import ExcludedSourcesBody

# TODO update the JSON string below
json = "{}"
# create an instance of ExcludedSourcesBody from a JSON string
excluded_sources_body_instance = ExcludedSourcesBody.from_json(json)
# print the JSON string representation of the object
print(ExcludedSourcesBody.to_json())

# convert the object into a dict
excluded_sources_body_dict = excluded_sources_body_instance.to_dict()
# create an instance of ExcludedSourcesBody from a dict
excluded_sources_body_from_dict = ExcludedSourcesBody.from_dict(excluded_sources_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


