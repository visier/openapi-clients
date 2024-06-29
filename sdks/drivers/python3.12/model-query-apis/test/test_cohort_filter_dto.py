# coding: utf-8

"""
    Visier Public Platform APIs

    Visier APIs for querying data and model metadata

    The version of the OpenAPI document: 22222222.99201.1081
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.model_query.models.cohort_filter_dto import CohortFilterDTO

class TestCohortFilterDTO(unittest.TestCase):
    """CohortFilterDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CohortFilterDTO:
        """Test CohortFilterDTO
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CohortFilterDTO`
        """
        model = CohortFilterDTO()
        if include_optional:
            return CohortFilterDTO(
                key_group = visier.model_query.models.key_group_filter_dto.KeyGroupFilterDTO(
                    filters = [
                        visier.model_query.models.key_group_filter_item_dto.KeyGroupFilterItemDTO(
                            formula = '', 
                            selection_concept = null, 
                            member_set = null, )
                        ], ),
                exclude = True,
                time_interval = visier.model_query.models.query_time_interval_dto.QueryTimeIntervalDTO(
                    from_instant = '', 
                    from_date_time = '', 
                    interval_period_type = 56, 
                    interval_period_count = 56, 
                    direction = 56, 
                    shift = null, )
            )
        else:
            return CohortFilterDTO(
        )
        """

    def testCohortFilterDTO(self):
        """Test CohortFilterDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
