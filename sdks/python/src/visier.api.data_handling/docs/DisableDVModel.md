# DisableDVModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_version_objects** | [**List[DataVersionObject]**](DataVersionObject.md) | A list of objects representing the data version to disable for a particular analytic tenant.  The limit of objects to include per request is 1000. | [optional] 

## Example

```python
from visier.api.data_handling.models.disable_dv_model import DisableDVModel

# TODO update the JSON string below
json = "{}"
# create an instance of DisableDVModel from a JSON string
disable_dv_model_instance = DisableDVModel.from_json(json)
# print the JSON string representation of the object
print(DisableDVModel.to_json())

# convert the object into a dict
disable_dv_model_dict = disable_dv_model_instance.to_dict()
# create an instance of DisableDVModel from a dict
disable_dv_model_from_dict = DisableDVModel.from_dict(disable_dv_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


