# coding: utf-8

"""
    Lightly API

    Lightly.ai enables you to do self-supervised learning in an easy and intuitive way. The lightly.ai OpenAPI spec defines how one can interact with our REST API to unleash the full potential of lightly.ai  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@lightly.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import Extra,  BaseModel, Field, StrictStr, constr, validator

class DatasourceConfigLOCALAllOf(BaseModel):
    """
    DatasourceConfigLOCALAllOf
    """
    full_path: StrictStr = Field(..., alias="fullPath", description="Relative path from the mount point. Not allowed to start with \"/\", contain \"://\" or contain \".\" or \"..\" directory parts.")
    web_server_location: Optional[constr(strict=True)] = Field(None, alias="webServerLocation", description="The webserver location where your local webserver is running to use for viewing images in the webapp when using the local datasource workflow. Defaults to http://localhost:3456 ")
    __properties = ["fullPath", "webServerLocation"]

    @validator('web_server_location')
    def web_server_location_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^https?:\/\/.+$", value):
            raise ValueError(r"must validate the regular expression /^https?:\/\/.+$/")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True
        use_enum_values = True
        extra = Extra.forbid

    def to_str(self, by_alias: bool = False) -> str:
        """Returns the string representation of the model"""
        return pprint.pformat(self.dict(by_alias=by_alias))

    def to_json(self, by_alias: bool = False) -> str:
        """Returns the JSON representation of the model"""
        return json.dumps(self.to_dict(by_alias=by_alias))

    @classmethod
    def from_json(cls, json_str: str) -> DatasourceConfigLOCALAllOf:
        """Create an instance of DatasourceConfigLOCALAllOf from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self, by_alias: bool = False):
        """Returns the dictionary representation of the model"""
        _dict = self.dict(by_alias=by_alias,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DatasourceConfigLOCALAllOf:
        """Create an instance of DatasourceConfigLOCALAllOf from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DatasourceConfigLOCALAllOf.parse_obj(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in DatasourceConfigLOCALAllOf) in the input: " + str(obj))

        _obj = DatasourceConfigLOCALAllOf.parse_obj({
            "full_path": obj.get("fullPath"),
            "web_server_location": obj.get("webServerLocation")
        })
        return _obj
