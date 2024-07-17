# DeleteUserGroupV2Request


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_group_id** | **str** | The ID of user group to delete. | [optional] 

## Example

```python
from visier.api.user_management.models.delete_user_group_v2_request import DeleteUserGroupV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteUserGroupV2Request from a JSON string
delete_user_group_v2_request_instance = DeleteUserGroupV2Request.from_json(json)
# print the JSON string representation of the object
print(DeleteUserGroupV2Request.to_json())

# convert the object into a dict
delete_user_group_v2_request_dict = delete_user_group_v2_request_instance.to_dict()
# create an instance of DeleteUserGroupV2Request from a dict
delete_user_group_v2_request_from_dict = DeleteUserGroupV2Request.from_dict(delete_user_group_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


