# External Libraries
from litestar.openapi import OpenAPIConfig, spec

# VerdanTech Source

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
