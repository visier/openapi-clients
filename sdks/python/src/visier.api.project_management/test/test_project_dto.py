# coding: utf-8

"""
    Visier Project Management APIs

    Visier APIs for managing and publishing projects

    The version of the OpenAPI document: 22222222.99201.1389
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.api.project_management.models.project_dto import ProjectDTO

class TestProjectDTO(unittest.TestCase):
    """ProjectDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProjectDTO:
        """Test ProjectDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectDTO`
        """
        model = ProjectDTO()
        if include_optional:
            return ProjectDTO(
                capabilities = [
                    'canRead'
                    ],
                description = '',
                id = '',
                name = '',
                release_version = '',
                ticket_number = '',
                version_number = 56
            )
        else:
            return ProjectDTO(
        )
        """

    def testProjectDTO(self):
        """Test ProjectDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
