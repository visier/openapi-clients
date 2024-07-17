# GetContentPackagesAPIResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_packages** | [**List[ContentPackageDTO]**](ContentPackageDTO.md) | A list of objects representing the available content packages. | [optional] 

## Example

```python
from visier.api.permission_management.models.get_content_packages_api_response_dto import GetContentPackagesAPIResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of GetContentPackagesAPIResponseDTO from a JSON string
get_content_packages_api_response_dto_instance = GetContentPackagesAPIResponseDTO.from_json(json)
# print the JSON string representation of the object
print(GetContentPackagesAPIResponseDTO.to_json())

# convert the object into a dict
get_content_packages_api_response_dto_dict = get_content_packages_api_response_dto_instance.to_dict()
# create an instance of GetContentPackagesAPIResponseDTO from a dict
get_content_packages_api_response_dto_from_dict = GetContentPackagesAPIResponseDTO.from_dict(get_content_packages_api_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


