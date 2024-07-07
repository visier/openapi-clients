# coding: utf-8

"""
    Visier Public Platform APIs

    Visier APIs for querying data and model metadata

    The version of the OpenAPI document: 22222222.99201.1371
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.model_query.models.lineage_dto import LineageDTO

class TestLineageDTO(unittest.TestCase):
    """LineageDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LineageDTO:
        """Test LineageDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LineageDTO`
        """
        model = LineageDTO()
        if include_optional:
            return LineageDTO(
                cell_sets = [
                    visier.model_query.models.cell_set_dto.CellSetDTO(
                        cells = [
                            visier.model_query.models.cell_dto.CellDTO(
                                value = '', 
                                support = '', 
                                coordinates = [
                                    56
                                    ], 
                                distribution = [
                                    visier.model_query.models.cell_distribution_bin_dto.CellDistributionBinDTO(
                                        value = '', 
                                        support = '', )
                                    ], )
                            ], 
                        axes = [
                            visier.model_query.models.cell_set_axis_dto.CellSetAxisDTO(
                                dimension = null, 
                                positions = [
                                    visier.model_query.models.cell_set_axis_position_dto.CellSetAxisPositionDTO(
                                        path = [
                                            ''
                                            ], 
                                        display_name = '', 
                                        display_name_path = [
                                            ''
                                            ], )
                                    ], )
                            ], 
                        lineage = null, )
                    ],
                op = ''
            )
        else:
            return LineageDTO(
        )
        """

    def testLineageDTO(self):
        """Test LineageDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()