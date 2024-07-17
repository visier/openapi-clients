# coding: utf-8

"""
    Visier Data and Job Handling APIs

    Visier APIs for data and job handling

    The version of the OpenAPI document: 22222222.99201.1389
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.api.data_handling.models.google_sheets_auth_params_dto import GoogleSheetsAuthParamsDTO

class TestGoogleSheetsAuthParamsDTO(unittest.TestCase):
    """GoogleSheetsAuthParamsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GoogleSheetsAuthParamsDTO:
        """Test GoogleSheetsAuthParamsDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GoogleSheetsAuthParamsDTO`
        """
        model = GoogleSheetsAuthParamsDTO()
        if include_optional:
            return GoogleSheetsAuthParamsDTO(
                auth_code = '',
                client_id = '',
                client_secret = '',
                configuration = ''
            )
        else:
            return GoogleSheetsAuthParamsDTO(
        )
        """

    def testGoogleSheetsAuthParamsDTO(self):
        """Test GoogleSheetsAuthParamsDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
