# PermissionsListDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | [**List[PermissionDTO]**](PermissionDTO.md) | The list of permissions that will be created or updated | [optional] 

## Example

```python
from visier.api.permission_management.models.permissions_list_dto import PermissionsListDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionsListDTO from a JSON string
permissions_list_dto_instance = PermissionsListDTO.from_json(json)
# print the JSON string representation of the object
print(PermissionsListDTO.to_json())

# convert the object into a dict
permissions_list_dto_dict = permissions_list_dto_instance.to_dict()
# create an instance of PermissionsListDTO from a dict
permissions_list_dto_from_dict = PermissionsListDTO.from_dict(permissions_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


