# coding: utf-8

"""
    Visier Permission Management APIs

    Visier APIs for managing permissions within an organization

    The version of the OpenAPI document: 22222222.99201.1389
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.api.permission_management.models.permission_failure_dto import PermissionFailureDTO

class TestPermissionFailureDTO(unittest.TestCase):
    """PermissionFailureDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PermissionFailureDTO:
        """Test PermissionFailureDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PermissionFailureDTO`
        """
        model = PermissionFailureDTO()
        if include_optional:
            return PermissionFailureDTO(
                display_name = '',
                error = visier.api.permission_management.models.permission_error_dto.PermissionErrorDTO(
                    message = '', 
                    rci = '', ),
                permission_id = ''
            )
        else:
            return PermissionFailureDTO(
        )
        """

    def testPermissionFailureDTO(self):
        """Test PermissionFailureDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
