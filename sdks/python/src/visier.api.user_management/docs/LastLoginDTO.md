# LastLoginDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **str** | The time that the user last logged into Visier. | [optional] 

## Example

```python
from visier.api.user_management.models.last_login_dto import LastLoginDTO

# TODO update the JSON string below
json = "{}"
# create an instance of LastLoginDTO from a JSON string
last_login_dto_instance = LastLoginDTO.from_json(json)
# print the JSON string representation of the object
print(LastLoginDTO.to_json())

# convert the object into a dict
last_login_dto_dict = last_login_dto_instance.to_dict()
# create an instance of LastLoginDTO from a dict
last_login_dto_from_dict = LastLoginDTO.from_dict(last_login_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


