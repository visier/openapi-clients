# coding: utf-8

"""
    Visier System Status APIs

    Visier APIs for checking the health and status of Visier's platform and services.

    The version of the OpenAPI document: 22222222.99201.1389
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.api.system_status.models.system_status_dto import SystemStatusDTO

class TestSystemStatusDTO(unittest.TestCase):
    """SystemStatusDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SystemStatusDTO:
        """Test SystemStatusDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SystemStatusDTO`
        """
        model = SystemStatusDTO()
        if include_optional:
            return SystemStatusDTO(
                overall = ''
            )
        else:
            return SystemStatusDTO(
        )
        """

    def testSystemStatusDTO(self):
        """Test SystemStatusDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
