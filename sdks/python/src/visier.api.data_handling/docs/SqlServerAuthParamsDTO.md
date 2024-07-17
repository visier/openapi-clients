# SqlServerAuthParamsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database** | **str** |  | [optional] 
**host** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**port** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from visier.api.data_handling.models.sql_server_auth_params_dto import SqlServerAuthParamsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SqlServerAuthParamsDTO from a JSON string
sql_server_auth_params_dto_instance = SqlServerAuthParamsDTO.from_json(json)
# print the JSON string representation of the object
print(SqlServerAuthParamsDTO.to_json())

# convert the object into a dict
sql_server_auth_params_dto_dict = sql_server_auth_params_dto_instance.to_dict()
# create an instance of SqlServerAuthParamsDTO from a dict
sql_server_auth_params_dto_from_dict = SqlServerAuthParamsDTO.from_dict(sql_server_auth_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


