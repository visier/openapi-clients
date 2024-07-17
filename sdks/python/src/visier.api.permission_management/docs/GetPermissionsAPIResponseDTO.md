# GetPermissionsAPIResponseDTO

List of available permissions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | [**List[PermissionDTO]**](PermissionDTO.md) | A list of objects representing the available permissions. | [optional] 

## Example

```python
from visier.api.permission_management.models.get_permissions_api_response_dto import GetPermissionsAPIResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of GetPermissionsAPIResponseDTO from a JSON string
get_permissions_api_response_dto_instance = GetPermissionsAPIResponseDTO.from_json(json)
# print the JSON string representation of the object
print(GetPermissionsAPIResponseDTO.to_json())

# convert the object into a dict
get_permissions_api_response_dto_dict = get_permissions_api_response_dto_instance.to_dict()
# create an instance of GetPermissionsAPIResponseDTO from a dict
get_permissions_api_response_dto_from_dict = GetPermissionsAPIResponseDTO.from_dict(get_permissions_api_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


