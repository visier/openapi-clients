# coding: utf-8

"""
    Visier Tenant Management APIs

    Visier APIs for managing tenants

    The version of the OpenAPI document: 22222222.99201.1389
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.api.tenant_management.api.tenant_management_api import TenantManagementApi


class TestTenantManagementApi(unittest.TestCase):
    """TenantManagementApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TenantManagementApi()

    def tearDown(self) -> None:
        pass

    def test_create_tenant(self) -> None:
        """Test case for create_tenant

        Add an analytic tenant
        """
        pass

    def test_list_tenants(self) -> None:
        """Test case for list_tenants

        Retrieve a list of all analytic tenants
        """
        pass

    def test_tenant_info(self) -> None:
        """Test case for tenant_info

        Retrieve an analytic tenant's details
        """
        pass

    def test_update_tenant(self) -> None:
        """Test case for update_tenant

        Update an analytic tenant
        """
        pass


if __name__ == '__main__':
    unittest.main()