# coding: utf-8

"""
    Visier Object Configuration APIs

    Visier APIs for managing objects in studio experience

    The version of the OpenAPI document: 22222222.99201.1389
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.api.object_configuration.models.analytic_object_filter_dto import AnalyticObjectFilterDTO

class TestAnalyticObjectFilterDTO(unittest.TestCase):
    """AnalyticObjectFilterDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AnalyticObjectFilterDTO:
        """Test AnalyticObjectFilterDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AnalyticObjectFilterDTO`
        """
        model = AnalyticObjectFilterDTO()
        if include_optional:
            return AnalyticObjectFilterDTO(
                analytic_object_uuid = '',
                dimensions = [
                    visier.api.object_configuration.models.dimension_filter_dto.DimensionFilterDTO(
                        dimension_id = '', 
                        dimension_members = [
                            visier.api.object_configuration.models.dimension_member_dto.DimensionMemberDTO(
                                dimension_member = [
                                    ''
                                    ], )
                            ], 
                        symbol_name = '', )
                    ],
                symbol_name = ''
            )
        else:
            return AnalyticObjectFilterDTO(
        )
        """

    def testAnalyticObjectFilterDTO(self):
        """Test AnalyticObjectFilterDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
