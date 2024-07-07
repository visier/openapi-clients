# CurrencyRatesDTO

A collection of currency exchange rates.  Note: Currencies may have different exchange rates in different time intervals, depending what rate data is stored in Visier.  For example, USD:CAD can be 1.2 between January 1 - March 1, while USD:EUR can be 0.92 between January 1 - February 1, but 0.88 between February  1 - March 1.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_rates** | [**List[CurrencyRateDTO]**](CurrencyRateDTO.md) |  | [optional] 

## Example

```python
from visier.model_query.models.currency_rates_dto import CurrencyRatesDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyRatesDTO from a JSON string
currency_rates_dto_instance = CurrencyRatesDTO.from_json(json)
# print the JSON string representation of the object
print(CurrencyRatesDTO.to_json())

# convert the object into a dict
currency_rates_dto_dict = currency_rates_dto_instance.to_dict()
# create an instance of CurrencyRatesDTO from a dict
currency_rates_dto_from_dict = CurrencyRatesDTO.from_dict(currency_rates_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


