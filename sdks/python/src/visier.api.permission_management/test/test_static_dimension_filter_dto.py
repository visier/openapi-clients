# coding: utf-8

"""
    Visier Permission Management APIs

    Visier APIs for managing permissions within an organization

    The version of the OpenAPI document: 22222222.99201.1389
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.api.permission_management.models.static_dimension_filter_dto import StaticDimensionFilterDTO

class TestStaticDimensionFilterDTO(unittest.TestCase):
    """StaticDimensionFilterDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StaticDimensionFilterDTO:
        """Test StaticDimensionFilterDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StaticDimensionFilterDTO`
        """
        model = StaticDimensionFilterDTO()
        if include_optional:
            return StaticDimensionFilterDTO(
                dimension_id = '',
                dimension_status = 'Unset',
                member_selections = [
                    visier.api.permission_management.models.member_selection_dto.MemberSelectionDTO(
                        dimension_member_status = 'Unset', 
                        excluded = True, 
                        name_path = [
                            ''
                            ], )
                    ],
                subject_reference_path = [
                    ''
                    ]
            )
        else:
            return StaticDimensionFilterDTO(
        )
        """

    def testStaticDimensionFilterDTO(self):
        """Test StaticDimensionFilterDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
