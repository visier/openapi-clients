# coding: utf-8

"""
    Visier Public Platform APIs

    Visier APIs for querying data and model metadata

    The version of the OpenAPI document: 22222222.99201.1081
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from visier.model_query.models.parameter_definition_dto import ParameterDefinitionDTO
from typing import Optional, Set
from typing_extensions import Self

class MetricDTO(BaseModel):
    """
    A metric is a calculation based on one or more attribute values of analytic objects.
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="The unique ID of the metric. Note: See `Metrics` to get the ID.")
    display_name: Optional[StrictStr] = Field(default=None, description="The localized display name of the metric.", alias="displayName")
    description: Optional[StrictStr] = Field(default=None, description="The localized description of the metric.")
    data_start_date: Optional[StrictStr] = Field(default=None, description="The date from which data becomes available for this metric.  Note: Format is the number of milliseconds since midnight 01 January, 1970 UTC as a string.  Epochs are expressed as 64-bit integers and represented as stringified longs in JSON due to JSON's inherent  limitation in representing large numbers.", alias="dataStartDate")
    data_end_date: Optional[StrictStr] = Field(default=None, description="The date from which data is no longer available for this metric.  Note: Format is the number of milliseconds since midnight 01 January, 1970 UTC as a string.  Epochs are expressed as 64-bit integers and represented as stringified longs in JSON due to JSON's inherent  limitation in representing large numbers.", alias="dataEndDate")
    analytic_object_id: Optional[StrictStr] = Field(default=None, description="The unique ID of the analytic object.", alias="analyticObjectId")
    parameters: Optional[List[ParameterDefinitionDTO]] = Field(default=None, description="The collection of parameters defined for the metric.")
    category: Optional[StrictInt] = Field(default=None, description="The category of the metric. Will be one of: `REGULAR`, `DERIVED` or `PLANNING`.")
    visible_in_app: Optional[StrictBool] = Field(default=None, description="// `true` if this metric is set to be visible in your solution.", alias="visibleInApp")
    __properties: ClassVar[List[str]] = ["id", "displayName", "description", "dataStartDate", "dataEndDate", "analyticObjectId", "parameters", "category", "visibleInApp"]

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
        """Create an instance of MetricDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in parameters (list)
        _items = []
        if self.parameters:
            for _item in self.parameters:
                if _item:
                    _items.append(_item.to_dict())
            _dict['parameters'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MetricDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "displayName": obj.get("displayName"),
            "description": obj.get("description"),
            "dataStartDate": obj.get("dataStartDate"),
            "dataEndDate": obj.get("dataEndDate"),
            "analyticObjectId": obj.get("analyticObjectId"),
            "parameters": [ParameterDefinitionDTO.from_dict(_item) for _item in obj["parameters"]] if obj.get("parameters") is not None else None,
            "category": obj.get("category"),
            "visibleInApp": obj.get("visibleInApp")
        })
        return _obj

