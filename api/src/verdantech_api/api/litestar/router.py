from litestar import Router
from src.verdantech_api import settings

from .user.router import user_router

base_router = Router(path=settings.API_URL_BASE, route_handlers=[user_router])
