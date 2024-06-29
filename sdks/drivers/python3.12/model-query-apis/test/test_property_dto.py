# coding: utf-8

"""
    Visier Public Platform APIs

    Visier APIs for querying data and model metadata

    The version of the OpenAPI document: 22222222.99201.1081
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.model_query.models.property_dto import PropertyDTO

class TestPropertyDTO(unittest.TestCase):
    """PropertyDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PropertyDTO:
        """Test PropertyDTO
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PropertyDTO`
        """
        model = PropertyDTO()
        if include_optional:
            return PropertyDTO(
                id = '',
                display_name = '',
                description = '',
                data_type = '',
                primitive_data_type = '',
                parameters = [
                    visier.model_query.models.parameter_definition_dto.ParameterDefinitionDTO(
                        member_parameter = null, 
                        numeric_parameter = null, 
                        plan_parameter = null, 
                        aggregation_type_parameter = null, )
                    ]
            )
        else:
            return PropertyDTO(
        )
        """

    def testPropertyDTO(self):
        """Test PropertyDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
