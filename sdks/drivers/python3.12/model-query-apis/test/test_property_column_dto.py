# coding: utf-8

"""
    Visier Public Platform APIs

    Visier APIs for querying data and model metadata

    The version of the OpenAPI document: 22222222.99201.1371
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.model_query.models.property_column_dto import PropertyColumnDTO

class TestPropertyColumnDTO(unittest.TestCase):
    """PropertyColumnDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PropertyColumnDTO:
        """Test PropertyColumnDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PropertyColumnDTO`
        """
        model = PropertyColumnDTO()
        if include_optional:
            return PropertyColumnDTO(
                column_name = '',
                column_definition = visier.model_query.models.query_property_dto.QueryPropertyDTO(
                    formula = '', 
                    property = null, 
                    selection_concept = null, 
                    dimension = null, 
                    member_map_property = null, 
                    effective_date_property = null, )
            )
        else:
            return PropertyColumnDTO(
        )
        """

    def testPropertyColumnDTO(self):
        """Test PropertyColumnDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
