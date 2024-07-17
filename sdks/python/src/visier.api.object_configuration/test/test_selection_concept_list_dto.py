# coding: utf-8

"""
    Visier Object Configuration APIs

    Visier APIs for managing objects in studio experience

    The version of the OpenAPI document: 22222222.99201.1389
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.api.object_configuration.models.selection_concept_list_dto import SelectionConceptListDTO

class TestSelectionConceptListDTO(unittest.TestCase):
    """SelectionConceptListDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SelectionConceptListDTO:
        """Test SelectionConceptListDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SelectionConceptListDTO`
        """
        model = SelectionConceptListDTO()
        if include_optional:
            return SelectionConceptListDTO(
                concepts = [
                    visier.api.object_configuration.models.selection_concept_dto.SelectionConceptDTO(
                        configuration = null, 
                        name = '', 
                        uuid = '', )
                    ]
            )
        else:
            return SelectionConceptListDTO(
        )
        """

    def testSelectionConceptListDTO(self):
        """Test SelectionConceptListDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
