# External Libraries
from litestar.config.cors import CORSConfig

cors_config = CORSConfig(
    allow_origins=["http://localhost:5173"], allow_credentials=True
)
