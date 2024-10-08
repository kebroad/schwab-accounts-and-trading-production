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

from openapi_client.models.transaction import Transaction

class TestTransaction(unittest.TestCase):
    """Transaction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Transaction:
        """Test Transaction
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Transaction`
        """
        model = Transaction()
        if include_optional:
            return Transaction(
                activity_id = 56,
                time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                user = openapi_client.models.user_details.UserDetails(
                    cd_domain_id = '', 
                    login = '', 
                    type = 'ADVISOR_USER', 
                    user_id = 56, 
                    system_user_name = '', 
                    first_name = '', 
                    last_name = '', 
                    broker_rep_code = '', ),
                description = '',
                account_number = '',
                type = 'TRADE',
                status = 'VALID',
                sub_account = 'CASH',
                trade_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                settlement_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                position_id = 56,
                order_id = 56,
                net_amount = 1.337,
                activity_type = 'ACTIVITY_CORRECTION',
                transfer_items = [
                    openapi_client.models.transfer_item.TransferItem(
                        instrument = null, 
                        amount = 1.337, 
                        cost = 1.337, 
                        price = 1.337, 
                        fee_type = 'COMMISSION', 
                        position_effect = 'OPENING', )
                    ]
            )
        else:
            return Transaction(
        )
        """

    def testTransaction(self):
        """Test Transaction"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
