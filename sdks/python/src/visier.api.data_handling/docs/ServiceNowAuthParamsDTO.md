# ServiceNowAuthParamsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_domain_name** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from visier.api.data_handling.models.service_now_auth_params_dto import ServiceNowAuthParamsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceNowAuthParamsDTO from a JSON string
service_now_auth_params_dto_instance = ServiceNowAuthParamsDTO.from_json(json)
# print the JSON string representation of the object
print(ServiceNowAuthParamsDTO.to_json())

# convert the object into a dict
service_now_auth_params_dto_dict = service_now_auth_params_dto_instance.to_dict()
# create an instance of ServiceNowAuthParamsDTO from a dict
service_now_auth_params_dto_from_dict = ServiceNowAuthParamsDTO.from_dict(service_now_auth_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


