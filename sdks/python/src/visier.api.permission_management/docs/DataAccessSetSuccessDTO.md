# DataAccessSetSuccessDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_access_set_id** | **str** | The unique identifier associated with the created data access set. | [optional] 
**display_name** | **str** | An identifiable data access set name to display in Visier, such as \&quot;Detailed(Employee)\&quot;. | [optional] 

## Example

```python
from visier.api.permission_management.models.data_access_set_success_dto import DataAccessSetSuccessDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DataAccessSetSuccessDTO from a JSON string
data_access_set_success_dto_instance = DataAccessSetSuccessDTO.from_json(json)
# print the JSON string representation of the object
print(DataAccessSetSuccessDTO.to_json())

# convert the object into a dict
data_access_set_success_dto_dict = data_access_set_success_dto_instance.to_dict()
# create an instance of DataAccessSetSuccessDTO from a dict
data_access_set_success_dto_from_dict = DataAccessSetSuccessDTO.from_dict(data_access_set_success_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


