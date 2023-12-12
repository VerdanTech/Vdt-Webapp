# External Libraries
from litestar_svcs import SvcsPlugin, SvcsPluginConfig

# VerdanTech Source
from src.dependencies.registry import registry

svcs_plugin_config = SvcsPluginConfig(registry=registry)
svcs_plugin = SvcsPlugin(svcs_plugin_config)
