# CurrencyDTO

Information about a currency type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_code** | **str** | The ISO 4217 3-letter code for the currency. | [optional] 
**display_name** | **str** | The display name for the currency. | [optional] 
**symbol** | **str** | The symbol name for the currency. | [optional] 
**short_symbol** | **str** | The shortened symbol name for the currency.  Removes all alphabetic characters. If **symbol** only has alphabetic characters, **shortSymbol** is empty.  If **symbol** contains only non-alphabetic characters, **shortSymbol** is the same as **symbol**.  For example, if **symbol** is CA$, **shortSymbol** is $. If **symbol** is $, then **shortSymbol** is $. | [optional] 

## Example

```python
from visier.model_query.models.currency_dto import CurrencyDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyDTO from a JSON string
currency_dto_instance = CurrencyDTO.from_json(json)
# print the JSON string representation of the object
print(CurrencyDTO.to_json())

# convert the object into a dict
currency_dto_dict = currency_dto_instance.to_dict()
# create an instance of CurrencyDTO from a dict
currency_dto_from_dict = CurrencyDTO.from_dict(currency_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


