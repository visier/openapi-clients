# coding: utf-8

"""
    Visier Data and Job Handling APIs

    Visier APIs for data and job handling

    The version of the OpenAPI document: 22222222.99201.1389
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.api.data_handling.models.success_factors_auth_params_dto import SuccessFactorsAuthParamsDTO

class TestSuccessFactorsAuthParamsDTO(unittest.TestCase):
    """SuccessFactorsAuthParamsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SuccessFactorsAuthParamsDTO:
        """Test SuccessFactorsAuthParamsDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SuccessFactorsAuthParamsDTO`
        """
        model = SuccessFactorsAuthParamsDTO()
        if include_optional:
            return SuccessFactorsAuthParamsDTO(
                company_id = '',
                host_domain_name = '',
                o_auth = visier.api.data_handling.models.success_factors_o_auth_params_dto.SuccessFactorsOAuthParamsDTO(
                    api_key = '', 
                    private_x509_key = '', 
                    public_x509_cert = '', ),
                password = '',
                username = ''
            )
        else:
            return SuccessFactorsAuthParamsDTO(
        )
        """

    def testSuccessFactorsAuthParamsDTO(self):
        """Test SuccessFactorsAuthParamsDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
