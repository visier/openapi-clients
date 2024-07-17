# FusionAuthParamsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_domain_name** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from visier.api.data_handling.models.fusion_auth_params_dto import FusionAuthParamsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of FusionAuthParamsDTO from a JSON string
fusion_auth_params_dto_instance = FusionAuthParamsDTO.from_json(json)
# print the JSON string representation of the object
print(FusionAuthParamsDTO.to_json())

# convert the object into a dict
fusion_auth_params_dto_dict = fusion_auth_params_dto_instance.to_dict()
# create an instance of FusionAuthParamsDTO from a dict
fusion_auth_params_dto_from_dict = FusionAuthParamsDTO.from_dict(fusion_auth_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


