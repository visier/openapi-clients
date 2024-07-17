# ReducedErrorDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_message** | **str** | A meaningful message for the end user. | [optional] 

## Example

```python
from visier.api.profile_management.models.reduced_error_dto import ReducedErrorDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ReducedErrorDTO from a JSON string
reduced_error_dto_instance = ReducedErrorDTO.from_json(json)
# print the JSON string representation of the object
print(ReducedErrorDTO.to_json())

# convert the object into a dict
reduced_error_dto_dict = reduced_error_dto_instance.to_dict()
# create an instance of ReducedErrorDTO from a dict
reduced_error_dto_from_dict = ReducedErrorDTO.from_dict(reduced_error_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


