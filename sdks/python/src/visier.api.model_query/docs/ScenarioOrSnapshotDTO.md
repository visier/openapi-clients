# ScenarioOrSnapshotDTO

The unique identifier and display name for plan scenarios and snapshots.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The scenario or snapshot display name. | [optional] 
**id** | **str** | The identifier of the scenario or snapshot. | [optional] 

## Example

```python
from visier.api.model_query.models.scenario_or_snapshot_dto import ScenarioOrSnapshotDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ScenarioOrSnapshotDTO from a JSON string
scenario_or_snapshot_dto_instance = ScenarioOrSnapshotDTO.from_json(json)
# print the JSON string representation of the object
print(ScenarioOrSnapshotDTO.to_json())

# convert the object into a dict
scenario_or_snapshot_dto_dict = scenario_or_snapshot_dto_instance.to_dict()
# create an instance of ScenarioOrSnapshotDTO from a dict
scenario_or_snapshot_dto_from_dict = ScenarioOrSnapshotDTO.from_dict(scenario_or_snapshot_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


