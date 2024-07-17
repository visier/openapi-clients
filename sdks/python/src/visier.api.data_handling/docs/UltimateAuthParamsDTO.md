# UltimateAuthParamsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** |  | [optional] 
**host_domain_name** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**user_access_key** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from visier.api.data_handling.models.ultimate_auth_params_dto import UltimateAuthParamsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UltimateAuthParamsDTO from a JSON string
ultimate_auth_params_dto_instance = UltimateAuthParamsDTO.from_json(json)
# print the JSON string representation of the object
print(UltimateAuthParamsDTO.to_json())

# convert the object into a dict
ultimate_auth_params_dto_dict = ultimate_auth_params_dto_instance.to_dict()
# create an instance of UltimateAuthParamsDTO from a dict
ultimate_auth_params_dto_from_dict = UltimateAuthParamsDTO.from_dict(ultimate_auth_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


