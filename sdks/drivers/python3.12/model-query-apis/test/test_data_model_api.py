# coding: utf-8

"""
    Visier Public Platform APIs

    Visier APIs for querying data and model metadata

    The version of the OpenAPI document: 22222222.99201.1081
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.model_query.api.data_model_api import DataModelApi


class TestDataModelApi(unittest.TestCase):
    """DataModelApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DataModelApi()

    def tearDown(self) -> None:
        pass

    def test_data_model_analytic_object(self) -> None:
        """Test case for data_model_analytic_object

        Retrieve an analytic object by ID
        """
        pass

    def test_data_model_analytic_objects(self) -> None:
        """Test case for data_model_analytic_objects

        Retrieve a list of analytic objects
        """
        pass

    def test_data_model_currencies(self) -> None:
        """Test case for data_model_currencies

        Retrieve all currencies
        """
        pass

    def test_data_model_currency(self) -> None:
        """Test case for data_model_currency

        Retrieve a currency
        """
        pass

    def test_data_model_currency_rates(self) -> None:
        """Test case for data_model_currency_rates

        Retrieve all exchange rates for a currency
        """
        pass

    def test_data_model_currency_rates_with_to_currency(self) -> None:
        """Test case for data_model_currency_rates_with_to_currency

        Retrieve exchange rates from one currency to another currency
        """
        pass

    def test_data_model_dimension(self) -> None:
        """Test case for data_model_dimension

        Retrieve a dimension by ID
        """
        pass

    def test_data_model_dimensions(self) -> None:
        """Test case for data_model_dimensions

        Retrieve a list of dimensions
        """
        pass

    def test_data_model_member(self) -> None:
        """Test case for data_model_member

        Retrieve a dimension member
        """
        pass

    def test_data_model_members(self) -> None:
        """Test case for data_model_members

        Retrieve a list of dimension members
        """
        pass

    def test_data_model_metric(self) -> None:
        """Test case for data_model_metric

        Retrieve a metric by ID
        """
        pass

    def test_data_model_metric_dimensions(self) -> None:
        """Test case for data_model_metric_dimensions

        Retrieve a metric's dimensions
        """
        pass

    def test_data_model_metric_selection_concepts(self) -> None:
        """Test case for data_model_metric_selection_concepts

        Retrieve a metric's selection concepts
        """
        pass

    def test_data_model_metrics(self) -> None:
        """Test case for data_model_metrics

        Retrieve a list of metrics
        """
        pass

    def test_data_model_planning_metrics(self) -> None:
        """Test case for data_model_planning_metrics

        Retrieve metrics by planning model ID
        """
        pass

    def test_data_model_planning_model(self) -> None:
        """Test case for data_model_planning_model

        Retrieve a planning model by ID
        """
        pass

    def test_data_model_planning_models(self) -> None:
        """Test case for data_model_planning_models

        Retrieve a list of planning models
        """
        pass

    def test_data_model_planning_plan(self) -> None:
        """Test case for data_model_planning_plan

        Retrieve a plan by ID
        """
        pass

    def test_data_model_planning_plans(self) -> None:
        """Test case for data_model_planning_plans

        Retrieve a list of plans
        """
        pass

    def test_data_model_prediction(self) -> None:
        """Test case for data_model_prediction

        Retrieve a prediction by ID
        """
        pass

    def test_data_model_predictions(self) -> None:
        """Test case for data_model_predictions

        Retrieve a list of predictions
        """
        pass

    def test_data_model_properties(self) -> None:
        """Test case for data_model_properties

        Retrieve a list of properties
        """
        pass

    def test_data_model_property(self) -> None:
        """Test case for data_model_property

        Retrieve a property by ID
        """
        pass

    def test_data_model_selection_concept(self) -> None:
        """Test case for data_model_selection_concept

        Retrieve an analytic object's selection concept by ID
        """
        pass

    def test_data_model_selection_concepts(self) -> None:
        """Test case for data_model_selection_concepts

        Retrieve an analytic object's selection concepts
        """
        pass


if __name__ == '__main__':
    unittest.main()
