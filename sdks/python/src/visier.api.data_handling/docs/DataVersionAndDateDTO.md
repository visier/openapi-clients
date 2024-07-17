# DataVersionAndDateDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_version** | **str** | The data version ID. | [optional] 
**data_version_date** | **str** | The date that the data version was created. | [optional] 

## Example

```python
from visier.api.data_handling.models.data_version_and_date_dto import DataVersionAndDateDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DataVersionAndDateDTO from a JSON string
data_version_and_date_dto_instance = DataVersionAndDateDTO.from_json(json)
# print the JSON string representation of the object
print(DataVersionAndDateDTO.to_json())

# convert the object into a dict
data_version_and_date_dto_dict = data_version_and_date_dto_instance.to_dict()
# create an instance of DataVersionAndDateDTO from a dict
data_version_and_date_dto_from_dict = DataVersionAndDateDTO.from_dict(data_version_and_date_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


