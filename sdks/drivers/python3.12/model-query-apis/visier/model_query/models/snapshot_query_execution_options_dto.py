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
from typing import Optional, Set
from typing_extensions import Self

class SnapshotQueryExecutionOptionsDTO(BaseModel):
    """
    A SnapshotQueryExecutionOptions provides additional instructions to perform a snapshot query.
    """ # noqa: E501
    limit: Optional[StrictInt] = Field(default=None, description="The maximum number of entries to return. Default is to return all entries. If `page` is defined but  limit is not defined, limit will be set to a default value of 1000.")
    query_mode: Optional[StrictInt] = Field(default=None, description="Determines how the query should handle column definitions that the query is unable to resolve. Default is DEFAULT.", alias="queryMode")
    omit_header: Optional[StrictBool] = Field(default=None, description="Option to omit the header from the result.  If true, queryMode must be either FILL or FAIL.  Default is false.", alias="omitHeader")
    calendar_type: Optional[StrictInt] = Field(default=None, description="The calendar type to use. This will be used for all time calculations unless explicitly overridden in  the calculation itself. Default is TENANT_CALENDAR.", alias="calendarType")
    currency_conversion_date: Optional[StrictStr] = Field(default=None, description="The currency conversion date to use. If defined, the currency conversion will use the exchange rates as of this date.", alias="currencyConversionDate")
    page: Optional[StrictInt] = Field(default=None, description="A page defines a subset of the overall result set. The number of rows per page is equal to limit  with the exception of the last page in the result set which may contain fewer rows. `Page` is an index  that begins at 0. The index to start retrieving results is calculated by multiplying `page` by `limit`.")
    multiple_tables: Optional[StrictBool] = Field(default=None, description="Option to return multiple table files as zipped archive for derived metrics.  Default is false. If false, one table is returned for the drill-through metric.", alias="multipleTables")
    currency_conversion_code: Optional[StrictStr] = Field(default=None, description="The optional target currency for all currency conversions.  If not specified, the tenant default currency will be used.", alias="currencyConversionCode")
    __properties: ClassVar[List[str]] = ["limit", "queryMode", "omitHeader", "calendarType", "currencyConversionDate", "page", "multipleTables", "currencyConversionCode"]

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
        """Create an instance of SnapshotQueryExecutionOptionsDTO from a JSON string"""
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
        """Create an instance of SnapshotQueryExecutionOptionsDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "limit": obj.get("limit"),
            "queryMode": obj.get("queryMode"),
            "omitHeader": obj.get("omitHeader"),
            "calendarType": obj.get("calendarType"),
            "currencyConversionDate": obj.get("currencyConversionDate"),
            "page": obj.get("page"),
            "multipleTables": obj.get("multipleTables"),
            "currencyConversionCode": obj.get("currencyConversionCode")
        })
        return _obj


