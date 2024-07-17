# BulkDataAccessSetResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failures** | [**List[DataAccessSetFailureDTO]**](DataAccessSetFailureDTO.md) | The data access sets that failed to be created and any relevant error information. | [optional] 
**successes** | [**List[DataAccessSetSuccessDTO]**](DataAccessSetSuccessDTO.md) | The successfully created data access sets. | [optional] 

## Example

```python
from visier.api.permission_management.models.bulk_data_access_set_response_dto import BulkDataAccessSetResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of BulkDataAccessSetResponseDTO from a JSON string
bulk_data_access_set_response_dto_instance = BulkDataAccessSetResponseDTO.from_json(json)
# print the JSON string representation of the object
print(BulkDataAccessSetResponseDTO.to_json())

# convert the object into a dict
bulk_data_access_set_response_dto_dict = bulk_data_access_set_response_dto_instance.to_dict()
# create an instance of BulkDataAccessSetResponseDTO from a dict
bulk_data_access_set_response_dto_from_dict = BulkDataAccessSetResponseDTO.from_dict(bulk_data_access_set_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


