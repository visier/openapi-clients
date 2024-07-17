# DeletePermissionsRequestDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permission_ids** | **List[str]** | The identifiers of the permissions to delete. | [optional] 

## Example

```python
from visier.api.permission_management.models.delete_permissions_request_dto import DeletePermissionsRequestDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DeletePermissionsRequestDTO from a JSON string
delete_permissions_request_dto_instance = DeletePermissionsRequestDTO.from_json(json)
# print the JSON string representation of the object
print(DeletePermissionsRequestDTO.to_json())

# convert the object into a dict
delete_permissions_request_dto_dict = delete_permissions_request_dto_instance.to_dict()
# create an instance of DeletePermissionsRequestDTO from a dict
delete_permissions_request_dto_from_dict = DeletePermissionsRequestDTO.from_dict(delete_permissions_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


