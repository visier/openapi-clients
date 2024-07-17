# DataTransferResultDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_size** | **str** | The total size of the transfer session in bytes. | [optional] 
**rows** | **str** | The total number of rows transferred during the transfer session. | [optional] 
**source_names** | **List[str]** | A list of strings representing the sources that received a data transfer. | [optional] 
**tenant_code** | **str** | The code of the tenant that data was transferred to. For example, WFF_j1r or WFF_j1r~c7o. | [optional] 

## Example

```python
from visier.api.data_intake.models.data_transfer_result_detail import DataTransferResultDetail

# TODO update the JSON string below
json = "{}"
# create an instance of DataTransferResultDetail from a JSON string
data_transfer_result_detail_instance = DataTransferResultDetail.from_json(json)
# print the JSON string representation of the object
print(DataTransferResultDetail.to_json())

# convert the object into a dict
data_transfer_result_detail_dict = data_transfer_result_detail_instance.to_dict()
# create an instance of DataTransferResultDetail from a dict
data_transfer_result_detail_from_dict = DataTransferResultDetail.from_dict(data_transfer_result_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


