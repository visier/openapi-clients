# BigQueryAuthParamsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**dataset_location** | **str** |  | [optional] 
**default_dataset** | **str** |  | [optional] 
**project_id** | **str** |  | [optional] 
**refresh_token** | **str** |  | [optional] 
**service_account_params** | [**BigQueryServiceAccountParamsDTO**](BigQueryServiceAccountParamsDTO.md) |  | [optional] 

## Example

```python
from visier.api.data_handling.models.big_query_auth_params_dto import BigQueryAuthParamsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of BigQueryAuthParamsDTO from a JSON string
big_query_auth_params_dto_instance = BigQueryAuthParamsDTO.from_json(json)
# print the JSON string representation of the object
print(BigQueryAuthParamsDTO.to_json())

# convert the object into a dict
big_query_auth_params_dto_dict = big_query_auth_params_dto_instance.to_dict()
# create an instance of BigQueryAuthParamsDTO from a dict
big_query_auth_params_dto_from_dict = BigQueryAuthParamsDTO.from_dict(big_query_auth_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


