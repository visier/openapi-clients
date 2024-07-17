# ImportDefinitionsAPIDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_connectors** | [**List[ImportDefinitionAPIDTO]**](ImportDefinitionAPIDTO.md) | A list of objects representing all the available data connectors in Production. | [optional] 
**limit** | **int** | The number of data connectors to return. The maximum number of data connectors to return is 1000. | [optional] 
**start** | **int** | The index to start retrieving values from, also known as offset. The index begins at 0. | [optional] 

## Example

```python
from visier.api.data_handling.models.import_definitions_apidto import ImportDefinitionsAPIDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ImportDefinitionsAPIDTO from a JSON string
import_definitions_apidto_instance = ImportDefinitionsAPIDTO.from_json(json)
# print the JSON string representation of the object
print(ImportDefinitionsAPIDTO.to_json())

# convert the object into a dict
import_definitions_apidto_dict = import_definitions_apidto_instance.to_dict()
# create an instance of ImportDefinitionsAPIDTO from a dict
import_definitions_apidto_from_dict = ImportDefinitionsAPIDTO.from_dict(import_definitions_apidto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


