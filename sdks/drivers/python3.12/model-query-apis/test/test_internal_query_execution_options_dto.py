# coding: utf-8

"""
    Visier Public Platform APIs

    Visier APIs for querying data and model metadata

    The version of the OpenAPI document: 22222222.99201.1081
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.model_query.models.internal_query_execution_options_dto import InternalQueryExecutionOptionsDTO

class TestInternalQueryExecutionOptionsDTO(unittest.TestCase):
    """InternalQueryExecutionOptionsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InternalQueryExecutionOptionsDTO:
        """Test InternalQueryExecutionOptionsDTO
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InternalQueryExecutionOptionsDTO`
        """
        model = InternalQueryExecutionOptionsDTO()
        if include_optional:
            return InternalQueryExecutionOptionsDTO(
                sparse_handling_mode = 56
            )
        else:
            return InternalQueryExecutionOptionsDTO(
        )
        """

    def testInternalQueryExecutionOptionsDTO(self):
        """Test InternalQueryExecutionOptionsDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
