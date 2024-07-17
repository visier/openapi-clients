# GongAuthParamsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 

## Example

```python
from visier.api.data_handling.models.gong_auth_params_dto import GongAuthParamsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of GongAuthParamsDTO from a JSON string
gong_auth_params_dto_instance = GongAuthParamsDTO.from_json(json)
# print the JSON string representation of the object
print(GongAuthParamsDTO.to_json())

# convert the object into a dict
gong_auth_params_dto_dict = gong_auth_params_dto_instance.to_dict()
# create an instance of GongAuthParamsDTO from a dict
gong_auth_params_dto_from_dict = GongAuthParamsDTO.from_dict(gong_auth_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


