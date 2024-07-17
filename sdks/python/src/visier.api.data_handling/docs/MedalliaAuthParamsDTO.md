# MedalliaAuthParamsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**instance_url** | **str** |  | [optional] 
**tenant_domain_name** | **str** |  | [optional] 

## Example

```python
from visier.api.data_handling.models.medallia_auth_params_dto import MedalliaAuthParamsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MedalliaAuthParamsDTO from a JSON string
medallia_auth_params_dto_instance = MedalliaAuthParamsDTO.from_json(json)
# print the JSON string representation of the object
print(MedalliaAuthParamsDTO.to_json())

# convert the object into a dict
medallia_auth_params_dto_dict = medallia_auth_params_dto_instance.to_dict()
# create an instance of MedalliaAuthParamsDTO from a dict
medallia_auth_params_dto_from_dict = MedalliaAuthParamsDTO.from_dict(medallia_auth_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


