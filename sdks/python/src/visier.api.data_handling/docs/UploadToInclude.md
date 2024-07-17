# UploadToInclude


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_all** | **bool** | If \&quot;true\&quot;, all data uploads are included for the analytic tenant. | [optional] 
**tenant_code** | **str** | The tenant code of the analytic tenant you are including a data upload for. | [optional] 
**upload_times** | **List[str]** | A comma-separated list of strings representing the upload time of each data upload to include. | [optional] 

## Example

```python
from visier.api.data_handling.models.upload_to_include import UploadToInclude

# TODO update the JSON string below
json = "{}"
# create an instance of UploadToInclude from a JSON string
upload_to_include_instance = UploadToInclude.from_json(json)
# print the JSON string representation of the object
print(UploadToInclude.to_json())

# convert the object into a dict
upload_to_include_dict = upload_to_include_instance.to_dict()
# create an instance of UploadToInclude from a dict
upload_to_include_from_dict = UploadToInclude.from_dict(upload_to_include_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


