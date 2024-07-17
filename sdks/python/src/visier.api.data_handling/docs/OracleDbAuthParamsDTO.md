# OracleDbAuthParamsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**port** | **str** |  | [optional] 
**service_name** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from visier.api.data_handling.models.oracle_db_auth_params_dto import OracleDbAuthParamsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of OracleDbAuthParamsDTO from a JSON string
oracle_db_auth_params_dto_instance = OracleDbAuthParamsDTO.from_json(json)
# print the JSON string representation of the object
print(OracleDbAuthParamsDTO.to_json())

# convert the object into a dict
oracle_db_auth_params_dto_dict = oracle_db_auth_params_dto_instance.to_dict()
# create an instance of OracleDbAuthParamsDTO from a dict
oracle_db_auth_params_dto_from_dict = OracleDbAuthParamsDTO.from_dict(oracle_db_auth_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


