# GreenhouseAuthParamsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** |  | [optional] 

## Example

```python
from visier.api.data_handling.models.greenhouse_auth_params_dto import GreenhouseAuthParamsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of GreenhouseAuthParamsDTO from a JSON string
greenhouse_auth_params_dto_instance = GreenhouseAuthParamsDTO.from_json(json)
# print the JSON string representation of the object
print(GreenhouseAuthParamsDTO.to_json())

# convert the object into a dict
greenhouse_auth_params_dto_dict = greenhouse_auth_params_dto_instance.to_dict()
# create an instance of GreenhouseAuthParamsDTO from a dict
greenhouse_auth_params_dto_from_dict = GreenhouseAuthParamsDTO.from_dict(greenhouse_auth_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


