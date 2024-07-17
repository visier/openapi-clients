# UserPropertyDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name property to map to in the dynamic filter. Valid values are one of &#x60;username&#x60;, &#x60;email&#x60;, &#x60;employeeId&#x60;. | [optional] 

## Example

```python
from visier.api.permission_management.models.user_property_dto import UserPropertyDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UserPropertyDTO from a JSON string
user_property_dto_instance = UserPropertyDTO.from_json(json)
# print the JSON string representation of the object
print(UserPropertyDTO.to_json())

# convert the object into a dict
user_property_dto_dict = user_property_dto_instance.to_dict()
# create an instance of UserPropertyDTO from a dict
user_property_dto_from_dict = UserPropertyDTO.from_dict(user_property_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


