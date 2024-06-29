# coding: utf-8

"""
    Visier Public Platform APIs

    Visier APIs for querying data and model metadata

    The version of the OpenAPI document: 22222222.99201.1081
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.model_query.models.dimensions_dto import DimensionsDTO

class TestDimensionsDTO(unittest.TestCase):
    """DimensionsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DimensionsDTO:
        """Test DimensionsDTO
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DimensionsDTO`
        """
        model = DimensionsDTO()
        if include_optional:
            return DimensionsDTO(
                dimensions = [
                    visier.model_query.models.dimension_dto.DimensionDTO(
                        id = '', 
                        display_name = '', 
                        description = '', 
                        levels = [
                            visier.model_query.models.level_dto.LevelDTO(
                                id = '', 
                                display_name = '', 
                                depth = 56, )
                            ], 
                        unknown_member = [
                            ''
                            ], 
                        member_count = 56, 
                        visible_in_app = True, )
                    ]
            )
        else:
            return DimensionsDTO(
        )
        """

    def testDimensionsDTO(self):
        """Test DimensionsDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
