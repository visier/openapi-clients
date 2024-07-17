# coding: utf-8

"""
    Visier Project Management APIs

    Visier APIs for managing and publishing projects

    The version of the OpenAPI document: 22222222.99201.1389
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.api.project_management.models.project_operation_response_dto import ProjectOperationResponseDTO

class TestProjectOperationResponseDTO(unittest.TestCase):
    """ProjectOperationResponseDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProjectOperationResponseDTO:
        """Test ProjectOperationResponseDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectOperationResponseDTO`
        """
        model = ProjectOperationResponseDTO()
        if include_optional:
            return ProjectOperationResponseDTO(
                commit_and_publish = visier.api.project_management.models.commit_and_publish_operation_response_dto.CommitAndPublishOperationResponseDTO(
                    published_version = null, )
            )
        else:
            return ProjectOperationResponseDTO(
        )
        """

    def testProjectOperationResponseDTO(self):
        """Test ProjectOperationResponseDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
