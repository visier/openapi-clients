# JiraAuthParamsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_token** | **str** |  | [optional] 
**connect_params** | [**JiraConnectParamsDTO**](JiraConnectParamsDTO.md) |  | [optional] 
**host_name** | **str** |  | [optional] 

## Example

```python
from visier.api.data_handling.models.jira_auth_params_dto import JiraAuthParamsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of JiraAuthParamsDTO from a JSON string
jira_auth_params_dto_instance = JiraAuthParamsDTO.from_json(json)
# print the JSON string representation of the object
print(JiraAuthParamsDTO.to_json())

# convert the object into a dict
jira_auth_params_dto_dict = jira_auth_params_dto_instance.to_dict()
# create an instance of JiraAuthParamsDTO from a dict
jira_auth_params_dto_from_dict = JiraAuthParamsDTO.from_dict(jira_auth_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


