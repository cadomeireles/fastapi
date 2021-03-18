from fastapi import FastAPI

from .orders import endpoints

app = FastAPI()


app.include_router(endpoints.router)
