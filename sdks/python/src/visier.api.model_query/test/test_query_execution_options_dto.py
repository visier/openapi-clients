# coding: utf-8

"""
    Visier Public Platform APIs

    Visier APIs for querying data and model metadata

    The version of the OpenAPI document: 22222222.99201.1389
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.api.model_query.models.query_execution_options_dto import QueryExecutionOptionsDTO

class TestQueryExecutionOptionsDTO(unittest.TestCase):
    """QueryExecutionOptionsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QueryExecutionOptionsDTO:
        """Test QueryExecutionOptionsDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QueryExecutionOptionsDTO`
        """
        model = QueryExecutionOptionsDTO()
        if include_optional:
            return QueryExecutionOptionsDTO(
                axis_visibility = 'SIMPLE',
                calendar_type = 'TENANT_CALENDAR',
                cell_distribution_options = visier.api.model_query.models.cell_distribution_options_dto.CellDistributionOptionsDTO(
                    bin_count = 56, ),
                currency_conversion_code = '',
                currency_conversion_date = '',
                currency_conversion_mode = 'TENANT_CURRENCY_CONVERSION',
                enable_descending_space = True,
                enable_sparse_results = True,
                internal = visier.api.model_query.models.internal_query_execution_options_dto.InternalQueryExecutionOptionsDTO(
                    align_time_axis_to_period_end = True, 
                    sparse_handling_mode = 'ALLOW', ),
                lineage_depth = 56,
                member_display_mode = 'DEFAULT',
                null_visibility = 'SHOW',
                zero_visibility = 'SHOW'
            )
        else:
            return QueryExecutionOptionsDTO(
        )
        """

    def testQueryExecutionOptionsDTO(self):
        """Test QueryExecutionOptionsDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()