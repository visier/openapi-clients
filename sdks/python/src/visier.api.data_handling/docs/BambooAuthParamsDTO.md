# BambooAuthParamsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | **str** |  | [optional] 
**tenant_domain_name** | **str** |  | [optional] 

## Example

```python
from visier.api.data_handling.models.bamboo_auth_params_dto import BambooAuthParamsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of BambooAuthParamsDTO from a JSON string
bamboo_auth_params_dto_instance = BambooAuthParamsDTO.from_json(json)
# print the JSON string representation of the object
print(BambooAuthParamsDTO.to_json())

# convert the object into a dict
bamboo_auth_params_dto_dict = bamboo_auth_params_dto_instance.to_dict()
# create an instance of BambooAuthParamsDTO from a dict
bamboo_auth_params_dto_from_dict = BambooAuthParamsDTO.from_dict(bamboo_auth_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


