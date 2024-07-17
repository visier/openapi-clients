# coding: utf-8

"""
    Visier Consolidated Analytics APIs

    Visier APIs for managing consolidated analytics (CA) tenants.

    The version of the OpenAPI document: 22222222.99201.1389
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.api.consolidated_analytics.models.consolidated_analytics_api_source_tenant_list_dto import ConsolidatedAnalyticsAPISourceTenantListDTO

class TestConsolidatedAnalyticsAPISourceTenantListDTO(unittest.TestCase):
    """ConsolidatedAnalyticsAPISourceTenantListDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConsolidatedAnalyticsAPISourceTenantListDTO:
        """Test ConsolidatedAnalyticsAPISourceTenantListDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConsolidatedAnalyticsAPISourceTenantListDTO`
        """
        model = ConsolidatedAnalyticsAPISourceTenantListDTO()
        if include_optional:
            return ConsolidatedAnalyticsAPISourceTenantListDTO(
                tenant_codes = [
                    ''
                    ]
            )
        else:
            return ConsolidatedAnalyticsAPISourceTenantListDTO(
        )
        """

    def testConsolidatedAnalyticsAPISourceTenantListDTO(self):
        """Test ConsolidatedAnalyticsAPISourceTenantListDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
