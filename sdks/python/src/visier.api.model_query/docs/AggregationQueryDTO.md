# AggregationQueryDTO

An AggregationQuery defines the data to query in an aggregation query and returns a `cell set` calculated from  the selected data points.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**axes** | [**List[QueryAxisDTO]**](QueryAxisDTO.md) | The objects by which to group the query. An axis defines the groups that the data belongs to.  Omit &#x60;axes&#x60; if no grouping is required. | [optional] 
**filters** | [**List[QueryFilterDTO]**](QueryFilterDTO.md) | The objects by which to filter the query, such as dimensions or concepts.  A filter defines the population to retrieve data from. Omit &#x60;filters&#x60; if no filtering is required. | [optional] 
**parameter_values** | [**List[QueryParameterValueDTO]**](QueryParameterValueDTO.md) | The values associated with parameters, if defined. | [optional] 
**source** | [**AggregationQuerySourceDTO**](AggregationQuerySourceDTO.md) | The source data, such as a metric or formula, to query. | [optional] 
**time_intervals** | [**QueryTimeIntervalsDTO**](QueryTimeIntervalsDTO.md) | The time intervals to query. | [optional] 

## Example

```python
from visier.api.model_query.models.aggregation_query_dto import AggregationQueryDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AggregationQueryDTO from a JSON string
aggregation_query_dto_instance = AggregationQueryDTO.from_json(json)
# print the JSON string representation of the object
print(AggregationQueryDTO.to_json())

# convert the object into a dict
aggregation_query_dto_dict = aggregation_query_dto_instance.to_dict()
# create an instance of AggregationQueryDTO from a dict
aggregation_query_dto_from_dict = AggregationQueryDTO.from_dict(aggregation_query_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


