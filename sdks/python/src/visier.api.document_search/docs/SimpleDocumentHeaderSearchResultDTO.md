# SimpleDocumentHeaderSearchResultDTO

Structure of a single document header search using the Simple search operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The &#x60;Web Template Framework&#x60; representation of the search result element. This commonly displayed alongside the result by search portals. | [optional] 
**display_name** | **str** | The display name of the element in the search result. | [optional] 
**relevance** | **float** | The relevance of the search result and a number between &#x60;0&#x60; and &#x60;100&#x60;. | [optional] 
**view_link** | [**DocumentSearchLinkDTO**](DocumentSearchLinkDTO.md) | Use the &#x60;viewLink&#x60; to build a web request to view this document. | [optional] 

## Example

```python
from visier.api.document_search.models.simple_document_header_search_result_dto import SimpleDocumentHeaderSearchResultDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleDocumentHeaderSearchResultDTO from a JSON string
simple_document_header_search_result_dto_instance = SimpleDocumentHeaderSearchResultDTO.from_json(json)
# print the JSON string representation of the object
print(SimpleDocumentHeaderSearchResultDTO.to_json())

# convert the object into a dict
simple_document_header_search_result_dto_dict = simple_document_header_search_result_dto_instance.to_dict()
# create an instance of SimpleDocumentHeaderSearchResultDTO from a dict
simple_document_header_search_result_dto_from_dict = SimpleDocumentHeaderSearchResultDTO.from_dict(simple_document_header_search_result_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


