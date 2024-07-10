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
import lightly.openapi_generated.swagger_client.models


from typing import Optional
try:
    # Pydantic >=v1.10.17
    from pydantic.v1 import BaseModel, Field, StrictStr, constr, validator
except ImportError:
    # Pydantic v1
    from pydantic import BaseModel, Field, StrictStr, constr, validator
from lightly.openapi_generated.swagger_client.models.datasource_purpose import DatasourcePurpose

class DatasourceConfigBase(BaseModel):
    """
    DatasourceConfigBase
    """
    id: Optional[constr(strict=True)] = Field(None, description="MongoDB ObjectId")
    purpose: DatasourcePurpose = Field(...)
    type: StrictStr = Field(...)
    thumb_suffix: Optional[StrictStr] = Field(None, alias="thumbSuffix", description="the suffix of where to find the thumbnail image. If none is provided, the full image will be loaded where thumbnails would be loaded otherwise. - [filename]: represents the filename without the extension - [extension]: represents the files extension (e.g jpg, png, webp) ")
    __properties = ["id", "purpose", "type", "thumbSuffix"]

    @validator('id')
    def id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-f0-9]{24}$", value):
            raise ValueError(r"must validate the regular expression /^[a-f0-9]{24}$/")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True
        use_enum_values = True
        extra = "forbid"

    # JSON field name that stores the object type
    __discriminator_property_name = 'type'

    # discriminator mappings
    __discriminator_value_class_map = {
        'DatasourceConfigAzure': 'DatasourceConfigAzure',
        'DatasourceConfigGCS': 'DatasourceConfigGCS',
        'DatasourceConfigLIGHTLY': 'DatasourceConfigLIGHTLY',
        'DatasourceConfigLOCAL': 'DatasourceConfigLOCAL',
        'DatasourceConfigOBS': 'DatasourceConfigOBS',
        'DatasourceConfigS3': 'DatasourceConfigS3',
        'DatasourceConfigS3DelegatedAccess': 'DatasourceConfigS3DelegatedAccess'
    }

    @classmethod
    def get_discriminator_value(cls, obj: dict) -> str:
        """Returns the discriminator value (object type) of the data"""
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None

    def to_str(self, by_alias: bool = False) -> str:
        """Returns the string representation of the model"""
        return pprint.pformat(self.dict(by_alias=by_alias))

    def to_json(self, by_alias: bool = False) -> str:
        """Returns the JSON representation of the model"""
        return json.dumps(self.to_dict(by_alias=by_alias))

    @classmethod
    def from_json(cls, json_str: str) -> Union(DatasourceConfigAzure, DatasourceConfigGCS, DatasourceConfigLIGHTLY, DatasourceConfigLOCAL, DatasourceConfigOBS, DatasourceConfigS3, DatasourceConfigS3DelegatedAccess):
        """Create an instance of DatasourceConfigBase from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self, by_alias: bool = False):
        """Returns the dictionary representation of the model"""
        _dict = self.dict(by_alias=by_alias,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Union(DatasourceConfigAzure, DatasourceConfigGCS, DatasourceConfigLIGHTLY, DatasourceConfigLOCAL, DatasourceConfigOBS, DatasourceConfigS3, DatasourceConfigS3DelegatedAccess):
        """Create an instance of DatasourceConfigBase from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type:
            klass = getattr(lightly.openapi_generated.swagger_client.models, object_type)
            return klass.from_dict(obj)
        else:
            raise ValueError("DatasourceConfigBase failed to lookup discriminator value from " +
                             json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                             ", mapping: " + json.dumps(cls.__discriminator_value_class_map))

