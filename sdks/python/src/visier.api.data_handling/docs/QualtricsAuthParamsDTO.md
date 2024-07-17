# QualtricsAuthParamsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_token** | **str** |  | [optional] 
**data_center_id** | **str** |  | [optional] 

## Example

```python
from visier.api.data_handling.models.qualtrics_auth_params_dto import QualtricsAuthParamsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of QualtricsAuthParamsDTO from a JSON string
qualtrics_auth_params_dto_instance = QualtricsAuthParamsDTO.from_json(json)
# print the JSON string representation of the object
print(QualtricsAuthParamsDTO.to_json())

# convert the object into a dict
qualtrics_auth_params_dto_dict = qualtrics_auth_params_dto_instance.to_dict()
# create an instance of QualtricsAuthParamsDTO from a dict
qualtrics_auth_params_dto_from_dict = QualtricsAuthParamsDTO.from_dict(qualtrics_auth_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


