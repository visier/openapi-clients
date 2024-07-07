# coding: utf-8

"""
    Visier Public Platform APIs

    Visier APIs for querying data and model metadata

    The version of the OpenAPI document: 22222222.99201.1371
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.model_query.models.key_group_filter_item_dto import KeyGroupFilterItemDTO

class TestKeyGroupFilterItemDTO(unittest.TestCase):
    """KeyGroupFilterItemDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> KeyGroupFilterItemDTO:
        """Test KeyGroupFilterItemDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `KeyGroupFilterItemDTO`
        """
        model = KeyGroupFilterItemDTO()
        if include_optional:
            return KeyGroupFilterItemDTO(
                formula = '',
                selection_concept = visier.model_query.models.selection_concept_reference_dto.SelectionConceptReferenceDTO(
                    name = '', 
                    qualifying_path = '', ),
                member_set = visier.model_query.models.member_filter_dto.MemberFilterDTO(
                    dimension = null, 
                    values = null, )
            )
        else:
            return KeyGroupFilterItemDTO(
        )
        """

    def testKeyGroupFilterItemDTO(self):
        """Test KeyGroupFilterItemDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
