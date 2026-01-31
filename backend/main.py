from fastapi import FastAPI
from backend.api.v1.router import router as api_router


def create_app() -> FastAPI:
    app = FastAPI(title="Intelligent Document Processing System")

    app.include_router(api_router, prefix="/api/v1")

    return app

app = create_app()
