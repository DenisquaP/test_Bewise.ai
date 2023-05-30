from fastapi import FastAPI
# import asyncio
import uvicorn

from api.routers import router
# from database import create_metadata


app = FastAPI(
    title='task2'
)

app.include_router(router)


# async def main():
#     await create_metadata()


if __name__ == '__main__':
    # asyncio.run(main())
    uvicorn.run('main:app', reload=True)
