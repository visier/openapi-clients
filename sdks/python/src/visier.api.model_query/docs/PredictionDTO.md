# PredictionDTO

A prediction is a forecast of future events with advanced machine learning models.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_end_date** | **str** | The date from which data is no longer available for this prediction.  Note: Format is the number of milliseconds since midnight 01 January, 1970 UTC as a string.  Epochs are expressed as 64-bit integers and represented as stringified longs in JSON due to JSON&#39;s inherent  limitation in representing large numbers. | [optional] 
**data_start_date** | **str** | The date from which data becomes available for this prediction.  Note: Format is the number of milliseconds since midnight 01 January, 1970 UTC as a string.  Epochs are expressed as 64-bit integers and represented as stringified longs in JSON due to JSON&#39;s inherent  limitation in representing large numbers. | [optional] 
**description** | **str** | The localized description of the prediction. | [optional] 
**display_name** | **str** | The localized display name of the prediction. | [optional] 
**event** | **str** | The object name of the event to predict. The prediction&#39;s training data uses past occurrences of the event to  make predictions. For example, the Predicted Risk of Resignation model uses the Employee_Exit event to estimate  likelihood of exit from the organization. | [optional] 
**event_filter** | **str** | The object name of a selection concept to filter event occurrences in the prediction&#39;s training data. | [optional] 
**factor_concepts** | **List[str]** | The list of unique IDs of the concepts used as prediction factors. | [optional] 
**factor_dimensions** | **List[str]** | The list of unique IDs of the dimensions used as prediction factors. | [optional] 
**factor_properties** | **List[str]** | The list of unique IDs of the properties used as prediction factors.  Note: Factors are conditions used as part of a Visier prediction. For example, Compensation might be a factor in  predicting an individual&#39;s risk of resignation. Factors are chosen based on:  - Availability in tenants.  - Prediction impact, such as salary.  - Reducing bias. | [optional] 
**factors_name** | **str** | The unique name of the factor property. The prediction&#39;s formula references the factor property as an object. This is automatically generated. | [optional] 
**id** | **str** | The unique ID of the prediction.  Note: See &#x60;Predictions&#x60; to get the ID. | [optional] 
**is_multi_tenant** | **bool** | If &#x60;true&#x60;, this prediction applies to more than one tenant. If \&quot;false\&quot;, the prediction only applies to the current tenant. | [optional] 
**label_property** | **str** | The unique ID of the property label for the prediction. This is automatically generated. | [optional] 
**minimum_training_months** | **str** | The minimum amount of time, in months, to train the prediction model. | [optional] 
**score_name** | **str** | The unique name of the score property.  The prediction&#39;s formula references the score property as an object. This is automatically generated. | [optional] 
**subject** | **str** | The object name of the subject that the prediction applies to. For example, Employee. | [optional] 
**subject_filter** | **str** | The object name of a selection concept to filter the subject population. Filtering the population selects  specific subject members in the prediction&#39;s training data. For example, using the isHighPerformer concept will  filter the prediction to only high performing employees. | [optional] 
**subject_key** | **str** | The unique ID of the subject&#39;s property that the prediction applies to. For example, Employee.EmployeeID. | [optional] 
**subject_parent_key** | **str** | The unique ID of the reference that connects a subject member to other members. For example, Employee.Direct_Manager.  Note: The &#x60;subjectParentKey&#x60; defines parent, child, and peer relationships between subject members. | [optional] 

## Example

```python
from visier.api.model_query.models.prediction_dto import PredictionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PredictionDTO from a JSON string
prediction_dto_instance = PredictionDTO.from_json(json)
# print the JSON string representation of the object
print(PredictionDTO.to_json())

# convert the object into a dict
prediction_dto_dict = prediction_dto_instance.to_dict()
# create an instance of PredictionDTO from a dict
prediction_dto_from_dict = PredictionDTO.from_dict(prediction_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


