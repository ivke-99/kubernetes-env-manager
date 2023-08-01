import logging

from fastapi import Response, APIRouter
from package.app.managers import AuthManager
from package.app.schemas import TokenSchema, BaseResponseSchema, LoginSchema

logger = logging.getLogger(__name__)

auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@auth_router.post("/login/", response_model=TokenSchema | BaseResponseSchema)
async def login(form_data: LoginSchema, response: Response):
    is_valid = AuthManager.check_credentials(form_data.username, form_data.password)
    if is_valid:
        token = AuthManager.create_access_token()
        return {"access_token": token}
    response.status_code = 422
    return {"message": "Invalid username or password."}
