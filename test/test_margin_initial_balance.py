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

from openapi_client.models.margin_initial_balance import MarginInitialBalance

class TestMarginInitialBalance(unittest.TestCase):
    """MarginInitialBalance unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MarginInitialBalance:
        """Test MarginInitialBalance
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MarginInitialBalance`
        """
        model = MarginInitialBalance()
        if include_optional:
            return MarginInitialBalance(
                accrued_interest = 1.337,
                available_funds_non_marginable_trade = 1.337,
                bond_value = 1.337,
                buying_power = 1.337,
                cash_balance = 1.337,
                cash_available_for_trading = 1.337,
                cash_receipts = 1.337,
                day_trading_buying_power = 1.337,
                day_trading_buying_power_call = 1.337,
                day_trading_equity_call = 1.337,
                equity = 1.337,
                equity_percentage = 1.337,
                liquidation_value = 1.337,
                long_margin_value = 1.337,
                long_option_market_value = 1.337,
                long_stock_value = 1.337,
                maintenance_call = 1.337,
                maintenance_requirement = 1.337,
                margin = 1.337,
                margin_equity = 1.337,
                money_market_fund = 1.337,
                mutual_fund_value = 1.337,
                reg_t_call = 1.337,
                short_margin_value = 1.337,
                short_option_market_value = 1.337,
                short_stock_value = 1.337,
                total_cash = 1.337,
                is_in_call = 1.337,
                unsettled_cash = 1.337,
                pending_deposits = 1.337,
                margin_balance = 1.337,
                short_balance = 1.337,
                account_value = 1.337
            )
        else:
            return MarginInitialBalance(
        )
        """

    def testMarginInitialBalance(self):
        """Test MarginInitialBalance"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
