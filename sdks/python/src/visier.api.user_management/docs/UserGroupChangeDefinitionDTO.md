# UserGroupChangeDefinitionDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A detailed description of the population and purpose of the user group. | [optional] 
**display_name** | **str** | An identifiable user group name to display in Visier, such as \&quot;Leadership User Group\&quot;. | [optional] 
**permission_ids** | [**ElementIDsDTO**](ElementIDsDTO.md) | The unique identifiers of permissions assigned to members of this user group. | [optional] 
**tenant_code** | **str** | The code of the tenant to which the user group belongs or should be created in.  Omit if creating or updating user groups in the current tenant. | [optional] 
**user_group_id** | **str** | The unique identifier of the user group. Omit if creating a new user group. | [optional] 
**users** | [**UserGroupChangeUsersDTO**](UserGroupChangeUsersDTO.md) | The users assigned to the user group. You can define user group members dynamically with &#x60;dynamicFilterDefinition&#x60; or manually with &#x60;includeAllUsers&#x60; or &#x60;manuallyIncludedIds&#x60;. | [optional] 

## Example

```python
from visier.api.user_management.models.user_group_change_definition_dto import UserGroupChangeDefinitionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupChangeDefinitionDTO from a JSON string
user_group_change_definition_dto_instance = UserGroupChangeDefinitionDTO.from_json(json)
# print the JSON string representation of the object
print(UserGroupChangeDefinitionDTO.to_json())

# convert the object into a dict
user_group_change_definition_dto_dict = user_group_change_definition_dto_instance.to_dict()
# create an instance of UserGroupChangeDefinitionDTO from a dict
user_group_change_definition_dto_from_dict = UserGroupChangeDefinitionDTO.from_dict(user_group_change_definition_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


