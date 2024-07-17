# SnowflakeAuthParamsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_identifier** | **str** |  | [optional] 
**database** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**private_key** | **str** |  | [optional] 
**var_schema** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**warehouse** | **str** |  | [optional] 

## Example

```python
from visier.api.data_handling.models.snowflake_auth_params_dto import SnowflakeAuthParamsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SnowflakeAuthParamsDTO from a JSON string
snowflake_auth_params_dto_instance = SnowflakeAuthParamsDTO.from_json(json)
# print the JSON string representation of the object
print(SnowflakeAuthParamsDTO.to_json())

# convert the object into a dict
snowflake_auth_params_dto_dict = snowflake_auth_params_dto_instance.to_dict()
# create an instance of SnowflakeAuthParamsDTO from a dict
snowflake_auth_params_dto_from_dict = SnowflakeAuthParamsDTO.from_dict(snowflake_auth_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


