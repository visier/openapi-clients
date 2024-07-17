# DirectDataUploadFileResponseDTO

The transaction results.  If uploading a file, a success response means the upload was successful and doesn't always mean the file was successfully loaded into its target object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The upload response message from the provisioning service. | [optional] 
**status** | **str** | The status of the request. | [optional] 
**transaction_id** | **str** | The unique transaction identifier. | [optional] 

## Example

```python
from visier.api.direct_data_intake.models.direct_data_upload_file_response_dto import DirectDataUploadFileResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DirectDataUploadFileResponseDTO from a JSON string
direct_data_upload_file_response_dto_instance = DirectDataUploadFileResponseDTO.from_json(json)
# print the JSON string representation of the object
print(DirectDataUploadFileResponseDTO.to_json())

# convert the object into a dict
direct_data_upload_file_response_dto_dict = direct_data_upload_file_response_dto_instance.to_dict()
# create an instance of DirectDataUploadFileResponseDTO from a dict
direct_data_upload_file_response_dto_from_dict = DirectDataUploadFileResponseDTO.from_dict(direct_data_upload_file_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


