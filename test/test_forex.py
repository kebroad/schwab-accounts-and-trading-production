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

from openapi_client.models.forex import Forex

class TestForex(unittest.TestCase):
    """Forex unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Forex:
        """Test Forex
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Forex`
        """
        model = Forex()
        if include_optional:
            return Forex(
                type = 'STANDARD',
                base_currency = None,
                counter_currency = None,
                asset_type = 'EQUITY',
                cusip = '',
                symbol = '',
                description = '',
                instrument_id = 56,
                net_change = 1.337
            )
        else:
            return Forex(
                asset_type = 'EQUITY',
        )
        """

    def testForex(self):
        """Test Forex"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
