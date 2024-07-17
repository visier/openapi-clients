# ImportDefinitionAPIDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_id** | **str** | The ID associated with the data connector. | [optional] 
**credential_id** | **str** | The ID associated with the connector credentials currently assigned to this data connector. | [optional] 
**display_name** | **str** | An identifiable data connector name that is displayed within Visier. | [optional] 

## Example

```python
from visier.api.data_handling.models.import_definition_apidto import ImportDefinitionAPIDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ImportDefinitionAPIDTO from a JSON string
import_definition_apidto_instance = ImportDefinitionAPIDTO.from_json(json)
# print the JSON string representation of the object
print(ImportDefinitionAPIDTO.to_json())

# convert the object into a dict
import_definition_apidto_dict = import_definition_apidto_instance.to_dict()
# create an instance of ImportDefinitionAPIDTO from a dict
import_definition_apidto_from_dict = ImportDefinitionAPIDTO.from_dict(import_definition_apidto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


