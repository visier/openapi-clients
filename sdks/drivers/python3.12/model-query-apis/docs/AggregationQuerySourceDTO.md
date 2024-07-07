# AggregationQuerySourceDTO

An AggregationQuerySource defines the source data to query in an aggregation query.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**formula** | **str** | An ad-hoc metric formula. The response returns the results of the aggregate.  See the formula dictionary in Visier to find functions and objects you can use in a formula. | [optional] 
**metric** | **str** | The ID of an existing metric in your Visier solution. See &#x60;Metrics&#x60; to get the ID. | [optional] 
**metrics** | [**AggregationQuerySourceMetricsDTO**](AggregationQuerySourceMetricsDTO.md) | The IDs of metrics to aggregate. All metrics in the query must reference the same analytic object.  For example, you cannot query Headcount and Applicant Count because one uses the Employee subject and  the other uses the Applicant subject. You can query Headcount and Employee Count for Women because both  reference the Employee subject. Only available when the Accept header is text/csv. For more information,  see &#x60;Aggregate&#x60;. | [optional] 

## Example

```python
from visier.model_query.models.aggregation_query_source_dto import AggregationQuerySourceDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AggregationQuerySourceDTO from a JSON string
aggregation_query_source_dto_instance = AggregationQuerySourceDTO.from_json(json)
# print the JSON string representation of the object
print(AggregationQuerySourceDTO.to_json())

# convert the object into a dict
aggregation_query_source_dto_dict = aggregation_query_source_dto_instance.to_dict()
# create an instance of AggregationQuerySourceDTO from a dict
aggregation_query_source_dto_from_dict = AggregationQuerySourceDTO.from_dict(aggregation_query_source_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


