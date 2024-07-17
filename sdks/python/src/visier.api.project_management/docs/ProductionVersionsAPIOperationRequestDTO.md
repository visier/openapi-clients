# ProductionVersionsAPIOperationRequestDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**export_parameters** | [**ExportProductionVersionsAPIOperationParametersDTO**](ExportProductionVersionsAPIOperationParametersDTO.md) | The parameters for the &#x60;export&#x60; option, such as the production version to start exporting versions from. Required for &#x60;export&#x60; operations. | [optional] 
**operation** | **str** | The operation to perform. Valid values:  * &#x60;export&#x60;: Export the project changes of the requested production versions and their related files, such as any Guidebook images. If successful, a ZIP file is returned containing any relevant image files and a JSON file with the production project changes. | [optional] 

## Example

```python
from visier.api.project_management.models.production_versions_api_operation_request_dto import ProductionVersionsAPIOperationRequestDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ProductionVersionsAPIOperationRequestDTO from a JSON string
production_versions_api_operation_request_dto_instance = ProductionVersionsAPIOperationRequestDTO.from_json(json)
# print the JSON string representation of the object
print(ProductionVersionsAPIOperationRequestDTO.to_json())

# convert the object into a dict
production_versions_api_operation_request_dto_dict = production_versions_api_operation_request_dto_instance.to_dict()
# create an instance of ProductionVersionsAPIOperationRequestDTO from a dict
production_versions_api_operation_request_dto_from_dict = ProductionVersionsAPIOperationRequestDTO.from_dict(production_versions_api_operation_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


