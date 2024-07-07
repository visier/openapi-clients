# coding: utf-8

"""
    Visier Public Platform APIs

    Visier APIs for querying data and model metadata

    The version of the OpenAPI document: 22222222.99201.1371
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class TimeShiftDTO(BaseModel):
    """
    The amount of time to shift the time interval by, such as backward by one year.
    """ # noqa: E501
    period_type: Optional[StrictStr] = Field(default=None, description="The time period type for the shift.", alias="periodType")
    period_count: Optional[StrictInt] = Field(default=None, description="The number of intervals. Default is 1.", alias="periodCount")
    direction: Optional[StrictStr] = Field(default=None, description="The direction to extend. Default is BACKWARD.")
    __properties: ClassVar[List[str]] = ["periodType", "periodCount", "direction"]

    @field_validator('period_type')
    def period_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['MONTH', 'DAY', 'WEEK', 'QUARTER', 'YEAR']):
            raise ValueError("must be one of enum values ('MONTH', 'DAY', 'WEEK', 'QUARTER', 'YEAR')")
        return value

    @field_validator('direction')
    def direction_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['BACKWARD', 'FORWARD']):
            raise ValueError("must be one of enum values ('BACKWARD', 'FORWARD')")
        return value

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
        """Create an instance of TimeShiftDTO from a JSON string"""
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
        """Create an instance of TimeShiftDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "periodType": obj.get("periodType"),
            "periodCount": obj.get("periodCount"),
            "direction": obj.get("direction")
        })
        return _obj

