# coding: utf-8

"""
    Visier Permission Management APIs

    Visier APIs for managing permissions within an organization

    The version of the OpenAPI document: 22222222.99201.1389
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

class SecurablePropertyDTO(BaseModel):
    """
    SecurablePropertyDTO
    """ # noqa: E501
    analytic_object_id: Optional[StrictStr] = Field(default=None, description="The property's analytic object ID.", alias="analyticObjectId")
    display_name: Optional[StrictStr] = Field(default=None, description="An identifiable property name to display in Visier, such as \"Job Pay Level\".", alias="displayName")
    is_primary_key: Optional[StrictBool] = Field(default=None, description="If true, this property is the analytic object's primary key.", alias="isPrimaryKey")
    property_id: Optional[StrictStr] = Field(default=None, description="The property ID.", alias="propertyId")
    reference_symbol_name: Optional[StrictStr] = Field(default=None, description="The reference symbol name.", alias="referenceSymbolName")
    __properties: ClassVar[List[str]] = ["analyticObjectId", "displayName", "isPrimaryKey", "propertyId", "referenceSymbolName"]

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
        """Create an instance of SecurablePropertyDTO from a JSON string"""
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
        """Create an instance of SecurablePropertyDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "analyticObjectId": obj.get("analyticObjectId"),
            "displayName": obj.get("displayName"),
            "isPrimaryKey": obj.get("isPrimaryKey"),
            "propertyId": obj.get("propertyId"),
            "referenceSymbolName": obj.get("referenceSymbolName")
        })
        return _obj

