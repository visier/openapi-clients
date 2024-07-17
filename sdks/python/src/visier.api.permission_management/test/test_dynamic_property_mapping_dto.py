# coding: utf-8

"""
    Visier Permission Management APIs

    Visier APIs for managing permissions within an organization

    The version of the OpenAPI document: 22222222.99201.1389
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.api.permission_management.models.dynamic_property_mapping_dto import DynamicPropertyMappingDTO

class TestDynamicPropertyMappingDTO(unittest.TestCase):
    """DynamicPropertyMappingDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DynamicPropertyMappingDTO:
        """Test DynamicPropertyMappingDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DynamicPropertyMappingDTO`
        """
        model = DynamicPropertyMappingDTO()
        if include_optional:
            return DynamicPropertyMappingDTO(
                hierarchy_property_id = '',
                hierarchy_property_status = 'Unset',
                user_property = visier.api.permission_management.models.user_property_dto.UserPropertyDTO(
                    name = '', )
            )
        else:
            return DynamicPropertyMappingDTO(
        )
        """

    def testDynamicPropertyMappingDTO(self):
        """Test DynamicPropertyMappingDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()