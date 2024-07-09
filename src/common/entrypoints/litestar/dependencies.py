# External Libraries
from litestar_svcs import SvcsPlugin, SvcsPluginConfig

# VerdanTech Source
from src.common.adapters.registry import create_registry

svcs_plugin_config = SvcsPluginConfig(registry_factory=create_registry)
svcs_plugin = SvcsPlugin(svcs_plugin_config)
