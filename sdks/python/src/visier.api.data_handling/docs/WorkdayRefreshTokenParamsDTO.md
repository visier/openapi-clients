# WorkdayRefreshTokenParamsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**refresh_token** | **str** |  | [optional] 

## Example

```python
from visier.api.data_handling.models.workday_refresh_token_params_dto import WorkdayRefreshTokenParamsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of WorkdayRefreshTokenParamsDTO from a JSON string
workday_refresh_token_params_dto_instance = WorkdayRefreshTokenParamsDTO.from_json(json)
# print the JSON string representation of the object
print(WorkdayRefreshTokenParamsDTO.to_json())

# convert the object into a dict
workday_refresh_token_params_dto_dict = workday_refresh_token_params_dto_instance.to_dict()
# create an instance of WorkdayRefreshTokenParamsDTO from a dict
workday_refresh_token_params_dto_from_dict = WorkdayRefreshTokenParamsDTO.from_dict(workday_refresh_token_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


