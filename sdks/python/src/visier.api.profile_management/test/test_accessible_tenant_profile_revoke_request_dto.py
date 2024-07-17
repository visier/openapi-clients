# coding: utf-8

"""
    Visier Profile Management APIs

    Visier APIs for managing the profiles assigned to users

    The version of the OpenAPI document: 22222222.99201.1389
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.api.profile_management.models.accessible_tenant_profile_revoke_request_dto import AccessibleTenantProfileRevokeRequestDTO

class TestAccessibleTenantProfileRevokeRequestDTO(unittest.TestCase):
    """AccessibleTenantProfileRevokeRequestDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccessibleTenantProfileRevokeRequestDTO:
        """Test AccessibleTenantProfileRevokeRequestDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccessibleTenantProfileRevokeRequestDTO`
        """
        model = AccessibleTenantProfileRevokeRequestDTO()
        if include_optional:
            return AccessibleTenantProfileRevokeRequestDTO(
                target_tenant_codes = [
                    visier.api.profile_management.models.target_tenant_code_dto.TargetTenantCodeDTO(
                        for_all_children = True, 
                        tenant_code = '', )
                    ],
                target_user_ids = [
                    ''
                    ]
            )
        else:
            return AccessibleTenantProfileRevokeRequestDTO(
        )
        """

    def testAccessibleTenantProfileRevokeRequestDTO(self):
        """Test AccessibleTenantProfileRevokeRequestDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()