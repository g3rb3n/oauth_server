from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def setup_app():
    """
    Create standard app
    """
    app = FastAPI()

    origins = []

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )
    return app


def include(app, lib, path):
    """
    Include router
    """
    app.include_router(
        lib.router,
        prefix=path,
        responses=lib.responses
    )
