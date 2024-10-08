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
import pprint
import re  # noqa: F401
import json

from importlib import import_module
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from openapi_client.models.position import Position
from typing import Optional, Set
from typing_extensions import Self

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from openapi_client.models.cash_account import CashAccount
    from openapi_client.models.margin_account import MarginAccount

class SecuritiesAccountBase(BaseModel):
    """
    SecuritiesAccountBase
    """ # noqa: E501
    type: Optional[StrictStr] = None
    account_number: Optional[StrictStr] = Field(default=None, alias="accountNumber")
    round_trips: Optional[StrictInt] = Field(default=None, alias="roundTrips")
    is_day_trader: Optional[StrictBool] = Field(default=False, alias="isDayTrader")
    is_closing_only_restricted: Optional[StrictBool] = Field(default=False, alias="isClosingOnlyRestricted")
    pfcb_flag: Optional[StrictBool] = Field(default=False, alias="pfcbFlag")
    positions: Optional[List[Position]] = None
    __properties: ClassVar[List[str]] = ["type", "accountNumber", "roundTrips", "isDayTrader", "isClosingOnlyRestricted", "pfcbFlag", "positions"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['CASH', 'MARGIN']):
            raise ValueError("must be one of enum values ('CASH', 'MARGIN')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[str] = 'type'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'CashAccount': 'CashAccount','MarginAccount': 'MarginAccount'
    }

    @classmethod
    def get_discriminator_value(cls, obj: Dict[str, Any]) -> Optional[str]:
        """Returns the discriminator value (object type) of the data"""
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Union[CashAccount, MarginAccount]]:
        """Create an instance of SecuritiesAccountBase from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in positions (list)
        _items = []
        if self.positions:
            for _item_positions in self.positions:
                if _item_positions:
                    _items.append(_item_positions.to_dict())
            _dict['positions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Union[CashAccount, MarginAccount]]:
        """Create an instance of SecuritiesAccountBase from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type ==  'CashAccount':
            return import_module("openapi_client.models.cash_account").CashAccount.from_dict(obj)
        if object_type ==  'MarginAccount':
            return import_module("openapi_client.models.margin_account").MarginAccount.from_dict(obj)

        raise ValueError("SecuritiesAccountBase failed to lookup discriminator value from " +
                            json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                            ", mapping: " + json.dumps(cls.__discriminator_value_class_map))


