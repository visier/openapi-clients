# AssignRevokePermissionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | [**List[Permission]**](Permission.md) | A list of objects representing the permissions to assign to or remove from users. | [optional] 

## Example

```python
from visier.api.user_management.models.assign_revoke_permissions_request import AssignRevokePermissionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssignRevokePermissionsRequest from a JSON string
assign_revoke_permissions_request_instance = AssignRevokePermissionsRequest.from_json(json)
# print the JSON string representation of the object
print(AssignRevokePermissionsRequest.to_json())

# convert the object into a dict
assign_revoke_permissions_request_dict = assign_revoke_permissions_request_instance.to_dict()
# create an instance of AssignRevokePermissionsRequest from a dict
assign_revoke_permissions_request_from_dict = AssignRevokePermissionsRequest.from_dict(assign_revoke_permissions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


