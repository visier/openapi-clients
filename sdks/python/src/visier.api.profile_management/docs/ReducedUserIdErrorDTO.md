# ReducedUserIdErrorDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**ReducedErrorDTO**](ReducedErrorDTO.md) | The details about the error. | [optional] 
**user_id** | **str** | The bad user ID. | [optional] 

## Example

```python
from visier.api.profile_management.models.reduced_user_id_error_dto import ReducedUserIdErrorDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ReducedUserIdErrorDTO from a JSON string
reduced_user_id_error_dto_instance = ReducedUserIdErrorDTO.from_json(json)
# print the JSON string representation of the object
print(ReducedUserIdErrorDTO.to_json())

# convert the object into a dict
reduced_user_id_error_dto_dict = reduced_user_id_error_dto_instance.to_dict()
# create an instance of ReducedUserIdErrorDTO from a dict
reduced_user_id_error_dto_from_dict = ReducedUserIdErrorDTO.from_dict(reduced_user_id_error_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


