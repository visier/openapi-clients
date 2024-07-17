# coding: utf-8

"""
    Visier Data Intake APIs

    Visier APIs for sending raw or untransformed source data to Visier

    The version of the OpenAPI document: 22222222.99201.1389
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.api.data_intake.models.tenant import Tenant

class TestTenant(unittest.TestCase):
    """Tenant unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Tenant:
        """Test Tenant
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Tenant`
        """
        model = Tenant()
        if include_optional:
            return Tenant(
                sources = [
                    visier.api.data_intake.models.source.Source(
                        data_size = '', 
                        message = '', 
                        rows = '', 
                        source_id = '', 
                        source_name = '', 
                        status = '', )
                    ],
                status = '',
                tenant_code = ''
            )
        else:
            return Tenant(
        )
        """

    def testTenant(self):
        """Test Tenant"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
