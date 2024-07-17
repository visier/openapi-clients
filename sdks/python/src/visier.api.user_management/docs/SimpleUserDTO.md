# SimpleUserDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The unique identifier associated with the user. | [optional] 
**username** | **str** | The user&#39;s username. This is typically the user&#39;s email, such as john@visier.com. | [optional] 

## Example

```python
from visier.api.user_management.models.simple_user_dto import SimpleUserDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleUserDTO from a JSON string
simple_user_dto_instance = SimpleUserDTO.from_json(json)
# print the JSON string representation of the object
print(SimpleUserDTO.to_json())

# convert the object into a dict
simple_user_dto_dict = simple_user_dto_instance.to_dict()
# create an instance of SimpleUserDTO from a dict
simple_user_dto_from_dict = SimpleUserDTO.from_dict(simple_user_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


