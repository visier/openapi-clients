# SystemStatusDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overall** | **str** | The overall status of Visier&#39;s platform and services. | [optional] 

## Example

```python
from visier.api.system_status.models.system_status_dto import SystemStatusDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SystemStatusDTO from a JSON string
system_status_dto_instance = SystemStatusDTO.from_json(json)
# print the JSON string representation of the object
print(SystemStatusDTO.to_json())

# convert the object into a dict
system_status_dto_dict = system_status_dto_instance.to_dict()
# create an instance of SystemStatusDTO from a dict
system_status_dto_from_dict = SystemStatusDTO.from_dict(system_status_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


