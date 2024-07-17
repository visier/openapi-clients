# GoogleSheetsAuthParamsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_code** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**configuration** | **str** |  | [optional] 

## Example

```python
from visier.api.data_handling.models.google_sheets_auth_params_dto import GoogleSheetsAuthParamsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleSheetsAuthParamsDTO from a JSON string
google_sheets_auth_params_dto_instance = GoogleSheetsAuthParamsDTO.from_json(json)
# print the JSON string representation of the object
print(GoogleSheetsAuthParamsDTO.to_json())

# convert the object into a dict
google_sheets_auth_params_dto_dict = google_sheets_auth_params_dto_instance.to_dict()
# create an instance of GoogleSheetsAuthParamsDTO from a dict
google_sheets_auth_params_dto_from_dict = GoogleSheetsAuthParamsDTO.from_dict(google_sheets_auth_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


