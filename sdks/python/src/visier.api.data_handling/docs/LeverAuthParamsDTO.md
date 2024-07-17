# LeverAuthParamsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** |  | [optional] 

## Example

```python
from visier.api.data_handling.models.lever_auth_params_dto import LeverAuthParamsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of LeverAuthParamsDTO from a JSON string
lever_auth_params_dto_instance = LeverAuthParamsDTO.from_json(json)
# print the JSON string representation of the object
print(LeverAuthParamsDTO.to_json())

# convert the object into a dict
lever_auth_params_dto_dict = lever_auth_params_dto_instance.to_dict()
# create an instance of LeverAuthParamsDTO from a dict
lever_auth_params_dto_from_dict = LeverAuthParamsDTO.from_dict(lever_auth_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


