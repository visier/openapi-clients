# coding: utf-8

"""
    Visier Permission Management APIs

    Visier APIs for managing permissions within an organization

    The version of the OpenAPI document: 22222222.99201.1389
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.api.permission_management.models.bulk_data_access_set_response_dto import BulkDataAccessSetResponseDTO

class TestBulkDataAccessSetResponseDTO(unittest.TestCase):
    """BulkDataAccessSetResponseDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BulkDataAccessSetResponseDTO:
        """Test BulkDataAccessSetResponseDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BulkDataAccessSetResponseDTO`
        """
        model = BulkDataAccessSetResponseDTO()
        if include_optional:
            return BulkDataAccessSetResponseDTO(
                failures = [
                    visier.api.permission_management.models.data_access_set_failure_dto.DataAccessSetFailureDTO(
                        data_access_set_id = '', 
                        display_name = '', 
                        error = null, )
                    ],
                successes = [
                    visier.api.permission_management.models.data_access_set_success_dto.DataAccessSetSuccessDTO(
                        data_access_set_id = '', 
                        display_name = '', )
                    ]
            )
        else:
            return BulkDataAccessSetResponseDTO(
        )
        """

    def testBulkDataAccessSetResponseDTO(self):
        """Test BulkDataAccessSetResponseDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()