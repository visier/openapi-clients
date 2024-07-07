# coding: utf-8

"""
    Visier Public Platform APIs

    Visier APIs for querying data and model metadata

    The version of the OpenAPI document: 22222222.99201.1371
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.model_query.models.key_group_filter_dto import KeyGroupFilterDTO

class TestKeyGroupFilterDTO(unittest.TestCase):
    """KeyGroupFilterDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> KeyGroupFilterDTO:
        """Test KeyGroupFilterDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `KeyGroupFilterDTO`
        """
        model = KeyGroupFilterDTO()
        if include_optional:
            return KeyGroupFilterDTO(
                filters = [
                    visier.model_query.models.key_group_filter_item_dto.KeyGroupFilterItemDTO(
                        formula = '', 
                        selection_concept = null, 
                        member_set = null, )
                    ]
            )
        else:
            return KeyGroupFilterDTO(
        )
        """

    def testKeyGroupFilterDTO(self):
        """Test KeyGroupFilterDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
