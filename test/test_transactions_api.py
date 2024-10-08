# coding: utf-8

"""
    Trader API - Account Access and User Preferences

    Schwab Trader API access to Account, Order entry and User Preferences

    The version of the OpenAPI document: 1.0.0
    Contact: TraderAPI@Schwab.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.transactions_api import TransactionsApi


class TestTransactionsApi(unittest.TestCase):
    """TransactionsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TransactionsApi()

    def tearDown(self) -> None:
        pass

    def test_get_transactions_by_id(self) -> None:
        """Test case for get_transactions_by_id

        Get specific transaction information for a specific account
        """
        pass

    def test_get_transactions_by_path_param(self) -> None:
        """Test case for get_transactions_by_path_param

        Get all transactions information for a specific account.
        """
        pass


if __name__ == '__main__':
    unittest.main()
