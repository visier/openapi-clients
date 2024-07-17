# SalesforceAuthParamsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | [optional] 
**refresh_token** | **str** |  | [optional] 

## Example

```python
from visier.api.data_handling.models.salesforce_auth_params_dto import SalesforceAuthParamsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SalesforceAuthParamsDTO from a JSON string
salesforce_auth_params_dto_instance = SalesforceAuthParamsDTO.from_json(json)
# print the JSON string representation of the object
print(SalesforceAuthParamsDTO.to_json())

# convert the object into a dict
salesforce_auth_params_dto_dict = salesforce_auth_params_dto_instance.to_dict()
# create an instance of SalesforceAuthParamsDTO from a dict
salesforce_auth_params_dto_from_dict = SalesforceAuthParamsDTO.from_dict(salesforce_auth_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


