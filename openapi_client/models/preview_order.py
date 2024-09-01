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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.commission_and_fee import CommissionAndFee
from openapi_client.models.order_strategy import OrderStrategy
from openapi_client.models.order_validation_result import OrderValidationResult
from typing import Optional, Set
from typing_extensions import Self

class PreviewOrder(BaseModel):
    """
    PreviewOrder
    """ # noqa: E501
    order_id: Optional[StrictInt] = Field(default=None, alias="orderId")
    order_strategy: Optional[OrderStrategy] = Field(default=None, alias="orderStrategy")
    order_validation_result: Optional[OrderValidationResult] = Field(default=None, alias="orderValidationResult")
    commission_and_fee: Optional[CommissionAndFee] = Field(default=None, alias="commissionAndFee")
    __properties: ClassVar[List[str]] = ["orderId", "orderStrategy", "orderValidationResult", "commissionAndFee"]

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
        """Create an instance of PreviewOrder from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of order_strategy
        if self.order_strategy:
            _dict['orderStrategy'] = self.order_strategy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of order_validation_result
        if self.order_validation_result:
            _dict['orderValidationResult'] = self.order_validation_result.to_dict()
        # override the default output from pydantic by calling `to_dict()` of commission_and_fee
        if self.commission_and_fee:
            _dict['commissionAndFee'] = self.commission_and_fee.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PreviewOrder from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "orderId": obj.get("orderId"),
            "orderStrategy": OrderStrategy.from_dict(obj["orderStrategy"]) if obj.get("orderStrategy") is not None else None,
            "orderValidationResult": OrderValidationResult.from_dict(obj["orderValidationResult"]) if obj.get("orderValidationResult") is not None else None,
            "commissionAndFee": CommissionAndFee.from_dict(obj["commissionAndFee"]) if obj.get("commissionAndFee") is not None else None
        })
        return _obj


