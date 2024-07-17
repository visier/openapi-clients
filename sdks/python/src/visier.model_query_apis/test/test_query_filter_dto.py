# coding: utf-8

"""
    Visier Public Platform APIs

    Visier APIs for querying data and model metadata

    The version of the OpenAPI document: 22222222.99201.1371
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.model_query_apis.models.query_filter_dto import QueryFilterDTO

class TestQueryFilterDTO(unittest.TestCase):
    """QueryFilterDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QueryFilterDTO:
        """Test QueryFilterDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QueryFilterDTO`
        """
        model = QueryFilterDTO()
        if include_optional:
            return QueryFilterDTO(
                cohort = visier.model_query_apis.models.cohort_filter_dto.CohortFilterDTO(
                    exclude = True, 
                    key_group = null, 
                    time_interval = null, ),
                formula = '',
                member_set = visier.model_query_apis.models.member_filter_dto.MemberFilterDTO(
                    dimension = null, 
                    values = null, ),
                selection_concept = visier.model_query_apis.models.selection_concept_reference_dto.SelectionConceptReferenceDTO(
                    name = '', 
                    qualifying_path = '', )
            )
        else:
            return QueryFilterDTO(
        )
        """

    def testQueryFilterDTO(self):
        """Test QueryFilterDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()