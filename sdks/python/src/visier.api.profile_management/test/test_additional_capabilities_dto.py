# coding: utf-8

"""
    Visier Profile Management APIs

    Visier APIs for managing the profiles assigned to users

    The version of the OpenAPI document: 22222222.99201.1389
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.api.profile_management.models.additional_capabilities_dto import AdditionalCapabilitiesDTO

class TestAdditionalCapabilitiesDTO(unittest.TestCase):
    """AdditionalCapabilitiesDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdditionalCapabilitiesDTO:
        """Test AdditionalCapabilitiesDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdditionalCapabilitiesDTO`
        """
        model = AdditionalCapabilitiesDTO()
        if include_optional:
            return AdditionalCapabilitiesDTO(
                additional_capabilities = [
                    ''
                    ]
            )
        else:
            return AdditionalCapabilitiesDTO(
        )
        """

    def testAdditionalCapabilitiesDTO(self):
        """Test AdditionalCapabilitiesDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
