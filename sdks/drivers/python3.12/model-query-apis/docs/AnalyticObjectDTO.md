# AnalyticObjectDTO

Analytic objects are the various items that users can analyze in Visier. Analytic objects include subjects, events, and overlays.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the analytic object.  Note: See &#x60;AnalyticObjects&#x60; to get the ID. | [optional] 
**display_name** | **str** | The localized display name of the analytic object. | [optional] 
**description** | **str** | The localized description of the analytic object. | [optional] 
**type** | **str** | The analytic object type: SUBJECT, EVENT, or OVERLAY. | [optional] 
**data_start_date** | **str** | The date from which data becomes available for this analytic object.  Note: Format is the number of milliseconds since midnight 01 January, 1970 UTC as a string.  Epochs are expressed as 64-bit integers and represented as stringified longs in JSON due to JSON&#39;s inherent  limitation in representing large numbers. | [optional] 
**data_end_date** | **str** | The date from which data is no longer available for this analytic object.  Note: Format is the number of milliseconds since midnight 01 January, 1970 UTC as a string.  Epochs are expressed as 64-bit integers and represented as stringified longs in JSON due to JSON&#39;s inherent  limitation in representing large numbers. | [optional] 
**property_ids** | **List[str]** | A list of strings representing IDs of the properties that belong to this analytic object. | [optional] 
**dimension_ids** | **List[str]** | A list of strings representing IDs of the dimensions that belong to this analytic object. | [optional] 
**selection_concept_ids** | **List[str]** | A list of strings representing IDs of the selection concepts that belong to this analytic object.  Note: If there are no selection concepts, this field is omitted. | [optional] 
**object_references** | [**List[ObjectReferenceDTO]**](ObjectReferenceDTO.md) | A list of references from this analytic object to other analytic objects.  Note: If there are no references, this field is omitted. | [optional] 
**population_configuration** | [**PopulationConfigurationDTO**](PopulationConfigurationDTO.md) | A set of property and dimension references configured by Visier or an administrator to tell the platform what  properties and dimensions to use when doing population insight calculations. These are the distinguishing  properties, change history properties, and grouping dimensions to use in AI insights. This field is optional and  is only available for subjects. | [optional] 

## Example

```python
from visier.model_query.models.analytic_object_dto import AnalyticObjectDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticObjectDTO from a JSON string
analytic_object_dto_instance = AnalyticObjectDTO.from_json(json)
# print the JSON string representation of the object
print(AnalyticObjectDTO.to_json())

# convert the object into a dict
analytic_object_dto_dict = analytic_object_dto_instance.to_dict()
# create an instance of AnalyticObjectDTO from a dict
analytic_object_dto_from_dict = AnalyticObjectDTO.from_dict(analytic_object_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


