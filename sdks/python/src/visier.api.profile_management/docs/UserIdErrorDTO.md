# UserIdErrorDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**ErrorDTO**](ErrorDTO.md) | The details about the error. | [optional] 
**user_id** | **str** | The bad user ID. | [optional] 

## Example

```python
from visier.api.profile_management.models.user_id_error_dto import UserIdErrorDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UserIdErrorDTO from a JSON string
user_id_error_dto_instance = UserIdErrorDTO.from_json(json)
# print the JSON string representation of the object
print(UserIdErrorDTO.to_json())

# convert the object into a dict
user_id_error_dto_dict = user_id_error_dto_instance.to_dict()
# create an instance of UserIdErrorDTO from a dict
user_id_error_dto_from_dict = UserIdErrorDTO.from_dict(user_id_error_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


