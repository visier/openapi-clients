# CurrencyRateDTO

Information about a currency exchange rate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time** | **str** | The latest time instant to retrieve exchange rates from.  **Note:** Format is the number of milliseconds since Jan 1, 1970 12:00 AM UTC. | [optional] 
**from_currency_code** | **str** | The currency to convert **from**.  **Note:** If USD is the &#x60;fromCurrencyCode&#x60;, you are retrieving the exchange rates from USD to a different currency. | [optional] 
**rate** | **float** | The numeric value of the exchange rate.  **Note:** If **decimals** is specified, rate rounds to that value. If **decimals** is undefined, **rate** rounds to 2 significant figures after the decimal point. | [optional] 
**start_time** | **str** | The earliest time instant to retrieve exchange rates from.  **Note:** Format is the number of milliseconds since Jan 1, 1970 12:00 AM UTC. | [optional] 
**to_currency_code** | **str** | The currency to convert **to**.  **Note:** If USD is the &#x60;toCurrencyCode&#x60;, you are retrieving the exchange rates from a different currency to USD. | [optional] 

## Example

```python
from visier.model_query_apis.models.currency_rate_dto import CurrencyRateDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyRateDTO from a JSON string
currency_rate_dto_instance = CurrencyRateDTO.from_json(json)
# print the JSON string representation of the object
print(CurrencyRateDTO.to_json())

# convert the object into a dict
currency_rate_dto_dict = currency_rate_dto_instance.to_dict()
# create an instance of CurrencyRateDTO from a dict
currency_rate_dto_from_dict = CurrencyRateDTO.from_dict(currency_rate_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


