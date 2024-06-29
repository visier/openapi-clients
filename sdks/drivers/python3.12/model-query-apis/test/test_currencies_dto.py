# coding: utf-8

"""
    Visier Public Platform APIs

    Visier APIs for querying data and model metadata

    The version of the OpenAPI document: 22222222.99201.1081
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.model_query.models.currencies_dto import CurrenciesDTO

class TestCurrenciesDTO(unittest.TestCase):
    """CurrenciesDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CurrenciesDTO:
        """Test CurrenciesDTO
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CurrenciesDTO`
        """
        model = CurrenciesDTO()
        if include_optional:
            return CurrenciesDTO(
                currencies = [
                    visier.model_query.models.currency_dto.CurrencyDTO(
                        currency_code = '', 
                        display_name = '', 
                        symbol = '', 
                        short_symbol = '', )
                    ]
            )
        else:
            return CurrenciesDTO(
        )
        """

    def testCurrenciesDTO(self):
        """Test CurrenciesDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
