# QueryAxisOptionsDTO

QueryAxisOptions allows you to customize an axis in the query, such as changing the display mode for its cell set values or providing a custom column name.  Only available when the Accept header is a table format, such as text/csv or application/jsonlines.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_display_mode** | **int** | Options to override the display mode for the axis. This overrides the query-level &#x60;memberDisplayMode&#x60; options value in the query.  Only available for non-time axes. Use the QueryAxisMemberDisplayMode &#x60;memberDisplayMode&#x60; to apply different display modes to different axes.  For example, let&#39;s say your query has the &#x60;memberDisplayMode&#x60; as &#x60;DISPLAY&#x60; but you want to fetch the object name for a specific dimension.  With QueryAxisMemberDisplayMode &#x60;memberDisplayMode&#x60;, you can override that dimension&#39;s &#x60;memberDisplayMode&#x60; to &#x60;DEFAULT&#x60; instead of &#x60;DISPLAY&#x60;.   Valid values are &#x60;UNCHANGED&#x60;, &#x60;DEFAULT&#x60;, &#x60;COMPACT&#x60;, &#x60;DISPLAY&#x60;, or &#x60;MDX&#x60;. Default is &#x60;UNCHANGED&#x60;. | [optional] 
**column_name** | **str** | If specified, returns the column name of the axis in the response. | [optional] 

## Example

```python
from visier.model_query.models.query_axis_options_dto import QueryAxisOptionsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of QueryAxisOptionsDTO from a JSON string
query_axis_options_dto_instance = QueryAxisOptionsDTO.from_json(json)
# print the JSON string representation of the object
print(QueryAxisOptionsDTO.to_json())

# convert the object into a dict
query_axis_options_dto_dict = query_axis_options_dto_instance.to_dict()
# create an instance of QueryAxisOptionsDTO from a dict
query_axis_options_dto_from_dict = QueryAxisOptionsDTO.from_dict(query_axis_options_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


