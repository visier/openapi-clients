# DirectDataTransactionStartResponseDTO

The response after successfully creating a transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | The transaction&#39;s unique identifier. | [optional] 

## Example

```python
from visier.api.direct_data_intake.models.direct_data_transaction_start_response_dto import DirectDataTransactionStartResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DirectDataTransactionStartResponseDTO from a JSON string
direct_data_transaction_start_response_dto_instance = DirectDataTransactionStartResponseDTO.from_json(json)
# print the JSON string representation of the object
print(DirectDataTransactionStartResponseDTO.to_json())

# convert the object into a dict
direct_data_transaction_start_response_dto_dict = direct_data_transaction_start_response_dto_instance.to_dict()
# create an instance of DirectDataTransactionStartResponseDTO from a dict
direct_data_transaction_start_response_dto_from_dict = DirectDataTransactionStartResponseDTO.from_dict(direct_data_transaction_start_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


