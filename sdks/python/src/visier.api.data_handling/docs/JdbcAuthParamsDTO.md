# JdbcAuthParamsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jdbc_connect_string** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from visier.api.data_handling.models.jdbc_auth_params_dto import JdbcAuthParamsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of JdbcAuthParamsDTO from a JSON string
jdbc_auth_params_dto_instance = JdbcAuthParamsDTO.from_json(json)
# print the JSON string representation of the object
print(JdbcAuthParamsDTO.to_json())

# convert the object into a dict
jdbc_auth_params_dto_dict = jdbc_auth_params_dto_instance.to_dict()
# create an instance of JdbcAuthParamsDTO from a dict
jdbc_auth_params_dto_from_dict = JdbcAuthParamsDTO.from_dict(jdbc_auth_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


