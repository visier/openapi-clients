# JiraConnectParamsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_key** | **str** |  | [optional] 
**client_key** | **str** |  | [optional] 
**shared_secret** | **str** |  | [optional] 

## Example

```python
from visier.api.data_handling.models.jira_connect_params_dto import JiraConnectParamsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of JiraConnectParamsDTO from a JSON string
jira_connect_params_dto_instance = JiraConnectParamsDTO.from_json(json)
# print the JSON string representation of the object
print(JiraConnectParamsDTO.to_json())

# convert the object into a dict
jira_connect_params_dto_dict = jira_connect_params_dto_instance.to_dict()
# create an instance of JiraConnectParamsDTO from a dict
jira_connect_params_dto_from_dict = JiraConnectParamsDTO.from_dict(jira_connect_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


