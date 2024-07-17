# IncludeDataUploadsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | [**UploadToIncludeModel**](UploadToIncludeModel.md) | A form body key that contains a collection of key-value pairs. | [optional] 

## Example

```python
from visier.api.data_handling.models.include_data_uploads_request import IncludeDataUploadsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IncludeDataUploadsRequest from a JSON string
include_data_uploads_request_instance = IncludeDataUploadsRequest.from_json(json)
# print the JSON string representation of the object
print(IncludeDataUploadsRequest.to_json())

# convert the object into a dict
include_data_uploads_request_dict = include_data_uploads_request_instance.to_dict()
# create an instance of IncludeDataUploadsRequest from a dict
include_data_uploads_request_from_dict = IncludeDataUploadsRequest.from_dict(include_data_uploads_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


