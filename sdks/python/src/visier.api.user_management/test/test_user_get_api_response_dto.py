# coding: utf-8

"""
    Visier User Management APIs

    Visier APIs for managing users within an organization

    The version of the OpenAPI document: 22222222.99201.1389
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.api.user_management.models.user_get_api_response_dto import UserGetAPIResponseDTO

class TestUserGetAPIResponseDTO(unittest.TestCase):
    """UserGetAPIResponseDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserGetAPIResponseDTO:
        """Test UserGetAPIResponseDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserGetAPIResponseDTO`
        """
        model = UserGetAPIResponseDTO()
        if include_optional:
            return UserGetAPIResponseDTO(
                account_enabled = True,
                display_name = '',
                email = '',
                employee_id = '',
                last_login = visier.api.user_management.models.last_login_dto.LastLoginDTO(
                    timestamp = '', ),
                permissions = visier.api.user_management.models.all_permissions_assigned_for_local_tenant_dto.AllPermissionsAssignedForLocalTenantDTO(
                    assigned_permissions = [
                        visier.api.user_management.models.permission_assigned_for_local_tenant_dto.PermissionAssignedForLocalTenantDTO(
                            description = '', 
                            display_name = '', 
                            permission_id = '', )
                        ], ),
                profiles = visier.api.user_management.models.all_profile_assigned_for_local_tenant_dto.AllProfileAssignedForLocalTenantDTO(
                    assigned_profiles = [
                        visier.api.user_management.models.profile_assigned_for_local_tenant_dto.ProfileAssignedForLocalTenantDTO(
                            additional_capabilities = null, 
                            capabilities = [
                                visier.api.user_management.models.capabilities_dto.CapabilitiesDTO(
                                    access_level = '', 
                                    capability = '', 
                                    view_level = '', )
                                ], 
                            display_name = '', 
                            profile_id = '', 
                            validity_end_time = '', 
                            validity_start_time = '', )
                        ], ),
                user_groups = visier.api.user_management.models.all_user_groups_assigned_for_local_tenant_dto.AllUserGroupsAssignedForLocalTenantDTO(
                    assigned_user_groups = [
                        visier.api.user_management.models.user_group_assigned_for_local_tenant_dto.UserGroupAssignedForLocalTenantDTO(
                            display_name = '', 
                            user_group_id = '', )
                        ], ),
                user_id = '',
                username = ''
            )
        else:
            return UserGetAPIResponseDTO(
        )
        """

    def testUserGetAPIResponseDTO(self):
        """Test UserGetAPIResponseDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
