# WorkdayAuthParamsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** |  | [optional] 
**domain_name** | **str** |  | [optional] 
**implementation_name** | **str** |  | [optional] 
**integration_system_id** | **str** |  | [optional] 
**o_auth** | [**WorkdayOAuthParamsDTO**](WorkdayOAuthParamsDTO.md) |  | [optional] 
**password** | **str** |  | [optional] 
**ref_token** | [**WorkdayRefreshTokenParamsDTO**](WorkdayRefreshTokenParamsDTO.md) |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from visier.api.data_handling.models.workday_auth_params_dto import WorkdayAuthParamsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of WorkdayAuthParamsDTO from a JSON string
workday_auth_params_dto_instance = WorkdayAuthParamsDTO.from_json(json)
# print the JSON string representation of the object
print(WorkdayAuthParamsDTO.to_json())

# convert the object into a dict
workday_auth_params_dto_dict = workday_auth_params_dto_instance.to_dict()
# create an instance of WorkdayAuthParamsDTO from a dict
workday_auth_params_dto_from_dict = WorkdayAuthParamsDTO.from_dict(workday_auth_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


