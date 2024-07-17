# coding: utf-8

"""
    Visier User Management APIs

    Visier APIs for managing users within an organization

    The version of the OpenAPI document: 22222222.99201.1389
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.api.user_management.models.user_groups_get_api_response_dto import UserGroupsGetAPIResponseDTO

class TestUserGroupsGetAPIResponseDTO(unittest.TestCase):
    """UserGroupsGetAPIResponseDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserGroupsGetAPIResponseDTO:
        """Test UserGroupsGetAPIResponseDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserGroupsGetAPIResponseDTO`
        """
        model = UserGroupsGetAPIResponseDTO()
        if include_optional:
            return UserGroupsGetAPIResponseDTO(
                limit = 56,
                start = 56,
                user_groups = [
                    visier.api.user_management.models.user_group_get_api_response_dto.UserGroupGetAPIResponseDTO(
                        display_name = '', 
                        permissions = [
                            visier.api.user_management.models.permission_response_dto.PermissionResponseDTO(
                                display_name = '', 
                                permission_id = '', )
                            ], 
                        user_group_id = '', )
                    ]
            )
        else:
            return UserGroupsGetAPIResponseDTO(
        )
        """

    def testUserGroupsGetAPIResponseDTO(self):
        """Test UserGroupsGetAPIResponseDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
