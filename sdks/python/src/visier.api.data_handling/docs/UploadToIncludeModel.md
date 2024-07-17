# UploadToIncludeModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uploads** | [**List[UploadToInclude]**](UploadToInclude.md) | A list of objects representing the data uploads to include for a particular analytic tenant. | [optional] 

## Example

```python
from visier.api.data_handling.models.upload_to_include_model import UploadToIncludeModel

# TODO update the JSON string below
json = "{}"
# create an instance of UploadToIncludeModel from a JSON string
upload_to_include_model_instance = UploadToIncludeModel.from_json(json)
# print the JSON string representation of the object
print(UploadToIncludeModel.to_json())

# convert the object into a dict
upload_to_include_model_dict = upload_to_include_model_instance.to_dict()
# create an instance of UploadToIncludeModel from a dict
upload_to_include_model_from_dict = UploadToIncludeModel.from_dict(upload_to_include_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


