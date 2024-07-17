# GetProductionVersionsAPIResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**published_versions** | [**List[ProjectDTO]**](ProjectDTO.md) | A list of projects that were published to production. | [optional] 

## Example

```python
from visier.api.project_management.models.get_production_versions_api_response_dto import GetProductionVersionsAPIResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of GetProductionVersionsAPIResponseDTO from a JSON string
get_production_versions_api_response_dto_instance = GetProductionVersionsAPIResponseDTO.from_json(json)
# print the JSON string representation of the object
print(GetProductionVersionsAPIResponseDTO.to_json())

# convert the object into a dict
get_production_versions_api_response_dto_dict = get_production_versions_api_response_dto_instance.to_dict()
# create an instance of GetProductionVersionsAPIResponseDTO from a dict
get_production_versions_api_response_dto_from_dict = GetProductionVersionsAPIResponseDTO.from_dict(get_production_versions_api_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


