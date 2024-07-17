# SuccessFactorsOAuthParamsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** |  | [optional] 
**private_x509_key** | **str** |  | [optional] 
**public_x509_cert** | **str** |  | [optional] 

## Example

```python
from visier.api.data_handling.models.success_factors_o_auth_params_dto import SuccessFactorsOAuthParamsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessFactorsOAuthParamsDTO from a JSON string
success_factors_o_auth_params_dto_instance = SuccessFactorsOAuthParamsDTO.from_json(json)
# print the JSON string representation of the object
print(SuccessFactorsOAuthParamsDTO.to_json())

# convert the object into a dict
success_factors_o_auth_params_dto_dict = success_factors_o_auth_params_dto_instance.to_dict()
# create an instance of SuccessFactorsOAuthParamsDTO from a dict
success_factors_o_auth_params_dto_from_dict = SuccessFactorsOAuthParamsDTO.from_dict(success_factors_o_auth_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


