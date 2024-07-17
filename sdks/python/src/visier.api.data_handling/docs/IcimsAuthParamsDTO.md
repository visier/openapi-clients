# IcimsAuthParamsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from visier.api.data_handling.models.icims_auth_params_dto import IcimsAuthParamsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of IcimsAuthParamsDTO from a JSON string
icims_auth_params_dto_instance = IcimsAuthParamsDTO.from_json(json)
# print the JSON string representation of the object
print(IcimsAuthParamsDTO.to_json())

# convert the object into a dict
icims_auth_params_dto_dict = icims_auth_params_dto_instance.to_dict()
# create an instance of IcimsAuthParamsDTO from a dict
icims_auth_params_dto_from_dict = IcimsAuthParamsDTO.from_dict(icims_auth_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


