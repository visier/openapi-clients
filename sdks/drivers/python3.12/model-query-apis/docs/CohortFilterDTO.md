# CohortFilterDTO

Use a cohort filter to define a population as it existed during a specific time period.  Cohort filters allow you to define a population in terms of a collection of filters, known as a key group.  The cohort's defined time interval is independent of the query's time. The cohort's time interval is the  time at which the key group should be applied.  Cohorts are typically used to follow populations and understand changes to the population over time,  such as promotion and resignation rates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_group** | [**KeyGroupFilterDTO**](KeyGroupFilterDTO.md) | A key group is a collection of filters that define the shape of the analysis population. | [optional] 
**exclude** | **bool** | If true, the population is defined by those excluded by the filters. Default is false. | [optional] 
**time_interval** | [**QueryTimeIntervalDTO**](QueryTimeIntervalDTO.md) | The time at which to apply the key group, such as a specific day or period of months. | [optional] 

## Example

```python
from visier.model_query.models.cohort_filter_dto import CohortFilterDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CohortFilterDTO from a JSON string
cohort_filter_dto_instance = CohortFilterDTO.from_json(json)
# print the JSON string representation of the object
print(CohortFilterDTO.to_json())

# convert the object into a dict
cohort_filter_dto_dict = cohort_filter_dto_instance.to_dict()
# create an instance of CohortFilterDTO from a dict
cohort_filter_dto_from_dict = CohortFilterDTO.from_dict(cohort_filter_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


