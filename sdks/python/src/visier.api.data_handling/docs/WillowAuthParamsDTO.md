# WillowAuthParamsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_token** | **str** |  | [optional] 
**host_name** | **str** |  | [optional] 

## Example

```python
from visier.api.data_handling.models.willow_auth_params_dto import WillowAuthParamsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of WillowAuthParamsDTO from a JSON string
willow_auth_params_dto_instance = WillowAuthParamsDTO.from_json(json)
# print the JSON string representation of the object
print(WillowAuthParamsDTO.to_json())

# convert the object into a dict
willow_auth_params_dto_dict = willow_auth_params_dto_instance.to_dict()
# create an instance of WillowAuthParamsDTO from a dict
willow_auth_params_dto_from_dict = WillowAuthParamsDTO.from_dict(willow_auth_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


