# StartExtractionModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_tenants** | **bool** | If \&quot;true\&quot;, one extraction job is dispatched for each accessible analytic tenant. | [optional] 
**batch_size_override** | **int** | The maximum number of subjects the job can retrieve in each batch. | [optional] 
**connector_ids** | **List[str]** | The unique identifiers of the connectors to run extraction jobs. | [optional] 
**data_category_id** | **str** | The unique identifier of the data category on which to trigger the extraction job. Default is the tenant&#39;s primary data category. | [optional] 
**disable_artifact_generation** | **bool** | If \&quot;true\&quot;, the job does not generate data load artifacts. If unspecified, the default is \&quot;false\&quot;. | [optional] 
**extract_to_time_override** | **str** | An epoch timestamp in milliseconds for the end time up to which to retrieve data. | [optional] 
**last_extraction_time_offset_weeks** | **int** | The number of weeks in the past to retrieve data. This overrides the last extraction date to retrieve more data. | [optional] 
**months_to_extract** | **int** | The number of months to retrieve snapshot data. | [optional] 
**override_last_extraction_timestamp** | **str** | The time from which to extract data. | [optional] 
**publish_data_load_artifacts** | **bool** | If \&quot;true\&quot;, the generated data load artifacts are published to Production immediately. | [optional] 
**run_processing_job** | **bool** | If \&quot;true\&quot;, a processing job is spawned after a dispatched extraction job runs successfully. | [optional] 
**sql_batch_size** | **int** | The maximum amount of SQL table records the job can retrieve in each batch. | [optional] 
**tenants** | **List[str]** | A list of analytic tenants to dispatch extraction jobs for. One extraction job is dispatched per tenant. | [optional] 

## Example

```python
from visier.api.data_handling.models.start_extraction_model import StartExtractionModel

# TODO update the JSON string below
json = "{}"
# create an instance of StartExtractionModel from a JSON string
start_extraction_model_instance = StartExtractionModel.from_json(json)
# print the JSON string representation of the object
print(StartExtractionModel.to_json())

# convert the object into a dict
start_extraction_model_dict = start_extraction_model_instance.to_dict()
# create an instance of StartExtractionModel from a dict
start_extraction_model_from_dict = StartExtractionModel.from_dict(start_extraction_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


