# NamelyAuthParamsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_code** | **str** |  | [optional] 

## Example

```python
from visier.api.data_handling.models.namely_auth_params_dto import NamelyAuthParamsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of NamelyAuthParamsDTO from a JSON string
namely_auth_params_dto_instance = NamelyAuthParamsDTO.from_json(json)
# print the JSON string representation of the object
print(NamelyAuthParamsDTO.to_json())

# convert the object into a dict
namely_auth_params_dto_dict = namely_auth_params_dto_instance.to_dict()
# create an instance of NamelyAuthParamsDTO from a dict
namely_auth_params_dto_from_dict = NamelyAuthParamsDTO.from_dict(namely_auth_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


