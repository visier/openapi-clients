# BusinessLocationDTO

The location of operations or where business is performed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** | The country in which the business is located or business is performed. The country code must follow ISO 3166 standards in alpha-2 format (two-letter code). | [optional] 
**postal_code** | **str** | The postal code associated with the business location. Cannot be blank. | [optional] 

## Example

```python
from visier.api.tenant_management.models.business_location_dto import BusinessLocationDTO

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessLocationDTO from a JSON string
business_location_dto_instance = BusinessLocationDTO.from_json(json)
# print the JSON string representation of the object
print(BusinessLocationDTO.to_json())

# convert the object into a dict
business_location_dto_dict = business_location_dto_instance.to_dict()
# create an instance of BusinessLocationDTO from a dict
business_location_dto_from_dict = BusinessLocationDTO.from_dict(business_location_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


