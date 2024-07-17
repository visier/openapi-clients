# SuccessFactorsAuthParamsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **str** |  | [optional] 
**host_domain_name** | **str** |  | [optional] 
**o_auth** | [**SuccessFactorsOAuthParamsDTO**](SuccessFactorsOAuthParamsDTO.md) |  | [optional] 
**password** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from visier.api.data_handling.models.success_factors_auth_params_dto import SuccessFactorsAuthParamsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessFactorsAuthParamsDTO from a JSON string
success_factors_auth_params_dto_instance = SuccessFactorsAuthParamsDTO.from_json(json)
# print the JSON string representation of the object
print(SuccessFactorsAuthParamsDTO.to_json())

# convert the object into a dict
success_factors_auth_params_dto_dict = success_factors_auth_params_dto_instance.to_dict()
# create an instance of SuccessFactorsAuthParamsDTO from a dict
success_factors_auth_params_dto_from_dict = SuccessFactorsAuthParamsDTO.from_dict(success_factors_auth_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


