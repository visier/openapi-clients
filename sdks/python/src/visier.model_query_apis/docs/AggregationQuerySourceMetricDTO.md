# AggregationQuerySourceMetricDTO

The column definition for a single metric within a `metrics` query.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_name** | **str** | The column name in the CSV file. Default is to use id as the column name. | [optional] 
**formula** | **str** | An ad-hoc metric formula. The response returns the results of the aggregate.  See the formula dictionary in Visier to find functions and objects you can use in a formula. | [optional] 
**id** | **str** | The unique ID of the metric. Note: See &#x60;Metrics&#x60; to get the ID.  If columnName is omitted, id is the column name in the CSV file. | [optional] 
**qualifying_path** | **str** | The base qualifying path to prefix the axes and filters&#39; qualifying paths with.  You must specify the qualifying path on a metric if the convergent analytic object of the metric doesn&#39;t match the  starting object in the qualifying paths of the axes and filters.   For example, consider a multi-metric query that contains metrics that count the number of applicants and requisitions,  grouped by the country of the recruiter&#39;s direct manager. The following sample shows how to use qualifyingPath to specify  the object reference traversal path from each metric&#39;s convergent analytic object to the start of the path for the axes.  In this example, there is only one convergent analytic object.  &#x60;&#x60;&#x60;  \&quot;source\&quot;: {      \&quot;metrics\&quot;: {         \&quot;columns\&quot;: [             {                 \&quot;id\&quot;: \&quot;employeeCount\&quot;             },             {                 \&quot;id\&quot;: \&quot;applicantCount\&quot;,                 \&quot;qualifyingPath\&quot;: \&quot;Applicant.Requisition.Recruiter\&quot;             },             {                 \&quot;id\&quot;: \&quot;requisitionCount\&quot;,                 \&quot;qualifyingPath\&quot;: \&quot;Requisition.Recruiter\&quot;             }         ]     }  },  \&quot;axes\&quot;: [     {         \&quot;dimensionLevelSelection\&quot;: {             \&quot;dimension\&quot;: {                 \&quot;name\&quot;: \&quot;Location\&quot;,                 \&quot;qualifyingPath\&quot;: \&quot;Employee.Direct_Manager\&quot;             },             \&quot;levelIds\&quot;: [                 \&quot;Location_1\&quot;             ]         }     }  ]  &#x60;&#x60;&#x60;  **Note:**  * &#x60;employeeCount&#x60; doesn&#39;t need a &#x60;qualifyingPath&#x60; because it&#39;s already convergent with the start of the axis path.  * The metrics&#39; qualifying paths must provide the reference name that resolves to the first object of the axis&#39; qualifying path as their last path segment. In this case, Recruiter is a named reference pointing to Employee. The final qualifying paths for the metrics are:      * &#x60;employeeCount&#x60;: Employee.Direct_Manager      * &#x60;applicantCount&#x60;: Applicant.Requisition.Recruiter.Direct_Manager      * &#x60;requisitionCount&#x60;: Requisition.Recruiter.Direct_Manager | [optional] 

## Example

```python
from visier.model_query_apis.models.aggregation_query_source_metric_dto import AggregationQuerySourceMetricDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AggregationQuerySourceMetricDTO from a JSON string
aggregation_query_source_metric_dto_instance = AggregationQuerySourceMetricDTO.from_json(json)
# print the JSON string representation of the object
print(AggregationQuerySourceMetricDTO.to_json())

# convert the object into a dict
aggregation_query_source_metric_dto_dict = aggregation_query_source_metric_dto_instance.to_dict()
# create an instance of AggregationQuerySourceMetricDTO from a dict
aggregation_query_source_metric_dto_from_dict = AggregationQuerySourceMetricDTO.from_dict(aggregation_query_source_metric_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


