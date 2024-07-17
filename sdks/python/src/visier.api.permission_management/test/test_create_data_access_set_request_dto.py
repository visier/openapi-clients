# coding: utf-8

"""
    Visier Permission Management APIs

    Visier APIs for managing permissions within an organization

    The version of the OpenAPI document: 22222222.99201.1389
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.api.permission_management.models.create_data_access_set_request_dto import CreateDataAccessSetRequestDTO

class TestCreateDataAccessSetRequestDTO(unittest.TestCase):
    """CreateDataAccessSetRequestDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateDataAccessSetRequestDTO:
        """Test CreateDataAccessSetRequestDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateDataAccessSetRequestDTO`
        """
        model = CreateDataAccessSetRequestDTO()
        if include_optional:
            return CreateDataAccessSetRequestDTO(
                shareable_property_access_configs = [
                    visier.api.permission_management.models.data_access_set_dto.DataAccessSetDTO(
                        analytic_object_id = '', 
                        description = '', 
                        display_name = '', 
                        id = '', 
                        property_access_configs = [
                            visier.api.permission_management.models.property_access_config_dto.PropertyAccessConfigDTO(
                                access_level = 'None', 
                                analytic_object_id = '', 
                                analytic_object_reference_paths = [
                                    ''
                                    ], 
                                property_id = '', 
                                property_status = 'Unset', )
                            ], )
                    ]
            )
        else:
            return CreateDataAccessSetRequestDTO(
        )
        """

    def testCreateDataAccessSetRequestDTO(self):
        """Test CreateDataAccessSetRequestDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()