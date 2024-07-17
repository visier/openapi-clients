# ProductionVersionsAPIOperationResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**export** | **object** | The result of the &#x60;export&#x60; operation. | [optional] 

## Example

```python
from visier.api.project_management.models.production_versions_api_operation_response_dto import ProductionVersionsAPIOperationResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ProductionVersionsAPIOperationResponseDTO from a JSON string
production_versions_api_operation_response_dto_instance = ProductionVersionsAPIOperationResponseDTO.from_json(json)
# print the JSON string representation of the object
print(ProductionVersionsAPIOperationResponseDTO.to_json())

# convert the object into a dict
production_versions_api_operation_response_dto_dict = production_versions_api_operation_response_dto_instance.to_dict()
# create an instance of ProductionVersionsAPIOperationResponseDTO from a dict
production_versions_api_operation_response_dto_from_dict = ProductionVersionsAPIOperationResponseDTO.from_dict(production_versions_api_operation_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


