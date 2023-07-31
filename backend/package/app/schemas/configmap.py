from typing import Dict
from pydantic import BaseModel


class ConfigMapListSchema(BaseModel):
    name: str

    model_config = {
        "json_schema_extra": {
            "example": [
                {
                    "name": "front-config",
                },
                {
                    "name": "back-config",
                },
            ]
        }
    }


class ConfigMapSchema(BaseModel):
    name: str
    data: Dict[str, str]

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "front-config",
                "data": {"SOME_KEY": "SOME_VALUE"},
            },
        }
    }


class ConfigMapUpdateSchema(BaseModel):
    data: Dict[str, str]

    model_config = {
        "json_schema_extra": {"example": {"data": {"some_key": "some_value"}}}
    }
