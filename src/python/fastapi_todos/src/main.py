from fastapi import FastAPI

from config import config
from routers.meta_router import router as meta_router


app = FastAPI(
    swagger_ui_parameters={"tryItOutEnabled": True},
    title=config.docs.title,
    debug=True,
    version=str(config.docs.version),
    description=config.docs.description,
)


@app.get("/", tags=["Meta"])
async def home() -> dict[str, str]:
    return {
        "title": config.docs.title,
        "description": config.docs.description,
        "version": str(config.docs.version),
    }


app.include_router(meta_router)
