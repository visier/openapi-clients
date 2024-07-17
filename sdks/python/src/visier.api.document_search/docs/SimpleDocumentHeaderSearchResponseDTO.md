# SimpleDocumentHeaderSearchResponseDTO

The response body structure for Simple document header search operations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_headers** | [**List[SimpleDocumentHeaderSearchResultDTO]**](SimpleDocumentHeaderSearchResultDTO.md) | The ordered collection of document header search results. The results are sorted according to their relevance in a descending order. | [optional] 

## Example

```python
from visier.api.document_search.models.simple_document_header_search_response_dto import SimpleDocumentHeaderSearchResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleDocumentHeaderSearchResponseDTO from a JSON string
simple_document_header_search_response_dto_instance = SimpleDocumentHeaderSearchResponseDTO.from_json(json)
# print the JSON string representation of the object
print(SimpleDocumentHeaderSearchResponseDTO.to_json())

# convert the object into a dict
simple_document_header_search_response_dto_dict = simple_document_header_search_response_dto_instance.to_dict()
# create an instance of SimpleDocumentHeaderSearchResponseDTO from a dict
simple_document_header_search_response_dto_from_dict = SimpleDocumentHeaderSearchResponseDTO.from_dict(simple_document_header_search_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


