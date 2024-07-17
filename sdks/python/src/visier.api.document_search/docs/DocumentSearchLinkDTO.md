# DocumentSearchLinkDTO

Defines the attributes of a web request to reference documents in the search results.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The URL pointing to the specific document. | [optional] 
**verb** | **str** | The verb to use when formulating the web request. This is commonly &#x60;GET&#x60;. | [optional] 

## Example

```python
from visier.api.document_search.models.document_search_link_dto import DocumentSearchLinkDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSearchLinkDTO from a JSON string
document_search_link_dto_instance = DocumentSearchLinkDTO.from_json(json)
# print the JSON string representation of the object
print(DocumentSearchLinkDTO.to_json())

# convert the object into a dict
document_search_link_dto_dict = document_search_link_dto_instance.to_dict()
# create an instance of DocumentSearchLinkDTO from a dict
document_search_link_dto_from_dict = DocumentSearchLinkDTO.from_dict(document_search_link_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


