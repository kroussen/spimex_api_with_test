import uvicorn

from fastapi import FastAPI

from api.spimex import router


def create_app():
    _app = FastAPI()
    _app.include_router(router)

    return _app


app = create_app()

# @app.on_event("shutdown")
# async def shutdown_event():
#     await redis_cache.close()


if __name__ == "__main__":
    uvicorn.run(app='main:app', port=8000, reload=True)
