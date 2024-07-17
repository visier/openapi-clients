# DataAccessSetErrorDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Error message | [optional] 
**rci** | **str** | A root cause identifier that allows Visier to determine the source of the problem. | [optional] 

## Example

```python
from visier.api.permission_management.models.data_access_set_error_dto import DataAccessSetErrorDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DataAccessSetErrorDTO from a JSON string
data_access_set_error_dto_instance = DataAccessSetErrorDTO.from_json(json)
# print the JSON string representation of the object
print(DataAccessSetErrorDTO.to_json())

# convert the object into a dict
data_access_set_error_dto_dict = data_access_set_error_dto_instance.to_dict()
# create an instance of DataAccessSetErrorDTO from a dict
data_access_set_error_dto_from_dict = DataAccessSetErrorDTO.from_dict(data_access_set_error_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


