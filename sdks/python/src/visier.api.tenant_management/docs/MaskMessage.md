# MaskMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mask** | **str** | A comma separated list of strings that specifies which fields to include in the response. | [optional] 

## Example

```python
from visier.api.tenant_management.models.mask_message import MaskMessage

# TODO update the JSON string below
json = "{}"
# create an instance of MaskMessage from a JSON string
mask_message_instance = MaskMessage.from_json(json)
# print the JSON string representation of the object
print(MaskMessage.to_json())

# convert the object into a dict
mask_message_dict = mask_message_instance.to_dict()
# create an instance of MaskMessage from a dict
mask_message_from_dict = MaskMessage.from_dict(mask_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


