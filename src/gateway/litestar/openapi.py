# Standard Library
from typing import Any

# External Libraries
import yaml
from litestar import status_codes
from litestar.openapi import OpenAPIConfig, spec
from litestar.openapi.datastructures import ResponseSpec

# VerdanTech Source
from src.ops.user.schemas.write import UserCreateInput
from src.utils.sanitizers.spec import SpecErrorMessage

from .auth import jwt_cookie_auth

openapi_config = OpenAPIConfig(
    title="VerdanTech-Backend",
    version="0.1.0",
    contact=spec.Contact(name="Nathaniel King"),
    description="Backend API of the VerdanTech software project.",
    external_docs=spec.ExternalDocumentation(
        url="https://github.com/VerdanTech/VerdanTech-Backend",
        description="Github Repository",
    ),
    license=spec.License(name="GNU GPL v3.0"),
    tags=[spec.Tag(name="users"), spec.Tag(name="gardens")],
    use_handler_docstrings=False,
)
