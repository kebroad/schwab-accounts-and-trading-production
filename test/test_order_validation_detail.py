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

from openapi_client.models.order_validation_detail import OrderValidationDetail

class TestOrderValidationDetail(unittest.TestCase):
    """OrderValidationDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderValidationDetail:
        """Test OrderValidationDetail
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderValidationDetail`
        """
        model = OrderValidationDetail()
        if include_optional:
            return OrderValidationDetail(
                validation_rule_name = '',
                message = '',
                activity_message = '',
                original_severity = 'ACCEPT',
                override_name = '',
                override_severity = 'ACCEPT'
            )
        else:
            return OrderValidationDetail(
        )
        """

    def testOrderValidationDetail(self):
        """Test OrderValidationDetail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
