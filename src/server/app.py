from fastapi import FastAPI

from src.server.lifespans import lifespan

from src.producer.views import router as producer_router


def create_app() -> FastAPI:
    app = FastAPI(version="0.1.0", lifespan=lifespan)
    app.include_router(producer_router, prefix="/producer")
    return app
