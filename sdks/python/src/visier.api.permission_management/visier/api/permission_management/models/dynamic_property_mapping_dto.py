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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from visier.api.permission_management.models.user_property_dto import UserPropertyDTO
from typing import Optional, Set
from typing_extensions import Self

class DynamicPropertyMappingDTO(BaseModel):
    """
    DynamicPropertyMappingDTO
    """ # noqa: E501
    hierarchy_property_id: Optional[StrictStr] = Field(default=None, description="The unique ID of the property.", alias="hierarchyPropertyId")
    hierarchy_property_status: Optional[StrictStr] = Field(default=None, description="The property's validity status. Valid values: `Valid`, `NotFound`.  * **Valid**: The object exists and has loaded data.  * **NotFound**: The object doesn't exist.", alias="hierarchyPropertyStatus")
    user_property: Optional[UserPropertyDTO] = Field(default=None, description="The user property that you want to link the name property or organization head to.", alias="userProperty")
    __properties: ClassVar[List[str]] = ["hierarchyPropertyId", "hierarchyPropertyStatus", "userProperty"]

    @field_validator('hierarchy_property_status')
    def hierarchy_property_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Unset', 'Valid', 'NoData', 'NotFound']):
            raise ValueError("must be one of enum values ('Unset', 'Valid', 'NoData', 'NotFound')")
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
        """Create an instance of DynamicPropertyMappingDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of user_property
        if self.user_property:
            _dict['userProperty'] = self.user_property.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DynamicPropertyMappingDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "hierarchyPropertyId": obj.get("hierarchyPropertyId"),
            "hierarchyPropertyStatus": obj.get("hierarchyPropertyStatus"),
            "userProperty": UserPropertyDTO.from_dict(obj["userProperty"]) if obj.get("userProperty") is not None else None
        })
        return _obj

