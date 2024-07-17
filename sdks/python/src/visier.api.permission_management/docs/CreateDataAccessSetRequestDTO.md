# CreateDataAccessSetRequestDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shareable_property_access_configs** | [**List[DataAccessSetDTO]**](DataAccessSetDTO.md) | The data access sets to be created. | [optional] 

## Example

```python
from visier.api.permission_management.models.create_data_access_set_request_dto import CreateDataAccessSetRequestDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDataAccessSetRequestDTO from a JSON string
create_data_access_set_request_dto_instance = CreateDataAccessSetRequestDTO.from_json(json)
# print the JSON string representation of the object
print(CreateDataAccessSetRequestDTO.to_json())

# convert the object into a dict
create_data_access_set_request_dto_dict = create_data_access_set_request_dto_instance.to_dict()
# create an instance of CreateDataAccessSetRequestDTO from a dict
create_data_access_set_request_dto_from_dict = CreateDataAccessSetRequestDTO.from_dict(create_data_access_set_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


