# ContentPackageDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_package_id** | **str** | The unique ID of the content package. | [optional] 
**description** | **str** | A description of the content package. | [optional] 
**display_name** | **str** | An identifiable content package name to display in Visier, such as \&quot;Talent Acquisition Core Content\&quot;. | [optional] 

## Example

```python
from visier.api.permission_management.models.content_package_dto import ContentPackageDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ContentPackageDTO from a JSON string
content_package_dto_instance = ContentPackageDTO.from_json(json)
# print the JSON string representation of the object
print(ContentPackageDTO.to_json())

# convert the object into a dict
content_package_dto_dict = content_package_dto_instance.to_dict()
# create an instance of ContentPackageDTO from a dict
content_package_dto_from_dict = ContentPackageDTO.from_dict(content_package_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


