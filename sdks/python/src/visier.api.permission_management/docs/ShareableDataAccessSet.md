# ShareableDataAccessSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_access_set_id** | **str** | The unique identifier of the shareable data access set. | [optional] 

## Example

```python
from visier.api.permission_management.models.shareable_data_access_set import ShareableDataAccessSet

# TODO update the JSON string below
json = "{}"
# create an instance of ShareableDataAccessSet from a JSON string
shareable_data_access_set_instance = ShareableDataAccessSet.from_json(json)
# print the JSON string representation of the object
print(ShareableDataAccessSet.to_json())

# convert the object into a dict
shareable_data_access_set_dict = shareable_data_access_set_instance.to_dict()
# create an instance of ShareableDataAccessSet from a dict
shareable_data_access_set_from_dict = ShareableDataAccessSet.from_dict(shareable_data_access_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


