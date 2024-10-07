import uvicorn

print("HERE MAIN", __name__)

if __name__ == "__main__":

    print("main")

    uvicorn.run(
        "world:world.fastapi_app",
        host="127.0.0.1",
        port=5000,
        reload=True,
        reload_dirs="world",
    )
