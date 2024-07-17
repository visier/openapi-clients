# PropertyAccessConfigDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_level** | **str** | The access level of the property. Valid values are: &#x60;Aggregate&#x60;, &#x60;Detailed&#x60;.  * **Aggregate**: The property can only be accessed as part of an aggregate.  * **Detailed**: The property can be accessed at a detailed level. | [optional] 
**analytic_object_id** | **str** | The analytic object ID of the property. | [optional] 
**analytic_object_reference_paths** | **List[str]** | The path to the analytic object reference. Empty if the configuration is not a reference. | [optional] 
**property_id** | **str** | The property ID associated with the property access configuration. | [optional] 
**property_status** | **str** | The property&#39;s validity status. Valid values: &#x60;Valid&#x60;, &#x60;NoData&#x60;, &#x60;NotFound&#x60;.  * **Valid**: The object exists and has loaded data.  * **NoData**: The object exists but doesn&#39;t have loaded data.  * **NotFound**: The object doesn&#39;t exist. | [optional] 

## Example

```python
from visier.api.permission_management.models.property_access_config_dto import PropertyAccessConfigDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyAccessConfigDTO from a JSON string
property_access_config_dto_instance = PropertyAccessConfigDTO.from_json(json)
# print the JSON string representation of the object
print(PropertyAccessConfigDTO.to_json())

# convert the object into a dict
property_access_config_dto_dict = property_access_config_dto_instance.to_dict()
# create an instance of PropertyAccessConfigDTO from a dict
property_access_config_dto_from_dict = PropertyAccessConfigDTO.from_dict(property_access_config_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


