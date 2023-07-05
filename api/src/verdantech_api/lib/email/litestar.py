from litestar.events import listener

from . import provide_email_client


@listener("send_email")
async def send_email_emitter(
    self, filepath: str, receiver: str, subject: str, **kwargs
):
    client = provide_email_client()
    await client.compile_and_send(
        filepath=filepath, receiver=receiver, subject=subject, **kwargs
    )
