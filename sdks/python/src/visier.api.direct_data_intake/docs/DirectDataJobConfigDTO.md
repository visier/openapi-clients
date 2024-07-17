# DirectDataJobConfigDTO

Whether the direct data intake job is a primary job or a supplemental job.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extend_objects** | **List[str]** | The target analytic objects to load using extension tables.  You can extend objects if the job type is supplemental and the target objects already contain data from a previous data version.  This allows you to load data for objects that already contain data in Visier. | [optional] 
**supplemental_mode** | **str** | The configuration for the processing job as a primary job (default) or a supplemental job. If a primary job is already defined, the direct data   intake job must be supplemental. The valid values are &#x60;IS_PRIMARY&#x60;, &#x60;IS_SUPPLEMENTAL&#x60;, and &#x60;UNCHANGED&#x60;. | [optional] 

## Example

```python
from visier.api.direct_data_intake.models.direct_data_job_config_dto import DirectDataJobConfigDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DirectDataJobConfigDTO from a JSON string
direct_data_job_config_dto_instance = DirectDataJobConfigDTO.from_json(json)
# print the JSON string representation of the object
print(DirectDataJobConfigDTO.to_json())

# convert the object into a dict
direct_data_job_config_dto_dict = direct_data_job_config_dto_instance.to_dict()
# create an instance of DirectDataJobConfigDTO from a dict
direct_data_job_config_dto_from_dict = DirectDataJobConfigDTO.from_dict(direct_data_job_config_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


