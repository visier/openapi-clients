# SubjectMissingAccessDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **List[str]** | The attributes that cannot be accessed. | [optional] 
**subject** | **str** | The subjects that cannot be accessed. | [optional] 

## Example

```python
from visier.api.data_handling.models.subject_missing_access_dto import SubjectMissingAccessDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SubjectMissingAccessDTO from a JSON string
subject_missing_access_dto_instance = SubjectMissingAccessDTO.from_json(json)
# print the JSON string representation of the object
print(SubjectMissingAccessDTO.to_json())

# convert the object into a dict
subject_missing_access_dto_dict = subject_missing_access_dto_instance.to_dict()
# create an instance of SubjectMissingAccessDTO from a dict
subject_missing_access_dto_from_dict = SubjectMissingAccessDTO.from_dict(subject_missing_access_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


