import os
import jwt
import uuid
import time as t
import logging

logger = logging.getLogger(__name__)


class AuthManager:
    global_username = os.getenv("KUBE_USERNAME")
    global_password = os.getenv("KUBE_PASSWORD")
    app_secret_key = os.getenv("KUBE_APP_SECRET")

    @classmethod
    def check_credentials(cls, username, password):
        if username == cls.global_username and password == cls.global_password:
            return True
        return False

    @classmethod
    def create_access_token(cls):
        encoded_jwt = jwt.encode(
            {
                "username": cls.global_username,
                "random_uuid": uuid.uuid4().hex,
                "expires": t.time() + 60 * 30,
            },
            cls.app_secret_key,
            algorithm="HS256",
        )
        return encoded_jwt

    @classmethod
    def decode_access_token(cls, token: str) -> dict:
        try:
            decoded_token = jwt.decode(token, cls.app_secret_key, algorithms=["HS256"])
            return decoded_token if decoded_token["expires"] >= t.time() else {}
        except Exception as e:
            logger.error(
                "Error occured durring JWT token decoding. Error {}".format(str(e))
            )
            return {}
