from pydantic import BaseModel


class TokenSchema(BaseModel):
    access_token: str


class LoginSchema(BaseModel):
    username: str
    password: str
