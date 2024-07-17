# PermissionBulkOperationResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failures** | [**List[PermissionFailureDTO]**](PermissionFailureDTO.md) | The permissions that did not process and any relevant error information. | [optional] 
**successes** | [**List[PermissionSuccessDTO]**](PermissionSuccessDTO.md) | The successfully processed permissions. | [optional] 

## Example

```python
from visier.api.permission_management.models.permission_bulk_operation_response_dto import PermissionBulkOperationResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionBulkOperationResponseDTO from a JSON string
permission_bulk_operation_response_dto_instance = PermissionBulkOperationResponseDTO.from_json(json)
# print the JSON string representation of the object
print(PermissionBulkOperationResponseDTO.to_json())

# convert the object into a dict
permission_bulk_operation_response_dto_dict = permission_bulk_operation_response_dto_instance.to_dict()
# create an instance of PermissionBulkOperationResponseDTO from a dict
permission_bulk_operation_response_dto_from_dict = PermissionBulkOperationResponseDTO.from_dict(permission_bulk_operation_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


