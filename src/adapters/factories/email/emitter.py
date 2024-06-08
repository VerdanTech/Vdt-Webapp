# External Libraries
from svcs import Container

# VerdanTech Source
from src.adapters.email.emitter.saq import SaqEmailEmitter
from src.interfaces.email.client import AbstractEmailClient


async def provide_saq_email_emitter(svcs_container: Container) -> SaqEmailEmitter:
    # Todo: Implement Queueing
    client = await svcs_container.aget_abstract(AbstractEmailClient)
    emitter = SaqEmailEmitter(client=client)
    return emitter
