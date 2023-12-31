from fastapi import FastAPI
from api.db.base_class import Base
from api.db.session import engine
from api.core.config import settings
from api.routers.base import api_router


def create_tables():
    Base.metadata.create_all(bind=engine)


def include_router(app):
    app.include_router(api_router)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    create_tables()
    include_router(app)
    return app


app = start_application()


@app.get("/")
def read_root():
    return {"Hello": "World"}
