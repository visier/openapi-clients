# WorkdayOAuthParamsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_client_id** | **str** |  | [optional] 
**private_x509_key** | **str** |  | [optional] 
**public_x509_cert** | **str** |  | [optional] 

## Example

```python
from visier.api.data_handling.models.workday_o_auth_params_dto import WorkdayOAuthParamsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of WorkdayOAuthParamsDTO from a JSON string
workday_o_auth_params_dto_instance = WorkdayOAuthParamsDTO.from_json(json)
# print the JSON string representation of the object
print(WorkdayOAuthParamsDTO.to_json())

# convert the object into a dict
workday_o_auth_params_dto_dict = workday_o_auth_params_dto_instance.to_dict()
# create an instance of WorkdayOAuthParamsDTO from a dict
workday_o_auth_params_dto_from_dict = WorkdayOAuthParamsDTO.from_dict(workday_o_auth_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


