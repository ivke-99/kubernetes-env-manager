import os
import jwt
import uuid


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
            {"username": cls.global_username, "random_uuid": uuid.uuid4().hex}, cls.app_secret_key, algorithm="HS256"
        )
        return encoded_jwt
