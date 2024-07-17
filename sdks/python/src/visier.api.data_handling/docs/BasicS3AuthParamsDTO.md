# BasicS3AuthParamsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | **str** |  | [optional] 
**bucket_name** | **str** |  | [optional] 
**bucket_region** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**secret_key** | **str** |  | [optional] 

## Example

```python
from visier.api.data_handling.models.basic_s3_auth_params_dto import BasicS3AuthParamsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of BasicS3AuthParamsDTO from a JSON string
basic_s3_auth_params_dto_instance = BasicS3AuthParamsDTO.from_json(json)
# print the JSON string representation of the object
print(BasicS3AuthParamsDTO.to_json())

# convert the object into a dict
basic_s3_auth_params_dto_dict = basic_s3_auth_params_dto_instance.to_dict()
# create an instance of BasicS3AuthParamsDTO from a dict
basic_s3_auth_params_dto_from_dict = BasicS3AuthParamsDTO.from_dict(basic_s3_auth_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


