# DataSecurityProfileDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_data_point_access** | **bool** | If &#x60;true&#x60;, the permission grants access to the entire population. If &#x60;false&#x60;, define &#x60;memberFilterConfigs&#x60; to set custom population access. | [optional] 
**analytic_object_id** | **str** | The unique ID of the analytic object assigned data security in this permission. | [optional] 
**inherited_access_configs** | [**List[InheritedAccessConfigDTO]**](InheritedAccessConfigDTO.md) | The events and related objects inherited from the analytic object.  By default, all events and related objects associated with the analytic object will be inherited from the analytic object in a permission.  For example, if you assign access to Employee, then access to the Employee Exit event is inherited in the permission.  To remove access to an event or related object, add the object to &#x60;inheritedAccessConfigs&#x60; with &#x60;removeAccess&#x60;: true.  To add custom filters to an event or related object, add the object to &#x60;inheritedAccessConfigs&#x60; and define &#x60;memberFilterConfigs&#x60;. | [optional] 
**inherited_reference_member_filter_config** | [**InheritedReferenceMemberFilterConfigDTO**](InheritedReferenceMemberFilterConfigDTO.md) | Configures the analytic object to inherit population access filters from. The target analytic object must be assigned population access in the permission and have a binding (strong) reference from the source analytic object.  * For example, assume &#x60;Applicant&#x60; -&gt; &#x60;Requisition&#x60; is configured to be a binding (strong) reference.  For &#x60;Applicant&#x60; (source analytic object) to inherit population access filters from &#x60;Requisition&#x60; (target analytic object), in the Applicant &#x60;dataSecurityProfile&#x60;, set &#x60;inheritedReferenceMemberFilterConfig&#x60; to &#x60;Requisition&#x60;. In this example, Applicant will inherit filters from Requisition because Requsition is assigned data security in this permission and there is a binding (strong) reference from Applicant to Requisition. | [optional] 
**member_filter_configs** | [**List[MemberFilterConfigDTO]**](MemberFilterConfigDTO.md) | Custom filters that define population access for an item in the permission. | [optional] 
**property_set_config** | [**PropertySetConfigDTO**](PropertySetConfigDTO.md) | A list of objects representing the data access for an analytic object’s properties. | [optional] 

## Example

```python
from visier.api.permission_management.models.data_security_profile_dto import DataSecurityProfileDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DataSecurityProfileDTO from a JSON string
data_security_profile_dto_instance = DataSecurityProfileDTO.from_json(json)
# print the JSON string representation of the object
print(DataSecurityProfileDTO.to_json())

# convert the object into a dict
data_security_profile_dto_dict = data_security_profile_dto_instance.to_dict()
# create an instance of DataSecurityProfileDTO from a dict
data_security_profile_dto_from_dict = DataSecurityProfileDTO.from_dict(data_security_profile_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


