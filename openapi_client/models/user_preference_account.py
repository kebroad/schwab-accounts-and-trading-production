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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class UserPreferenceAccount(BaseModel):
    """
    UserPreferenceAccount
    """ # noqa: E501
    account_number: Optional[StrictStr] = Field(default=None, alias="accountNumber")
    primary_account: Optional[StrictBool] = Field(default=False, alias="primaryAccount")
    type: Optional[StrictStr] = None
    nick_name: Optional[StrictStr] = Field(default=None, alias="nickName")
    account_color: Optional[StrictStr] = Field(default=None, description="Green | Blue", alias="accountColor")
    display_acct_id: Optional[StrictStr] = Field(default=None, alias="displayAcctId")
    auto_position_effect: Optional[StrictBool] = Field(default=False, alias="autoPositionEffect")
    __properties: ClassVar[List[str]] = ["accountNumber", "primaryAccount", "type", "nickName", "accountColor", "displayAcctId", "autoPositionEffect"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of UserPreferenceAccount from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserPreferenceAccount from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accountNumber": obj.get("accountNumber"),
            "primaryAccount": obj.get("primaryAccount") if obj.get("primaryAccount") is not None else False,
            "type": obj.get("type"),
            "nickName": obj.get("nickName"),
            "accountColor": obj.get("accountColor"),
            "displayAcctId": obj.get("displayAcctId"),
            "autoPositionEffect": obj.get("autoPositionEffect") if obj.get("autoPositionEffect") is not None else False
        })
        return _obj


