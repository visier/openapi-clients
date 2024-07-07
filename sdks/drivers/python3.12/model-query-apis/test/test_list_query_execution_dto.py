# coding: utf-8

"""
    Visier Public Platform APIs

    Visier APIs for querying data and model metadata

    The version of the OpenAPI document: 22222222.99201.1371
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.model_query.models.list_query_execution_dto import ListQueryExecutionDTO

class TestListQueryExecutionDTO(unittest.TestCase):
    """ListQueryExecutionDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListQueryExecutionDTO:
        """Test ListQueryExecutionDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListQueryExecutionDTO`
        """
        model = ListQueryExecutionDTO()
        if include_optional:
            return ListQueryExecutionDTO(
                source = visier.model_query.models.list_query_source_dto.ListQuerySourceDTO(
                    formula = '', 
                    metric = '', 
                    analytic_object = '', ),
                columns = [
                    visier.model_query.models.property_column_dto.PropertyColumnDTO(
                        column_name = '', 
                        column_definition = null, )
                    ],
                sort_options = [
                    visier.model_query.models.sort_option_dto.SortOptionDTO(
                        column_index = 56, 
                        sort_direction = 'SORT_ASCENDING', )
                    ],
                filters = [
                    visier.model_query.models.query_filter_dto.QueryFilterDTO(
                        formula = '', 
                        selection_concept = null, 
                        member_set = null, 
                        cohort = null, )
                    ],
                time_interval = visier.model_query.models.query_time_interval_dto.QueryTimeIntervalDTO(
                    from_instant = '', 
                    from_date_time = '', 
                    dynamic_date_from = '', 
                    interval_period_type = 'MONTH', 
                    interval_period_count = 56, 
                    direction = 'BACKWARD', 
                    shift = null, ),
                parameter_values = [
                    visier.model_query.models.query_parameter_value_dto.QueryParameterValueDTO(
                        member_value = null, 
                        numeric_value = null, 
                        plan_value = null, 
                        aggregation_type_value = null, )
                    ],
                options = visier.model_query.models.list_query_execution_options_dto.ListQueryExecutionOptionsDTO(
                    limit = 56, 
                    query_mode = 'DEFAULT', 
                    omit_header = True, 
                    calendar_type = 'TENANT_CALENDAR', 
                    currency_conversion_mode = 'TENANT_CURRENCY_CONVERSION', 
                    currency_conversion_date = '', 
                    page = 56, 
                    multiple_tables = True, 
                    currency_conversion_code = '', 
                    record_mode = 'NORMAL', 
                    date_time_display_mode = 'EPOCH', )
            )
        else:
            return ListQueryExecutionDTO(
        )
        """

    def testListQueryExecutionDTO(self):
        """Test ListQueryExecutionDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()