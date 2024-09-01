# coding: utf-8

"""
    Trader API - Account Access and User Preferences

    Schwab Trader API access to Account, Order entry and User Preferences

    The version of the OpenAPI document: 1.0.0
    Contact: TraderAPI@Schwab.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class TransactionType(str, Enum):
    """
    TransactionType
    """

    """
    allowed enum values
    """
    TRADE = 'TRADE'
    RECEIVE_AND_DELIVER = 'RECEIVE_AND_DELIVER'
    DIVIDEND_OR_INTEREST = 'DIVIDEND_OR_INTEREST'
    ACH_RECEIPT = 'ACH_RECEIPT'
    ACH_DISBURSEMENT = 'ACH_DISBURSEMENT'
    CASH_RECEIPT = 'CASH_RECEIPT'
    CASH_DISBURSEMENT = 'CASH_DISBURSEMENT'
    ELECTRONIC_FUND = 'ELECTRONIC_FUND'
    WIRE_OUT = 'WIRE_OUT'
    WIRE_IN = 'WIRE_IN'
    JOURNAL = 'JOURNAL'
    MEMORANDUM = 'MEMORANDUM'
    MARGIN_CALL = 'MARGIN_CALL'
    MONEY_MARKET = 'MONEY_MARKET'
    SMA_ADJUSTMENT = 'SMA_ADJUSTMENT'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TransactionType from a JSON string"""
        return cls(json.loads(json_str))


