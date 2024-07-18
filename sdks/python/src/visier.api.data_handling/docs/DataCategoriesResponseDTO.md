# DataCategoriesResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | [**List[DataCategoryResponseDTO]**](DataCategoryResponseDTO.md) |  | [optional] 

## Example

```python
from visier.api.data_handling.models.data_categories_response_dto import DataCategoriesResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DataCategoriesResponseDTO from a JSON string
data_categories_response_dto_instance = DataCategoriesResponseDTO.from_json(json)
# print the JSON string representation of the object
print(DataCategoriesResponseDTO.to_json())

# convert the object into a dict
data_categories_response_dto_dict = data_categories_response_dto_instance.to_dict()
# create an instance of DataCategoriesResponseDTO from a dict
data_categories_response_dto_from_dict = DataCategoriesResponseDTO.from_dict(data_categories_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


