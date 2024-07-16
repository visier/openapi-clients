# QueryExecutionOptionsDTO

A QueryExecutionOptions provides additional instructions to perform a query.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**axis_visibility** | **str** | The amount of information to return about each axis. Default is SIMPLE. | [optional] 
**calendar_type** | **str** | The calendar type to use. This will be used for all time calculations unless explicitly overridden in  the calculation itself. Default is TENANT_CALENDAR. | [optional] 
**cell_distribution_options** | [**CellDistributionOptionsDTO**](CellDistributionOptionsDTO.md) |  | [optional] 
**currency_conversion_code** | **str** | The target currency for all currency conversions.  If not specified, the tenant default currency will be used. | [optional] 
**currency_conversion_date** | **str** | The currency conversion date to use. If defined, the currency conversion will use the exchange rates as of this date.  Default is the exchange rate at the end of the query time interval. Format is the number of milliseconds since  midnight 01 January, 1970 UTC as a string. Note: Epochs are expressed as 64-bit integers and represented as  stringified longs in JSON due to JSON&#39;s inherent limitation in representing large numbers. | [optional] 
**currency_conversion_mode** | **str** | The currency conversion mode to use. This will be used for all currency conversion calculations  unless explicitly overridden in the calculation itself. Default is TENANT_CURRENCY_CONVERSION. | [optional] 
**enable_descending_space** | **bool** | If true, filter non-time axis member sets to only include members that are in aggregate positions or whose previous position is a leaf | [optional] 
**enable_sparse_results** | **bool** | Retrieve sparse cell sets. Sparse results only retrieve non-zero and non-null cells. Whether a result is truly sparse  or not is determined by the Visier server. | [optional] 
**internal** | [**InternalQueryExecutionOptionsDTO**](InternalQueryExecutionOptionsDTO.md) |  | [optional] 
**lineage_depth** | **int** | The max number of levels of nesting to unwind when determining the lineage for a derived metric value. | [optional] 
**member_display_mode** | **str** | Define the &#x60;memberDisplayMode&#x60; options to control how member values are rendered in the aggregate query result set. You can override the &#x60;memberDisplayMode&#x60; on a per-axis basis, if required.   Valid values are &#x60;DEFAULT&#x60;, &#x60;COMPACT&#x60;, &#x60;DISPLAY&#x60;, or &#x60;MDX&#x60;. Default is &#x60;DEFAULT&#x60;.   * &#x60;DEFAULT&#x60;: The default member name representation. For non-time members, this means returning the technical member name path.    For time members, this includes a bracketed member index.    For example, Time instant member: &#x60;2019-06-01T00:00:00.000Z - [0]&#x60;    For example, Time interval member: &#x60;2022-06-01T00:00:00.000Z/2022-07-01T00:00:00.000Z - [12]&#x60;  * &#x60;COMPACT&#x60;: Compacts the time member name representation. This also transforms the representation of time intervals to the end time of the interval.     For example, Time instant member: &#x60;2019-06-01T00:00:00.000Z&#x60;     For example, Time interval member: &#x60;2022-07-01T00:00:00.000Z&#x60; where the interval member name was &#x60;2022-06-01T00:00:00.000Z/2022-07-01T00:00:00.000Z - [12]&#x60;  * &#x60;DISPLAY&#x60;: Emit the members&#39; display names whenever possible. When combined with &#x60;axisVisibility &#x3D; VERBOSE&#x60;, the full display name path will be emitted.  * &#x60;MDX&#x60;: Emit member name paths where each element is enclosed in square brackets, &#x60;[]&#x60;. Multidimensional expression (MDX) display mode automatically encloses time members in square brackets and puts them in &#x60;COMPACT&#x60; format.    For example, Location member &#x60;North America.United States.California&#x60; becomes &#x60;[North America].[United States].[California]&#x60; in MDX display mode.    For example, Time instant member &#x60;2019-06-01T00:00:00.000Z - [0]&#x60; becomes &#x60;[2019-06-01T00:00:00.000Z]&#x60; in MDX display mode. | [optional] 
**null_visibility** | **str** | Show or hide null or N/A values in the result. Default is SHOW. | [optional] 
**zero_visibility** | **str** | Show or hide zeros in the result. Default is SHOW. | [optional] 

## Example

```python
from visier.model_query_apis.models.query_execution_options_dto import QueryExecutionOptionsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of QueryExecutionOptionsDTO from a JSON string
query_execution_options_dto_instance = QueryExecutionOptionsDTO.from_json(json)
# print the JSON string representation of the object
print(QueryExecutionOptionsDTO.to_json())

# convert the object into a dict
query_execution_options_dto_dict = query_execution_options_dto_instance.to_dict()
# create an instance of QueryExecutionOptionsDTO from a dict
query_execution_options_dto_from_dict = QueryExecutionOptionsDTO.from_dict(query_execution_options_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


