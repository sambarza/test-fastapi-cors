from datetime import datetime
import time
import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI, APIRouter, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

print("HERE WORLD")


class World:
    world_router = APIRouter()

    def __init__(self) -> None:
        print("INIT WORLD")
        self.status = "STOPPED"
        self.fastapi_app = FastAPI(lifespan=World.fastapi_lifespan)

        self.fastapi_app.mount(
            "/static", StaticFiles(directory="static"), name="static"
        )

        origins = [
            # "http://test.sam.com:5000"
        ]

        self.fastapi_app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        self.fastapi_app.include_router(self.world_router)

    async def start(self):
        self.task_print_time = asyncio.create_task(self.print_time())
        self.counter = 0
        self.status = "RUNNING"

    async def print_time(self):
        print("Starting print_time")
        while True:
            await asyncio.sleep(1)
            print(datetime.now())

    @world_router.get("/")
    def status(request: Request):
        world = request.app.state.world
        return world.status

    @world_router.get("/add")
    def add(request: Request):
        world = request.app.state.world
        counter = world.counter
        time.sleep(0.1)
        world.counter = counter + 1
        return world.counter

    @world_router.get("/add_async")
    async def add(request: Request):
        world = request.app.state.world
        counter = world.counter
        await asyncio.sleep(0.1)
        world.counter = counter + 1
        return world.counter

    @world_router.get("/counter")
    def add(request: Request):
        world = request.app.state.world
        return world.counter

    @world_router.get("/reset")
    def add(request: Request):
        world = request.app.state.world
        world.counter = 0
        return world.counter

    @world_router.get("/delay")
    def add(request: Request):
        for i in range(1000000000):
            pass
        return world.counter

    @staticmethod
    @asynccontextmanager
    async def fastapi_lifespan(fastapi_app: FastAPI):
        print("Start lifespan")
        fastapi_app.state.world = world
        await world.start()
        yield
        print("End lifespan")


world = World()
