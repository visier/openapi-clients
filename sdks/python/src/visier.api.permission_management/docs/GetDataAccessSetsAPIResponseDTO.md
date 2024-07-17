# GetDataAccessSetsAPIResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_access_sets** | [**List[DataAccessSetDTO]**](DataAccessSetDTO.md) | A list of objects representing the shareable data access sets. | [optional] 

## Example

```python
from visier.api.permission_management.models.get_data_access_sets_api_response_dto import GetDataAccessSetsAPIResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of GetDataAccessSetsAPIResponseDTO from a JSON string
get_data_access_sets_api_response_dto_instance = GetDataAccessSetsAPIResponseDTO.from_json(json)
# print the JSON string representation of the object
print(GetDataAccessSetsAPIResponseDTO.to_json())

# convert the object into a dict
get_data_access_sets_api_response_dto_dict = get_data_access_sets_api_response_dto_instance.to_dict()
# create an instance of GetDataAccessSetsAPIResponseDTO from a dict
get_data_access_sets_api_response_dto_from_dict = GetDataAccessSetsAPIResponseDTO.from_dict(get_data_access_sets_api_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


