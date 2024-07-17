# ConnectorInfoResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_id** | **str** | The unique identifier associated with the data connector. | [optional] 
**description** | **str** |  | [optional] 
**display_name** | **str** | An identifiable data connector name that is displayed within Visier. | [optional] 

## Example

```python
from visier.api.data_handling.models.connector_info_response_dto import ConnectorInfoResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorInfoResponseDTO from a JSON string
connector_info_response_dto_instance = ConnectorInfoResponseDTO.from_json(json)
# print the JSON string representation of the object
print(ConnectorInfoResponseDTO.to_json())

# convert the object into a dict
connector_info_response_dto_dict = connector_info_response_dto_instance.to_dict()
# create an instance of ConnectorInfoResponseDTO from a dict
connector_info_response_dto_from_dict = ConnectorInfoResponseDTO.from_dict(connector_info_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


