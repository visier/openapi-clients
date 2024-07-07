# PredictionsDTO

A collection of predictions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**predictions** | [**List[PredictionDTO]**](PredictionDTO.md) |  | [optional] 

## Example

```python
from visier.model_query.models.predictions_dto import PredictionsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PredictionsDTO from a JSON string
predictions_dto_instance = PredictionsDTO.from_json(json)
# print the JSON string representation of the object
print(PredictionsDTO.to_json())

# convert the object into a dict
predictions_dto_dict = predictions_dto_instance.to_dict()
# create an instance of PredictionsDTO from a dict
predictions_dto_from_dict = PredictionsDTO.from_dict(predictions_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


