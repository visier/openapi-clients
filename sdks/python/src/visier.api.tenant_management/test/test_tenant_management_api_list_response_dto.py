# coding: utf-8

"""
    Visier Tenant Management APIs

    Visier APIs for managing tenants

    The version of the OpenAPI document: 22222222.99201.1389
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.api.tenant_management.models.tenant_management_api_list_response_dto import TenantManagementAPIListResponseDTO

class TestTenantManagementAPIListResponseDTO(unittest.TestCase):
    """TenantManagementAPIListResponseDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TenantManagementAPIListResponseDTO:
        """Test TenantManagementAPIListResponseDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TenantManagementAPIListResponseDTO`
        """
        model = TenantManagementAPIListResponseDTO()
        if include_optional:
            return TenantManagementAPIListResponseDTO(
                limit = 56,
                start = 56,
                tenants = [
                    visier.api.tenant_management.models.tenant_management_api_get_response_dto.TenantManagementAPIGetResponseDTO(
                        can_administer_other_tenants = True, 
                        click_through_link = '', 
                        click_through_link_enabled = '', 
                        current_data_version = '', 
                        custom_properties = [
                            visier.api.tenant_management.models.custom_property_dto.CustomPropertyDTO(
                                key = '', 
                                value = '', )
                            ], 
                        data_version_date = '', 
                        default_currency = '', 
                        embeddable_domains = [
                            ''
                            ], 
                        home_analysis_by_user_group = [
                            visier.api.tenant_management.models.home_analysis_by_user_group_dto.HomeAnalysisByUserGroupDTO(
                                home_analysis_id = '', 
                                user_group_id = '', )
                            ], 
                        home_analysis_id = '', 
                        industry_code = 56, 
                        primary_business_location = null, 
                        provision_date = '', 
                        purchased_modules = [
                            ''
                            ], 
                        sso_instance_issuers = [
                            ''
                            ], 
                        status = '', 
                        tenant_code = '', 
                        tenant_display_name = '', 
                        vanity_url_name = '', )
                    ]
            )
        else:
            return TenantManagementAPIListResponseDTO(
        )
        """

    def testTenantManagementAPIListResponseDTO(self):
        """Test TenantManagementAPIListResponseDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()