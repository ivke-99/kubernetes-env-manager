from fastapi import Request, Response, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import logging
from package.app.managers import AuthManager

logger = logging.getLogger(__name__)


class JWTBearer(HTTPBearer):

    payload = None

    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request, response: Response):
        credentials: HTTPAuthorizationCredentials = None
        try:
            credentials = await super(JWTBearer, self).__call__(request)
        except Exception as e:
            logger.warning("Issue with bearer {}".format(str(e)))
            raise HTTPException(status_code=401, detail="Invalid or no token.")
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=401, detail="Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=401, detail="Invalid or expired token.")
            request.credentials = self.payload
            return credentials.credentials
        raise HTTPException(status_code=401, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> bool:
        self.payload = None
        try:
            self.payload = AuthManager.decode_access_token(jwtoken)
        except Exception as e:
            logger.warning("Issue decoding JWT token. Error {}".format(str(e)))
        return self.payload
