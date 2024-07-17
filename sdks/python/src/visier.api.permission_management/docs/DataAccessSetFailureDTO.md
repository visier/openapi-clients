# DataAccessSetFailureDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_access_set_id** | **str** | The unique identifier associated with the data access set. | [optional] 
**display_name** | **str** | An identifiable data access set name to display in Visier, such as \&quot;Detailed(Employee)\&quot;. | [optional] 
**error** | [**DataAccessSetErrorDTO**](DataAccessSetErrorDTO.md) | The error associated with the failure. | [optional] 

## Example

```python
from visier.api.permission_management.models.data_access_set_failure_dto import DataAccessSetFailureDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DataAccessSetFailureDTO from a JSON string
data_access_set_failure_dto_instance = DataAccessSetFailureDTO.from_json(json)
# print the JSON string representation of the object
print(DataAccessSetFailureDTO.to_json())

# convert the object into a dict
data_access_set_failure_dto_dict = data_access_set_failure_dto_instance.to_dict()
# create an instance of DataAccessSetFailureDTO from a dict
data_access_set_failure_dto_from_dict = DataAccessSetFailureDTO.from_dict(data_access_set_failure_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


