# Microsoft365AuthParamsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**o_auth_tenant_id** | **str** |  | [optional] 

## Example

```python
from visier.api.data_handling.models.microsoft365_auth_params_dto import Microsoft365AuthParamsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of Microsoft365AuthParamsDTO from a JSON string
microsoft365_auth_params_dto_instance = Microsoft365AuthParamsDTO.from_json(json)
# print the JSON string representation of the object
print(Microsoft365AuthParamsDTO.to_json())

# convert the object into a dict
microsoft365_auth_params_dto_dict = microsoft365_auth_params_dto_instance.to_dict()
# create an instance of Microsoft365AuthParamsDTO from a dict
microsoft365_auth_params_dto_from_dict = Microsoft365AuthParamsDTO.from_dict(microsoft365_auth_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


