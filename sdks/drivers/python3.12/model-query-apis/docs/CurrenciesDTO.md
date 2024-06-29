# CurrenciesDTO

A collection of currencies.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currencies** | [**List[CurrencyDTO]**](CurrencyDTO.md) |  | [optional] 

## Example

```python
from visier.model_query.models.currencies_dto import CurrenciesDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CurrenciesDTO from a JSON string
currencies_dto_instance = CurrenciesDTO.from_json(json)
# print the JSON string representation of the object
print(CurrenciesDTO.to_json())

# convert the object into a dict
currencies_dto_dict = currencies_dto_instance.to_dict()
# create an instance of CurrenciesDTO from a dict
currencies_dto_from_dict = CurrenciesDTO.from_dict(currencies_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


