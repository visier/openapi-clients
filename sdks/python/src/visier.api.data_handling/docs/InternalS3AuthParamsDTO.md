# InternalS3AuthParamsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_name** | **str** |  | [optional] 
**path** | **str** |  | [optional] 

## Example

```python
from visier.api.data_handling.models.internal_s3_auth_params_dto import InternalS3AuthParamsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of InternalS3AuthParamsDTO from a JSON string
internal_s3_auth_params_dto_instance = InternalS3AuthParamsDTO.from_json(json)
# print the JSON string representation of the object
print(InternalS3AuthParamsDTO.to_json())

# convert the object into a dict
internal_s3_auth_params_dto_dict = internal_s3_auth_params_dto_instance.to_dict()
# create an instance of InternalS3AuthParamsDTO from a dict
internal_s3_auth_params_dto_from_dict = InternalS3AuthParamsDTO.from_dict(internal_s3_auth_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


