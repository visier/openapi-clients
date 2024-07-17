# RedshiftAuthParamsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database** | **str** |  | [optional] 
**endpoint** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**port** | **str** |  | [optional] 
**var_schema** | **str** |  | [optional] 
**table_prefix** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from visier.api.data_handling.models.redshift_auth_params_dto import RedshiftAuthParamsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of RedshiftAuthParamsDTO from a JSON string
redshift_auth_params_dto_instance = RedshiftAuthParamsDTO.from_json(json)
# print the JSON string representation of the object
print(RedshiftAuthParamsDTO.to_json())

# convert the object into a dict
redshift_auth_params_dto_dict = redshift_auth_params_dto_instance.to_dict()
# create an instance of RedshiftAuthParamsDTO from a dict
redshift_auth_params_dto_from_dict = RedshiftAuthParamsDTO.from_dict(redshift_auth_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


