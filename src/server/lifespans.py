from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.server.queue_app import get_kafka_broker


@asynccontextmanager
async def lifespan(app: FastAPI):
    broker = get_kafka_broker()
    await broker.start()
    yield
    await broker.close()
