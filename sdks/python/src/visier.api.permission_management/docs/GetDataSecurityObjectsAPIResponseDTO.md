# GetDataSecurityObjectsAPIResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analytic_objects** | [**List[AnalyticObjectDTO]**](AnalyticObjectDTO.md) | A list of analytic objects and their related objects that are available to define data access to. | [optional] 

## Example

```python
from visier.api.permission_management.models.get_data_security_objects_api_response_dto import GetDataSecurityObjectsAPIResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of GetDataSecurityObjectsAPIResponseDTO from a JSON string
get_data_security_objects_api_response_dto_instance = GetDataSecurityObjectsAPIResponseDTO.from_json(json)
# print the JSON string representation of the object
print(GetDataSecurityObjectsAPIResponseDTO.to_json())

# convert the object into a dict
get_data_security_objects_api_response_dto_dict = get_data_security_objects_api_response_dto_instance.to_dict()
# create an instance of GetDataSecurityObjectsAPIResponseDTO from a dict
get_data_security_objects_api_response_dto_from_dict = GetDataSecurityObjectsAPIResponseDTO.from_dict(get_data_security_objects_api_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


