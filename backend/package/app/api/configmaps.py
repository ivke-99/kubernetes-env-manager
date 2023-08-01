import logging
from typing import List

from fastapi import APIRouter, Body, Response, Depends
from package.app.managers import KubernetesManager
from package.app.schemas import (
    ConfigMapSchema,
    ConfigMapUpdateSchema,
    BaseResponseSchema,
    ConfigMapListSchema,
)
from package.app.auth import JWTBearer
from kubernetes.client import ApiException

logger = logging.getLogger(__name__)

configmap_router = APIRouter(
    prefix="/configmap",
    tags=["auth"],
)
manager = KubernetesManager()


@configmap_router.get("/", status_code=201, response_model=List[ConfigMapListSchema], dependencies=[Depends(JWTBearer())])
async def get_configmaps():
    return manager.get_configmaps()


@configmap_router.get(
    "/{configmap_name}/", response_model=ConfigMapSchema | BaseResponseSchema
)
async def get_configmap(response: Response, configmap_name: str):
    try:
        return manager.get_configmap(configmap_name, should_format=True)
    except ApiException:
        response.status_code = 404
        return {"message": "Configmap not found."}


@configmap_router.post("/", response_model=BaseResponseSchema, dependencies=[Depends(JWTBearer())])
async def create_configmap(response: Response, configmap: ConfigMapSchema = Body(...)):
    try:
        response = manager.create_configmap(configmap)
    except ApiException as e:
        response.status_code = 422
        return manager.format_kubernetes_api_exception(e)
    return {"message": "Success!"}


@configmap_router.put("/{configmap_name}/", response_model=BaseResponseSchema, dependencies=[Depends(JWTBearer())])
async def update_configmap(
    response: Response,
    configmap_name: str,
    configmap: ConfigMapUpdateSchema = Body(...),
):
    try:
        response = manager.update_configmap(configmap_name, configmap)
    except ApiException as e:
        response.status_code = 422
        return manager.format_kubernetes_api_exception(e)
    return {"message": "Success!"}
