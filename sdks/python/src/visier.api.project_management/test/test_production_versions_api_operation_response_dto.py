# coding: utf-8

"""
    Visier Project Management APIs

    Visier APIs for managing and publishing projects

    The version of the OpenAPI document: 22222222.99201.1389
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.api.project_management.models.production_versions_api_operation_response_dto import ProductionVersionsAPIOperationResponseDTO

class TestProductionVersionsAPIOperationResponseDTO(unittest.TestCase):
    """ProductionVersionsAPIOperationResponseDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductionVersionsAPIOperationResponseDTO:
        """Test ProductionVersionsAPIOperationResponseDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductionVersionsAPIOperationResponseDTO`
        """
        model = ProductionVersionsAPIOperationResponseDTO()
        if include_optional:
            return ProductionVersionsAPIOperationResponseDTO(
                export = None
            )
        else:
            return ProductionVersionsAPIOperationResponseDTO(
        )
        """

    def testProductionVersionsAPIOperationResponseDTO(self):
        """Test ProductionVersionsAPIOperationResponseDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()