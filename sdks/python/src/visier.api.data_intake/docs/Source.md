# Source


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_size** | **str** | The size of the data transfer in bytes. | [optional] 
**message** | **str** | A meaningful message about the data transfer. | [optional] 
**rows** | **str** | The number of rows in the data transfer. | [optional] 
**source_id** | **str** | The unique identifier associated with the source that data was transferred to. | [optional] 
**source_name** | **str** | The object name of the source. | [optional] 
**status** | **str** | The status of the data transfer for this source. | [optional] 

## Example

```python
from visier.api.data_intake.models.source import Source

# TODO update the JSON string below
json = "{}"
# create an instance of Source from a JSON string
source_instance = Source.from_json(json)
# print the JSON string representation of the object
print(Source.to_json())

# convert the object into a dict
source_dict = source_instance.to_dict()
# create an instance of Source from a dict
source_from_dict = Source.from_dict(source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


