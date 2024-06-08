# External Libraries
from saq import Queue

# VerdanTech Source
from src import settings
from src.adapters.email.emitter.saq import send_email

queue = Queue.from_url(settings.REDIS_URI)

settings = {
    "queue": queue,
    "functions": [send_email],
    "concurrency": settings.SAQ_WORKERS,
}
