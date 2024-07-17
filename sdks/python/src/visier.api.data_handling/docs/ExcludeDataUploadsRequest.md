# ExcludeDataUploadsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | [**UploadToExcludeModel**](UploadToExcludeModel.md) | A form body key that contains a collection of key-value pairs. | [optional] 

## Example

```python
from visier.api.data_handling.models.exclude_data_uploads_request import ExcludeDataUploadsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExcludeDataUploadsRequest from a JSON string
exclude_data_uploads_request_instance = ExcludeDataUploadsRequest.from_json(json)
# print the JSON string representation of the object
print(ExcludeDataUploadsRequest.to_json())

# convert the object into a dict
exclude_data_uploads_request_dict = exclude_data_uploads_request_instance.to_dict()
# create an instance of ExcludeDataUploadsRequest from a dict
exclude_data_uploads_request_from_dict = ExcludeDataUploadsRequest.from_dict(exclude_data_uploads_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


