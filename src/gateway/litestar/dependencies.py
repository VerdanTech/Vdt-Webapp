# External Libraries
from litestar_svcs import SvcsPlugin, SvcsPluginConfig
from svcs import Container

# VerdanTech Source
from src.adapters.registry import create_registry
from src.ops.common import MessageBus
from src.ops.handlers import ASGI_COMMAND_HANDLERS, ASGI_EVENT_HANDLERS

svcs_plugin_config = SvcsPluginConfig(registry_factory=create_registry)
svcs_plugin = SvcsPlugin(svcs_plugin_config)

def provide_message_bus(svcs_container: Container) -> MessageBus:
    return MessageBus(svcs_container=svcs_container, command_handlers=ASGI_COMMAND_HANDLERS, event_handlers=ASGI_EVENT_HANDLERS)