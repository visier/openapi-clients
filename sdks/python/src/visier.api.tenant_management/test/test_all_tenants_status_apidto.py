# coding: utf-8

"""
    Visier Tenant Management APIs

    Visier APIs for managing tenants

    The version of the OpenAPI document: 22222222.99201.1389
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.api.tenant_management.models.all_tenants_status_apidto import AllTenantsStatusAPIDTO

class TestAllTenantsStatusAPIDTO(unittest.TestCase):
    """AllTenantsStatusAPIDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AllTenantsStatusAPIDTO:
        """Test AllTenantsStatusAPIDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AllTenantsStatusAPIDTO`
        """
        model = AllTenantsStatusAPIDTO()
        if include_optional:
            return AllTenantsStatusAPIDTO(
                limit = 56,
                start = 56,
                tenants = [
                    visier.api.tenant_management.models.tenant_detail_apidto.TenantDetailAPIDTO(
                        can_administer_other_tenants = True, 
                        current_data_version = '', 
                        custom_properties = [
                            visier.api.tenant_management.models.custom_tenant_property_dto.CustomTenantPropertyDTO(
                                key = '', 
                                value = '', )
                            ], 
                        data_version_date = '', 
                        embeddable_domains = [
                            ''
                            ], 
                        industry_code = 56, 
                        modules = [
                            visier.api.tenant_management.models.tenant_module_dto.TenantModuleDTO(
                                display_name = '', 
                                module_settings = null, 
                                symbol_name = '', )
                            ], 
                        provision_date = '', 
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
            return AllTenantsStatusAPIDTO(
        )
        """

    def testAllTenantsStatusAPIDTO(self):
        """Test AllTenantsStatusAPIDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
