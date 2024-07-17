# DayforceV2AuthParamsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **str** |  | [optional] 
**host_domain_name** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**token_host** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from visier.api.data_handling.models.dayforce_v2_auth_params_dto import DayforceV2AuthParamsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DayforceV2AuthParamsDTO from a JSON string
dayforce_v2_auth_params_dto_instance = DayforceV2AuthParamsDTO.from_json(json)
# print the JSON string representation of the object
print(DayforceV2AuthParamsDTO.to_json())

# convert the object into a dict
dayforce_v2_auth_params_dto_dict = dayforce_v2_auth_params_dto_instance.to_dict()
# create an instance of DayforceV2AuthParamsDTO from a dict
dayforce_v2_auth_params_dto_from_dict = DayforceV2AuthParamsDTO.from_dict(dayforce_v2_auth_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


