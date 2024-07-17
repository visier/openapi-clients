# PropertySetConfigDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_access_configs** | [**List[PropertyAccessConfigDTO]**](PropertyAccessConfigDTO.md) | The data access for a property. | [optional] 
**shareable_data_access_set** | [**ShareableDataAccessSet**](ShareableDataAccessSet.md) | A shareable data access set. Shareable data access sets may be linked in multiple permissions. | [optional] 

## Example

```python
from visier.api.permission_management.models.property_set_config_dto import PropertySetConfigDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PropertySetConfigDTO from a JSON string
property_set_config_dto_instance = PropertySetConfigDTO.from_json(json)
# print the JSON string representation of the object
print(PropertySetConfigDTO.to_json())

# convert the object into a dict
property_set_config_dto_dict = property_set_config_dto_instance.to_dict()
# create an instance of PropertySetConfigDTO from a dict
property_set_config_dto_from_dict = PropertySetConfigDTO.from_dict(property_set_config_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


