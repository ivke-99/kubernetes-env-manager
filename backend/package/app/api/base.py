from fastapi import APIRouter, Response
from package.app.schemas.common import BaseResponseSchema
import logging

logger = logging.getLogger(__name__)

base_router = APIRouter(
    prefix="",
    tags=["base"],
)


@base_router.get("/", response_model=BaseResponseSchema)
async def read_root(response: Response) -> dict:
    response.status_code = 200
    return {"message": "Welcome to Rest API!"}


@base_router.get("/health", response_model=BaseResponseSchema)
async def health(response: Response) -> dict:
    response.status_code = 200
    return {"message": "Rest API is working correctly"}
