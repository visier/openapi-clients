# SlackAuthParamsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_code** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 

## Example

```python
from visier.api.data_handling.models.slack_auth_params_dto import SlackAuthParamsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SlackAuthParamsDTO from a JSON string
slack_auth_params_dto_instance = SlackAuthParamsDTO.from_json(json)
# print the JSON string representation of the object
print(SlackAuthParamsDTO.to_json())

# convert the object into a dict
slack_auth_params_dto_dict = slack_auth_params_dto_instance.to_dict()
# create an instance of SlackAuthParamsDTO from a dict
slack_auth_params_dto_from_dict = SlackAuthParamsDTO.from_dict(slack_auth_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


