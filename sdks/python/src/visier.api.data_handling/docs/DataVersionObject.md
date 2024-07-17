# DataVersionObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_versions** | **str** | The data version to disable for a particular analytic tenant. | [optional] 
**tenant_code** | **str** | The tenant code for the analytic tenant that you are disabling a data version. | [optional] 

## Example

```python
from visier.api.data_handling.models.data_version_object import DataVersionObject

# TODO update the JSON string below
json = "{}"
# create an instance of DataVersionObject from a JSON string
data_version_object_instance = DataVersionObject.from_json(json)
# print the JSON string representation of the object
print(DataVersionObject.to_json())

# convert the object into a dict
data_version_object_dict = data_version_object_instance.to_dict()
# create an instance of DataVersionObject from a dict
data_version_object_from_dict = DataVersionObject.from_dict(data_version_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


