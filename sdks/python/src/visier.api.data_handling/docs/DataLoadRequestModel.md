# DataLoadRequestModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | **List[str]** | A comma-separated list of file names.  Example:  &#x60;\&quot;files\&quot;: \&quot;/path/to/file1.zip.gpg,/path/to/another/file.zip.gpg\&quot;&#x60; | [optional] 
**skip_data_load** | **bool** | If \&quot;true\&quot;, receives the files and skips data loading. Does not generate a data version. | [optional] 

## Example

```python
from visier.api.data_handling.models.data_load_request_model import DataLoadRequestModel

# TODO update the JSON string below
json = "{}"
# create an instance of DataLoadRequestModel from a JSON string
data_load_request_model_instance = DataLoadRequestModel.from_json(json)
# print the JSON string representation of the object
print(DataLoadRequestModel.to_json())

# convert the object into a dict
data_load_request_model_dict = data_load_request_model_instance.to_dict()
# create an instance of DataLoadRequestModel from a dict
data_load_request_model_from_dict = DataLoadRequestModel.from_dict(data_load_request_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


