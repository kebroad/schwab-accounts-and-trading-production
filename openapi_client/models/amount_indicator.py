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


class AmountIndicator(str, Enum):
    """
    AmountIndicator
    """

    """
    allowed enum values
    """
    DOLLARS = 'DOLLARS'
    SHARES = 'SHARES'
    ALL_SHARES = 'ALL_SHARES'
    PERCENTAGE = 'PERCENTAGE'
    UNKNOWN = 'UNKNOWN'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AmountIndicator from a JSON string"""
        return cls(json.loads(json_str))


