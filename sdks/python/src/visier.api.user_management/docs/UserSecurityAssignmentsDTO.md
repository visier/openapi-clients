# UserSecurityAssignmentsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier associated with the user group. | [optional] 
**name** | **str** | The name of the user group. | [optional] 
**users** | [**List[SimpleUserDTO]**](SimpleUserDTO.md) | A list of objects representing the users assigned to or removed from the user group. | [optional] 

## Example

```python
from visier.api.user_management.models.user_security_assignments_dto import UserSecurityAssignmentsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UserSecurityAssignmentsDTO from a JSON string
user_security_assignments_dto_instance = UserSecurityAssignmentsDTO.from_json(json)
# print the JSON string representation of the object
print(UserSecurityAssignmentsDTO.to_json())

# convert the object into a dict
user_security_assignments_dto_dict = user_security_assignments_dto_instance.to_dict()
# create an instance of UserSecurityAssignmentsDTO from a dict
user_security_assignments_dto_from_dict = UserSecurityAssignmentsDTO.from_dict(user_security_assignments_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


