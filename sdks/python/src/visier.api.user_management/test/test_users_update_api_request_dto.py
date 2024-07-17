# coding: utf-8

"""
    Visier User Management APIs

    Visier APIs for managing users within an organization

    The version of the OpenAPI document: 22222222.99201.1389
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.api.user_management.models.users_update_api_request_dto import UsersUpdateAPIRequestDTO

class TestUsersUpdateAPIRequestDTO(unittest.TestCase):
    """UsersUpdateAPIRequestDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UsersUpdateAPIRequestDTO:
        """Test UsersUpdateAPIRequestDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UsersUpdateAPIRequestDTO`
        """
        model = UsersUpdateAPIRequestDTO()
        if include_optional:
            return UsersUpdateAPIRequestDTO(
                users = [
                    visier.api.user_management.models.users_update_api_user_dto.UsersUpdateAPIUserDTO(
                        account_enabled = '', 
                        display_name = '', 
                        email = '', 
                        employee_id = '', 
                        user_id = '', )
                    ]
            )
        else:
            return UsersUpdateAPIRequestDTO(
        )
        """

    def testUsersUpdateAPIRequestDTO(self):
        """Test UsersUpdateAPIRequestDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
