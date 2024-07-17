# DirectDataLoadConfigDTO

The configuration for the direct data intake, such as the  direct data intake job type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job** | [**DirectDataJobConfigDTO**](DirectDataJobConfigDTO.md) | The direct data intake job configuration. | [optional] 

## Example

```python
from visier.api.direct_data_intake.models.direct_data_load_config_dto import DirectDataLoadConfigDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DirectDataLoadConfigDTO from a JSON string
direct_data_load_config_dto_instance = DirectDataLoadConfigDTO.from_json(json)
# print the JSON string representation of the object
print(DirectDataLoadConfigDTO.to_json())

# convert the object into a dict
direct_data_load_config_dto_dict = direct_data_load_config_dto_instance.to_dict()
# create an instance of DirectDataLoadConfigDTO from a dict
direct_data_load_config_dto_from_dict = DirectDataLoadConfigDTO.from_dict(direct_data_load_config_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


