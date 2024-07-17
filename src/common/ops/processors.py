from .messages import MessageProcessor

asgi_processor = MessageProcessor()
"""This is the message processor for the ASGI application."""
task_processor = MessageProcessor()
"""This is the message processor for the task backend."""
