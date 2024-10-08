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

from openapi_client.models.order_strategy import OrderStrategy

class TestOrderStrategy(unittest.TestCase):
    """OrderStrategy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderStrategy:
        """Test OrderStrategy
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderStrategy`
        """
        model = OrderStrategy()
        if include_optional:
            return OrderStrategy(
                account_number = '',
                advanced_order_type = 'NONE',
                close_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                entered_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                order_balance = openapi_client.models.order_balance.OrderBalance(
                    order_value = 1.337, 
                    projected_available_fund = 1.337, 
                    projected_buying_power = 1.337, 
                    projected_commission = 1.337, ),
                order_strategy_type = 'SINGLE',
                order_version = 1.337,
                session = 'NORMAL',
                status = 'AWAITING_PARENT_ORDER',
                all_or_none = True,
                discretionary = True,
                duration = 'DAY',
                filled_quantity = 1.337,
                order_type = 'MARKET',
                order_value = 1.337,
                price = 1.337,
                quantity = 1.337,
                remaining_quantity = 1.337,
                sell_non_marginable_first = True,
                settlement_instruction = 'REGULAR',
                strategy = 'NONE',
                amount_indicator = 'DOLLARS',
                order_legs = [
                    openapi_client.models.order_leg.OrderLeg(
                        ask_price = 1.337, 
                        bid_price = 1.337, 
                        last_price = 1.337, 
                        mark_price = 1.337, 
                        projected_commission = 1.337, 
                        quantity = 1.337, 
                        final_symbol = '', 
                        leg_id = 1.337, 
                        asset_type = 'EQUITY', 
                        instruction = 'BUY', )
                    ]
            )
        else:
            return OrderStrategy(
        )
        """

    def testOrderStrategy(self):
        """Test OrderStrategy"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
