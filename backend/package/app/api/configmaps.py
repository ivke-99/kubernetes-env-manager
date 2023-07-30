import logging
from typing import List

from fastapi import APIRouter
from app.managers import KubernetesManager
from app.schemas import ConfigMapSchema

logger = logging.getLogger(__name__)

configmap_router = APIRouter(
    prefix="/configmap",
    tags=["auth"],
)


@configmap_router.get("/", response_model=List[ConfigMapSchema])
async def get_configmaps():
    return KubernetesManager().get_configmaps()
