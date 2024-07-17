# BigQueryServiceAccountParamsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**private_key** | **str** |  | [optional] 
**service_account_email** | **str** |  | [optional] 

## Example

```python
from visier.api.data_handling.models.big_query_service_account_params_dto import BigQueryServiceAccountParamsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of BigQueryServiceAccountParamsDTO from a JSON string
big_query_service_account_params_dto_instance = BigQueryServiceAccountParamsDTO.from_json(json)
# print the JSON string representation of the object
print(BigQueryServiceAccountParamsDTO.to_json())

# convert the object into a dict
big_query_service_account_params_dto_dict = big_query_service_account_params_dto_instance.to_dict()
# create an instance of BigQueryServiceAccountParamsDTO from a dict
big_query_service_account_params_dto_from_dict = BigQueryServiceAccountParamsDTO.from_dict(big_query_service_account_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


