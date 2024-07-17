# ExportProductionVersionsAPIOperationParametersDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_version** | **str** | The unique identifier of the version to stop exporting versions at. The range is inclusive. | [optional] 
**excluded_versions** | **List[str]** | A list of versions between &#x60;startVersion&#x60; and &#x60;endVersion&#x60; to exclude. | [optional] 
**start_version** | **str** | The unique identifier of the version to start exporting versions from. The range is inclusive. | [optional] 

## Example

```python
from visier.api.project_management.models.export_production_versions_api_operation_parameters_dto import ExportProductionVersionsAPIOperationParametersDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ExportProductionVersionsAPIOperationParametersDTO from a JSON string
export_production_versions_api_operation_parameters_dto_instance = ExportProductionVersionsAPIOperationParametersDTO.from_json(json)
# print the JSON string representation of the object
print(ExportProductionVersionsAPIOperationParametersDTO.to_json())

# convert the object into a dict
export_production_versions_api_operation_parameters_dto_dict = export_production_versions_api_operation_parameters_dto_instance.to_dict()
# create an instance of ExportProductionVersionsAPIOperationParametersDTO from a dict
export_production_versions_api_operation_parameters_dto_from_dict = ExportProductionVersionsAPIOperationParametersDTO.from_dict(export_production_versions_api_operation_parameters_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


