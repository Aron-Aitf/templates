from time import perf_counter

from fastapi import FastAPI, Request

from logger import logger

from config import config

from routers.meta_router import router as meta_router


app = FastAPI(
    swagger_ui_parameters={"tryItOutEnabled": True},
    title=config.docs.title,
    debug=config.app.debug,
    version=str(config.docs.version),
    description=config.docs.description,
)

if config.app.log_requests:

    @app.middleware("http")
    async def logging_middleware(request: Request, call_next):

        logger.info(f"Request: {request.method} {request.url.path} received")
        start_time = perf_counter()

        response = await call_next(request)

        process_time = perf_counter() - start_time

        logger.info(
            f"Response: {request.method} {request.url.path} returned status code {response.status_code} in {process_time}"
        )

        return response


@app.get("/", tags=["Meta"])
async def home() -> dict[str, str]:
    return {
        "title": config.docs.title,
        "description": config.docs.description,
        "version": str(config.docs.version),
    }


app.include_router(meta_router)
