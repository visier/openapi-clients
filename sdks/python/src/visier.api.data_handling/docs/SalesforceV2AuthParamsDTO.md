# SalesforceV2AuthParamsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_code** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**login_host** | **str** |  | [optional] 

## Example

```python
from visier.api.data_handling.models.salesforce_v2_auth_params_dto import SalesforceV2AuthParamsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SalesforceV2AuthParamsDTO from a JSON string
salesforce_v2_auth_params_dto_instance = SalesforceV2AuthParamsDTO.from_json(json)
# print the JSON string representation of the object
print(SalesforceV2AuthParamsDTO.to_json())

# convert the object into a dict
salesforce_v2_auth_params_dto_dict = salesforce_v2_auth_params_dto_instance.to_dict()
# create an instance of SalesforceV2AuthParamsDTO from a dict
salesforce_v2_auth_params_dto_from_dict = SalesforceV2AuthParamsDTO.from_dict(salesforce_v2_auth_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


