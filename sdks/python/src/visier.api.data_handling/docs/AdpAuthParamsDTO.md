# AdpAuthParamsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_code** | **str** |  | [optional] 

## Example

```python
from visier.api.data_handling.models.adp_auth_params_dto import AdpAuthParamsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AdpAuthParamsDTO from a JSON string
adp_auth_params_dto_instance = AdpAuthParamsDTO.from_json(json)
# print the JSON string representation of the object
print(AdpAuthParamsDTO.to_json())

# convert the object into a dict
adp_auth_params_dto_dict = adp_auth_params_dto_instance.to_dict()
# create an instance of AdpAuthParamsDTO from a dict
adp_auth_params_dto_from_dict = AdpAuthParamsDTO.from_dict(adp_auth_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


