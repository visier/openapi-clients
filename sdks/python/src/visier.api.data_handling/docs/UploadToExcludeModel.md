# UploadToExcludeModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uploads** | [**List[UploadToExclude]**](UploadToExclude.md) | A list of objects representing the data uploads to exclude for a particular analytic tenant. | [optional] 

## Example

```python
from visier.api.data_handling.models.upload_to_exclude_model import UploadToExcludeModel

# TODO update the JSON string below
json = "{}"
# create an instance of UploadToExcludeModel from a JSON string
upload_to_exclude_model_instance = UploadToExcludeModel.from_json(json)
# print the JSON string representation of the object
print(UploadToExcludeModel.to_json())

# convert the object into a dict
upload_to_exclude_model_dict = upload_to_exclude_model_instance.to_dict()
# create an instance of UploadToExcludeModel from a dict
upload_to_exclude_model_from_dict = UploadToExcludeModel.from_dict(upload_to_exclude_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


