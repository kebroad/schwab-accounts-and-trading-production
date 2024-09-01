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

from openapi_client.models.cash_account import CashAccount

class TestCashAccount(unittest.TestCase):
    """CashAccount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CashAccount:
        """Test CashAccount
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CashAccount`
        """
        model = CashAccount()
        if include_optional:
            return CashAccount(
                initial_balances = openapi_client.models.cash_initial_balance.CashInitialBalance(
                    accrued_interest = 1.337, 
                    cash_available_for_trading = 1.337, 
                    cash_available_for_withdrawal = 1.337, 
                    cash_balance = 1.337, 
                    bond_value = 1.337, 
                    cash_receipts = 1.337, 
                    liquidation_value = 1.337, 
                    long_option_market_value = 1.337, 
                    long_stock_value = 1.337, 
                    money_market_fund = 1.337, 
                    mutual_fund_value = 1.337, 
                    short_option_market_value = 1.337, 
                    short_stock_value = 1.337, 
                    is_in_call = 1.337, 
                    unsettled_cash = 1.337, 
                    cash_debit_call_value = 1.337, 
                    pending_deposits = 1.337, 
                    account_value = 1.337, ),
                current_balances = openapi_client.models.cash_balance.CashBalance(
                    cash_available_for_trading = 1.337, 
                    cash_available_for_withdrawal = 1.337, 
                    cash_call = 1.337, 
                    long_non_marginable_market_value = 1.337, 
                    total_cash = 1.337, 
                    cash_debit_call_value = 1.337, 
                    unsettled_cash = 1.337, ),
                projected_balances = openapi_client.models.cash_balance.CashBalance(
                    cash_available_for_trading = 1.337, 
                    cash_available_for_withdrawal = 1.337, 
                    cash_call = 1.337, 
                    long_non_marginable_market_value = 1.337, 
                    total_cash = 1.337, 
                    cash_debit_call_value = 1.337, 
                    unsettled_cash = 1.337, )
            )
        else:
            return CashAccount(
        )
        """

    def testCashAccount(self):
        """Test CashAccount"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
