# coding: utf-8

"""
    Visier Public Platform APIs

    Visier APIs for querying data and model metadata

    The version of the OpenAPI document: 22222222.99201.1371
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.model_query_apis.api.query_api import QueryApi


class TestQueryApi(unittest.TestCase):
    """QueryApi unit test stubs"""

    def setUp(self) -> None:
        self.api = QueryApi()

    def tearDown(self) -> None:
        pass

    def test_aggregate(self) -> None:
        """Test case for aggregate

        Query aggregate data
        """
        pass

    def test_list(self) -> None:
        """Test case for list

        Query a list of details
        """
        pass

    def test_snapshot(self) -> None:
        """Test case for snapshot

        Query a series of detailed snapshots
        """
        pass

    def test_sql_like(self) -> None:
        """Test case for sql_like

        Query aggregate or list data using SQL-like syntax
        """
        pass


if __name__ == '__main__':
    unittest.main()