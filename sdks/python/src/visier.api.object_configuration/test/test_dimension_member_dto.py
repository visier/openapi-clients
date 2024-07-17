# coding: utf-8

"""
    Visier Object Configuration APIs

    Visier APIs for managing objects in studio experience

    The version of the OpenAPI document: 22222222.99201.1389
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.api.object_configuration.models.dimension_member_dto import DimensionMemberDTO

class TestDimensionMemberDTO(unittest.TestCase):
    """DimensionMemberDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DimensionMemberDTO:
        """Test DimensionMemberDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DimensionMemberDTO`
        """
        model = DimensionMemberDTO()
        if include_optional:
            return DimensionMemberDTO(
                dimension_member = [
                    ''
                    ]
            )
        else:
            return DimensionMemberDTO(
        )
        """

    def testDimensionMemberDTO(self):
        """Test DimensionMemberDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()