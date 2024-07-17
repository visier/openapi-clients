# ZoomAuthParamsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_code** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 

## Example

```python
from visier.api.data_handling.models.zoom_auth_params_dto import ZoomAuthParamsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ZoomAuthParamsDTO from a JSON string
zoom_auth_params_dto_instance = ZoomAuthParamsDTO.from_json(json)
# print the JSON string representation of the object
print(ZoomAuthParamsDTO.to_json())

# convert the object into a dict
zoom_auth_params_dto_dict = zoom_auth_params_dto_instance.to_dict()
# create an instance of ZoomAuthParamsDTO from a dict
zoom_auth_params_dto_from_dict = ZoomAuthParamsDTO.from_dict(zoom_auth_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


