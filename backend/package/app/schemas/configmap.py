from typing import Dict
from pydantic import BaseModel


class ConfigMapSchema(BaseModel):
    name: str
    data: Dict[str, str]

    class Config:
        json_schema_extra = {
            "example": [
                {
                    "name": "front-config",
                    "data": {"SOME_KEY": "SOME_VALUE"},
                },
                {
                    "name": "back-config",
                    "data": {
                        "APP_KEY": "ASDASD",
                        "STRIPE_KEY": "pk_test_aaa",
                    },
                },
            ]
        }
