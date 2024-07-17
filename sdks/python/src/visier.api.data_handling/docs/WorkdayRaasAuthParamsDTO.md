# WorkdayRaasAuthParamsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_name** | **str** |  | [optional] 
**implementation_name** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**test_report_url** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from visier.api.data_handling.models.workday_raas_auth_params_dto import WorkdayRaasAuthParamsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of WorkdayRaasAuthParamsDTO from a JSON string
workday_raas_auth_params_dto_instance = WorkdayRaasAuthParamsDTO.from_json(json)
# print the JSON string representation of the object
print(WorkdayRaasAuthParamsDTO.to_json())

# convert the object into a dict
workday_raas_auth_params_dto_dict = workday_raas_auth_params_dto_instance.to_dict()
# create an instance of WorkdayRaasAuthParamsDTO from a dict
workday_raas_auth_params_dto_from_dict = WorkdayRaasAuthParamsDTO.from_dict(workday_raas_auth_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


