# coding: utf-8

"""
    Visier Data Intake APIs

    Visier APIs for sending raw or untransformed source data to Visier

    The version of the OpenAPI document: 22222222.99201.1389
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.api.data_intake.models.push_data_source_definition_dto import PushDataSourceDefinitionDTO

class TestPushDataSourceDefinitionDTO(unittest.TestCase):
    """PushDataSourceDefinitionDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PushDataSourceDefinitionDTO:
        """Test PushDataSourceDefinitionDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PushDataSourceDefinitionDTO`
        """
        model = PushDataSourceDefinitionDTO()
        if include_optional:
            return PushDataSourceDefinitionDTO(
                columns = [
                    visier.api.data_intake.models.push_data_column_definition_dto.PushDataColumnDefinitionDTO(
                        allow_empty = True, 
                        column_name = '', 
                        data_formats = [
                            ''
                            ], 
                        data_type = '', 
                        default_value = '', 
                        is_mandatory = True, )
                    ],
                is_inherited = True,
                name = '',
                source_id = ''
            )
        else:
            return PushDataSourceDefinitionDTO(
        )
        """

    def testPushDataSourceDefinitionDTO(self):
        """Test PushDataSourceDefinitionDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()