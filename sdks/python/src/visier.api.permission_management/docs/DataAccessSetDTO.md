# DataAccessSetDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analytic_object_id** | **str** | The unique ID of the analytic object that the data access set is for. | [optional] 
**description** | **str** | A description of the data access set. | [optional] 
**display_name** | **str** | An identifiable data access set name to display in Visier, such as \&quot;Aggregate(Employee)\&quot;. | [optional] 
**id** | **str** | The unique ID of the data access set. | [optional] 
**property_access_configs** | [**List[PropertyAccessConfigDTO]**](PropertyAccessConfigDTO.md) | The data access assigned to properties in the data access set. | [optional] 

## Example

```python
from visier.api.permission_management.models.data_access_set_dto import DataAccessSetDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DataAccessSetDTO from a JSON string
data_access_set_dto_instance = DataAccessSetDTO.from_json(json)
# print the JSON string representation of the object
print(DataAccessSetDTO.to_json())

# convert the object into a dict
data_access_set_dto_dict = data_access_set_dto_instance.to_dict()
# create an instance of DataAccessSetDTO from a dict
data_access_set_dto_from_dict = DataAccessSetDTO.from_dict(data_access_set_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


