# coding: utf-8

"""
    Visier Public Platform APIs

    Visier APIs for querying data and model metadata

    The version of the OpenAPI document: 22222222.99201.1371
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.model_query.models.query_time_intervals_dto import QueryTimeIntervalsDTO

class TestQueryTimeIntervalsDTO(unittest.TestCase):
    """QueryTimeIntervalsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QueryTimeIntervalsDTO:
        """Test QueryTimeIntervalsDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QueryTimeIntervalsDTO`
        """
        model = QueryTimeIntervalsDTO()
        if include_optional:
            return QueryTimeIntervalsDTO(
                from_instant = '',
                from_date_time = '',
                dynamic_date_from = '',
                interval_period_type = 'MONTH',
                interval_period_count = 56,
                interval_count = 56,
                direction = 'BACKWARD',
                shift = visier.model_query.models.time_shift_dto.TimeShiftDTO(
                    period_type = 'MONTH', 
                    period_count = 56, 
                    direction = 'BACKWARD', ),
                trailing_period_type = 'MONTH',
                trailing_period_count = 56
            )
        else:
            return QueryTimeIntervalsDTO(
        )
        """

    def testQueryTimeIntervalsDTO(self):
        """Test QueryTimeIntervalsDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
