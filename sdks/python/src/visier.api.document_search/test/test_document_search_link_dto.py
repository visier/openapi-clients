# coding: utf-8

"""
    Visier Document Search API

    Visier API for searching for Visier documents

    The version of the OpenAPI document: 22222222.99201.1389
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.api.document_search.models.document_search_link_dto import DocumentSearchLinkDTO

class TestDocumentSearchLinkDTO(unittest.TestCase):
    """DocumentSearchLinkDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DocumentSearchLinkDTO:
        """Test DocumentSearchLinkDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DocumentSearchLinkDTO`
        """
        model = DocumentSearchLinkDTO()
        if include_optional:
            return DocumentSearchLinkDTO(
                href = '',
                verb = ''
            )
        else:
            return DocumentSearchLinkDTO(
        )
        """

    def testDocumentSearchLinkDTO(self):
        """Test DocumentSearchLinkDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()