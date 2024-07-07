# coding: utf-8

"""
    Visier Authentication APIs

    Visier API for requesting an authentication token through basic authentication.

    The version of the OpenAPI document: 22222222.99201.1371
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.authentication.api.authentication_api import AuthenticationApi


class TestAuthenticationApi(unittest.TestCase):
    """AuthenticationApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AuthenticationApi()

    def tearDown(self) -> None:
        pass

    def test_authentication_asid_token_authentication(self) -> None:
        """Test case for authentication_asid_token_authentication

        Request a Visier authentication token.
        """
        pass


if __name__ == '__main__':
    unittest.main()
