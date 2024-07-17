# UploadToExclude


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_all** | **bool** | If \&quot;true\&quot;, all data uploads are excluded for the analytic tenant. | [optional] 
**tenant_code** | **str** | The tenant code of the analytic tenant you are excluding a data upload for. | [optional] 
**upload_times** | **List[str]** | A comma-separated list of strings representing the upload time of each data upload to exclude. | [optional] 

## Example

```python
from visier.api.data_handling.models.upload_to_exclude import UploadToExclude

# TODO update the JSON string below
json = "{}"
# create an instance of UploadToExclude from a JSON string
upload_to_exclude_instance = UploadToExclude.from_json(json)
# print the JSON string representation of the object
print(UploadToExclude.to_json())

# convert the object into a dict
upload_to_exclude_dict = upload_to_exclude_instance.to_dict()
# create an instance of UploadToExclude from a dict
upload_to_exclude_from_dict = UploadToExclude.from_dict(upload_to_exclude_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


