# DimensionsAuthParamsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_key** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**vanity_url** | **str** |  | [optional] 

## Example

```python
from visier.api.data_handling.models.dimensions_auth_params_dto import DimensionsAuthParamsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DimensionsAuthParamsDTO from a JSON string
dimensions_auth_params_dto_instance = DimensionsAuthParamsDTO.from_json(json)
# print the JSON string representation of the object
print(DimensionsAuthParamsDTO.to_json())

# convert the object into a dict
dimensions_auth_params_dto_dict = dimensions_auth_params_dto_instance.to_dict()
# create an instance of DimensionsAuthParamsDTO from a dict
dimensions_auth_params_dto_from_dict = DimensionsAuthParamsDTO.from_dict(dimensions_auth_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


