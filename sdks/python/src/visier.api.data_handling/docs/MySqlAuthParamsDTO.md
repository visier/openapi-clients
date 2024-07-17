# MySqlAuthParamsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database** | **str** |  | [optional] 
**host** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**port** | **str** |  | [optional] 
**ssl_mode** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from visier.api.data_handling.models.my_sql_auth_params_dto import MySqlAuthParamsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MySqlAuthParamsDTO from a JSON string
my_sql_auth_params_dto_instance = MySqlAuthParamsDTO.from_json(json)
# print the JSON string representation of the object
print(MySqlAuthParamsDTO.to_json())

# convert the object into a dict
my_sql_auth_params_dto_dict = my_sql_auth_params_dto_instance.to_dict()
# create an instance of MySqlAuthParamsDTO from a dict
my_sql_auth_params_dto_from_dict = MySqlAuthParamsDTO.from_dict(my_sql_auth_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


