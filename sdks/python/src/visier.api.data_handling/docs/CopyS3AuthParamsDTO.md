# CopyS3AuthParamsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iam_role** | **str** |  | [optional] 

## Example

```python
from visier.api.data_handling.models.copy_s3_auth_params_dto import CopyS3AuthParamsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CopyS3AuthParamsDTO from a JSON string
copy_s3_auth_params_dto_instance = CopyS3AuthParamsDTO.from_json(json)
# print the JSON string representation of the object
print(CopyS3AuthParamsDTO.to_json())

# convert the object into a dict
copy_s3_auth_params_dto_dict = copy_s3_auth_params_dto_instance.to_dict()
# create an instance of CopyS3AuthParamsDTO from a dict
copy_s3_auth_params_dto_from_dict = CopyS3AuthParamsDTO.from_dict(copy_s3_auth_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


