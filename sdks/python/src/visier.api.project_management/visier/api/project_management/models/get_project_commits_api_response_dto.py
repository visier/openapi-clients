# coding: utf-8

"""
    Visier Project Management APIs

    Visier APIs for managing and publishing projects

    The version of the OpenAPI document: 22222222.99201.1389
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from visier.api.project_management.models.commit_dto import CommitDTO
from typing import Optional, Set
from typing_extensions import Self

class GetProjectCommitsAPIResponseDTO(BaseModel):
    """
    GetProjectCommitsAPIResponseDTO
    """ # noqa: E501
    commits: Optional[List[CommitDTO]] = Field(default=None, description="A list of committed changes in the project.")
    __properties: ClassVar[List[str]] = ["commits"]

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
        """Create an instance of GetProjectCommitsAPIResponseDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in commits (list)
        _items = []
        if self.commits:
            for _item in self.commits:
                if _item:
                    _items.append(_item.to_dict())
            _dict['commits'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetProjectCommitsAPIResponseDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "commits": [CommitDTO.from_dict(_item) for _item in obj["commits"]] if obj.get("commits") is not None else None
        })
        return _obj


